import argparse
import glob
import os
import random

parser = argparse.ArgumentParser(description='Compile list of images into a pickled object for training')
parser.add_argument('--dir', required=True, help='path of examples')
parser.add_argument('--split_ratio', type=float, default=0.1, dest='split_ratio',
                    help='split ratio between train and val')
parser.add_argument('--shuffle', action='store_true', help='shuffle the dataset before splitting')

args = parser.parse_args()

def split_train_val(dir, split_ratio, shuffle=False):
    trainA_paths = glob.glob(os.path.join(dir, 'trainA', '*.jpg'))
    trainB_paths = glob.glob(os.path.join(dir, 'trainB', '*.jpg'))

    if args.shuffle:
        random.shuffle(trainB_paths)

    numA_val = int(len(trainA_paths) * split_ratio)
    numB_val = int(len(trainB_paths) * split_ratio)

    testA_paths = trainA_paths[:numA_val]
    testB_paths = trainB_paths[:numB_val]

    if not os.path.exists(os.path.join(dir, 'testA')):
        os.makedirs(os.path.join(dir, 'testA'))
    if not os.path.exists(os.path.join(dir, 'testB')):
        os.makedirs(os.path.join(dir, 'testB'))

    for testA_path in testA_paths:
        os.rename(testA_path, os.path.join(dir, 'testA', os.path.basename(testA_path)))
    for testB_path in testB_paths:
        os.rename(testB_path, os.path.join(dir, 'testB', os.path.basename(testB_path)))

if __name__ == '__main__':
    split_train_val(args.dir, args.split_ratio, args.shuffle)