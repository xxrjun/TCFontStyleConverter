from data import DatasetFromObj
from torch.utils.data import DataLoader
from models.zi2zi import Zi2ZiModel
from util.htmlZi2zi import HTML
import os
import sys
import argparse
import torch
import random
import time
import math

parser = argparse.ArgumentParser(description='Train')
parser.add_argument('--experiment_dir', required=True,
                    help='experiment directory, data, samples,checkpoints,etc')
parser.add_argument('--gpu_ids', default=[], nargs='+', help="GPUs")
parser.add_argument('--augment', default=[], nargs='+',
                    help="Data augmentaiton options: bold, rotate, blur, use multiple options \
                    by separating them with space")
parser.add_argument('--image_size', type=int, default=256,
                    help="size of your input and output image")
parser.add_argument('--L1_penalty', type=int, default=100, help='weight for L1 loss')
parser.add_argument('--Lconst_penalty', type=int, default=15, help='weight for const loss')
# parser.add_argument('--Ltv_penalty', dest='Ltv_penalty', type=float, default=0.0, help='weight for tv loss')
parser.add_argument('--Lcategory_penalty', type=float, default=1.0,
                    help='weight for category loss')
parser.add_argument('--embedding_num', type=int, default=40,
                    help="number for distinct embeddings")
parser.add_argument('--embedding_dim', type=int, default=128, help="dimension for embedding")
parser.add_argument('--epoch', type=int, default=100, help='number of epoch')
parser.add_argument('--batch_size', type=int, default=16, help='number of examples in batch')
parser.add_argument('--lr', type=float, default=0.001, help='initial learning rate for adam')
parser.add_argument('--schedule', type=int, default=20, help='number of epochs to half learning rate')
parser.add_argument('--freeze_encoder', action='store_true',
                    help="freeze encoder weights during training")
parser.add_argument('--fine_tune', type=str, default=None,
                    help='specific labels id to be fine tuned')
parser.add_argument('--inst_norm', action='store_true',
                    help='use conditional instance normalization in your model')
parser.add_argument('--sample_steps', type=int, default=10,
                    help='number of batches in between two samples are drawn from validation set')
parser.add_argument('--checkpoint_steps', type=int, default=100,
                    help='number of batches in between two checkpoints')
parser.add_argument('--flip_labels', action='store_true',
                    help='whether flip training data labels or not, in fine tuning')
parser.add_argument('--random_seed', type=int, default=777,
                    help='random seed for random and pytorch')
parser.add_argument('--resume', type=int, default=None, help='resume from previous training')
parser.add_argument('--input_nc', type=int, default=3,
                    help='number of input images channels')

def chkormakedir(path):
    if not os.path.isdir(path) and not os.path.exists(path):
        os.makedirs(path)

def main():
    args = parser.parse_args()
    random.seed(args.random_seed)
    torch.manual_seed(args.random_seed)

    data_dir = os.path.join(args.experiment_dir, "data")
    checkpoint_dir = os.path.join(args.experiment_dir, "checkpoint")
    chkormakedir(checkpoint_dir)
    train_sample_dir = os.path.join(args.experiment_dir, "sample", "train")
    val_sample_dir = os.path.join(args.experiment_dir, "sample", "val")

    start_time = time.time()

    # train_dataset = DatasetFromObj(os.path.join(data_dir, 'train.obj'),
    #                                augment=True, bold=True, rotate=True, blur=True)
    # val_dataset = DatasetFromObj(os.path.join(data_dir, 'val.obj'))
    # dataloader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True)

    model = Zi2ZiModel(
        input_nc=args.input_nc,
        embedding_num=args.embedding_num,
        embedding_dim=args.embedding_dim,
        Lconst_penalty=args.Lconst_penalty,
        Lcategory_penalty=args.Lcategory_penalty,
        save_dir=checkpoint_dir,
        gpu_ids=args.gpu_ids
    )
    model.setup()
    model.print_networks(True)
    if args.resume:
        model.load_networks(args.resume)

    # val dataset load only once, no shuffle
    val_dataset = DatasetFromObj(os.path.join(data_dir, 'val.obj'), input_nc=args.input_nc)
    val_dataloader = DataLoader(val_dataset, batch_size=args.batch_size, shuffle=True)

    global_steps = 0
    train_webpage = HTML(train_sample_dir, 'Training results')
    val_webpage = HTML(val_sample_dir, 'Validation results')



    for epoch in range(args.epoch):
        # generate train dataset every epoch so that different styles of saved char imgs can be trained.
        train_dataset = DatasetFromObj(
            os.path.join(data_dir, 'train.obj'),
            input_nc = args.input_nc,
            augment = not args.augment == [],
            bold = 'bold' in args.augment,
            rotate = 'rotate' in args.augment,
            blur = 'blur' in args.augment,
        )
        total_batches = math.ceil(len(train_dataset) / args.batch_size)
        dataloader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True)
        model.sample_reset()
        for bid, batch in enumerate(dataloader):
            model.set_input(batch[0], batch[2], batch[1])
            const_loss, l1_loss, category_loss, cheat_loss = model.optimize_parameters()
            if bid % 100 == 0:
                passed = time.time() - start_time
                log_format = "Epoch: [%2d], [%4d/%4d] time: %4.2f, d_loss: %.5f, g_loss: %.5f, " + \
                             "category_loss: %.5f, cheat_loss: %.5f, const_loss: %.5f, l1_loss: %.5f"
                print(log_format % (epoch, bid, total_batches, passed, model.d_loss.item(), model.g_loss.item(),
                                    category_loss, cheat_loss, const_loss, l1_loss))
            if global_steps % args.checkpoint_steps == 0:
                model.save_networks(global_steps)
                print("Checkpoint: save checkpoint step %d" % global_steps)
            if global_steps % args.sample_steps == 0:
                if not model.sample_saved:
                    # save training results of the current batch and validation results
                    model.sample(batch, train_sample_dir, epoch, train_webpage)
                    model.sample_reset()
                    for val_batch in val_dataloader:
                        model.sample(val_batch, val_sample_dir, epoch, val_webpage)
                    model.sample_done()
                    print("Sample: sample step %d" % global_steps)
                else:
                    print("This result of this epoch has been saved, skip this step")
            global_steps += 1
        if (epoch + 1) % args.schedule == 0:
            model.update_lr()
    # save latest validation results
    model.sample_reset()
    for val_batch in val_dataloader:
        model.sample(val_batch, val_sample_dir, 'latest', val_webpage)
        print("Checkpoint: save checkpoint step %d" % global_steps)
    train_webpage.save()
    val_webpage.save()
    model.save_networks(global_steps)


if __name__ == '__main__':
    main()
