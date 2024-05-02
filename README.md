# Traditional Chinese Font Style Transfer using CycleGAN　and zi2zi(A pix2pix implementation)

- [Traditional Chinese Font Style Transfer using CycleGAN　and zi2zi(A pix2pix implementation)](#traditional-chinese-font-style-transfer-using-cycleganand-zi2zia-pix2pix-implementation)
  - [Environment Building](#environment-building)
    - [Pix2pix and CycleGAN](#pix2pix-and-cyclegan)
    - [Zi2zi](#zi2zi)
  - [Dataset](#dataset)
    - [Pix2pix and CycleGAN](#pix2pix-and-cyclegan-1)
    - [Zi2Zi](#zi2zi-1)
  - [Training and Testing](#training-and-testing)
    - [Pix2pix and CycleGAN](#pix2pix-and-cyclegan-2)
    - [Zi2zi](#zi2zi-2)
  - [References](#references)

## Environment Building

According to the original repo, the following dependencies are required:
### Pix2pix and CycleGAN
- `torch>=1.4.0`
- `torchvision>=0.5.0`
- `dominate>=2.4.0`
- `visdom>=0.1.8.8`
- `wandb`
### Zi2zi
- `Python 3.7`
- `CUDA 10.2`
- `cudnn 7.6.5`
- `pytorch 1.5.1`
- `pillow 7.1.2`
- `numpy 1.18.1`
- `scipy 1.4.1`
- `imageio 2.8.0`

*The version of torch and torchvision are too old for my environment, so I updated them to a newer version.*

And the prerequisites are as follows:

- Linux or macOS
- Python 3
- CPU or NVIDIA GPU + CUDA CuDNN

I personally use miniconda to manage my environment. You can create a new environment with the following command which will automatically install all the required packages:

```bash
conda env create -f environment.yml
```
The name of the environment is set to `fontConverter`, so to activate the environment, use the following command:

```bash
conda activate fontConverter
```

## Dataset
### Pix2pix and CycleGAN
> [!TIP]
> Please ask the author for the access token to download the dataset.

Copy `.env.example` to `.env` and fill in the access token for the dataset.

```bash
cp .env.example .env
```

Open `.env` and fill in the access token for the dataset.

```bash
ACCESS_TOKEN=<access_token>
```

Or you can download the dataset manually by running the following command:

```bash
gdown --id <access_token>
```


Run the following shell script to download **Paired Dataset for pix2pix**:

```bash
./scripts/download_paired_font_dataset.sh
```

Run the following shell script to download **Unpaired Dataset for cycleGAN**:

```bash
./scripts/download_font_dataset.sh
```

Another way to generate the dataset is to use the given fonts and convert them to images. The fonts should be in `.ttf` format.

First, download tons of fonts as you please and put **one** source font in `./datasets/charset/src` and **put any number less than 40 of** target fonts in `./datasets/charset/dst`. The fonts should be in `.ttf` format.
```bash
datasets
  └─ charset
      ├─src         (n = 1)
      │  └─src.ttf
      └─dst         (n <= 40)
        ├─dst1.ttf
        ├─dst2.ttf
        └─dst?.ttf
```

Then run the following command to convert the source font and target fonts to images for **pix2pix**:

```bash
bash ./scripts/generate_dataset_Pix2pix.sh
```

Run the following command to convert the source font and target fonts to images for **CycleGAN**:

```bash
bash ./scripts/generate_dataset_CycleGAN.sh
```
The dataset will be saved in the `./datasets/Dataset_CycleGAN` or `./datasets/Dataset_Pix2pix` directory with the following structure:

```bash
datasets
  ├─Dataset_CycleGAN
  │  ├─trainA
  │  ├─trainB
  │  ├─testA
  │  └─testB
  └─Dataset_Pix2pix
     ├─trainA
     ├─trainB
     ├─testA
     └─testB
```

You can open these two shell scripts and modify the following parameters:
- `sample_number`: the number of samples to generate
- `src_font`: the name of the source font
- `dst_font`: the name of the target font
- `split_ratio`: the ratio of the training set to the validation set

### Zi2Zi
Download tons of fonts as you please and put **one** source font in `./datasets/charset/src` and **put any number less than 40 of** target fonts in `./datasets/charset/dst`. The fonts should be in `.ttf` format.
```bash
datasets
  └─ charset
      ├─src         (n = 1)
      │  └─src.ttf
      └─dst         (n <= 40)
        ├─dst1.ttf
        ├─dst2.ttf
        └─dst?.ttf
```
Then, run the following command to convert the source font and target fonts to images:

```bash
bash ./scripts/run_font2font.sh <sample_number> <src_font> <dst_font> <label>
```
- `sample_number`: the number of samples to generate
- `src_font`: the name of the source font
- `dst_font`: the name of the target font
- `label`: the label of the target font

For example, you have `a.ttf` for the source font and `b.ttf`, `c.ttf`, `d.ttf` for the target fonts, and you want to generate 1000 samples for each target font, you can run the following command:

```bash
bash ./scripts/run_font2font.sh 1000 b 0
bash ./scripts/run_font2font.sh 1000 c 1
bash ./scripts/run_font2font.sh 1000 d 2
```
**Suggestion**: Use the same source font, and different target font will give you better performance.

**Demo**: For example, you have a.ttf, b.ttf, c.ttf, d.ttf. And you want to use a.ttf as source font. First, you should give b.ttf ~ d.ttf each one an ID.

| b.ttf | c.ttf | d.ttf |
| ----- | ----- | ----- |
| 0     | 1     | 2     |

After running all the commands, run the following command to generate the dataset:

```bash
bash ./scripts/run_package.sh <split_ratio>
```
`split_ratio`: the ratio of the training set to the validation set

The dataset will be saved in the `./experiment/data` directory with the following structure:

```bash
data
  ├─train.obj
  └─val.obj
```
## Training and Testing

### Pix2pix and CycleGAN

Run the following shell script to **train and test Pix2pix**:

```bash
./scripts/train_test_pix2pix.sh
```

Run the following shell script to **train and test CycleGAN**:

```bash
./scripts/train_test_cycleGAN.sh
```

*Be sure to modify all the parameters which are needed in the shell script before running the script.*


For detailed information, you can run the following command to see the help message:

```bash
python train.py --help
python test.py --help
```

### Zi2zi
Before training the model, you need to open the `run_train_zi2zi.sh` file and modify the following parameters:
- `epoch`: the number of epochs
- `batch_size`: the batch size
- `sample_steps`: the every number of steps to save the sample
- `checkpoint_steps`: the every number of steps to save the checkpoint

Then, run the following command to train the model:

```bash
bash ./scripts/run_train_zi2zi.sh
```

*During the training process, the generated images will be saved with the following folder structure. Additionally, only the first image of each label from every training epoch will be saved.*

```sh
experiment
    └─sample
        ├─train
        │  ├─images
        │  │   ├─epoch_0
        │  │   │  ├─label_0.png
        │  │   │  └─label_?.png
        │  │   └─epoch_?
        │  │      ├─label_0.png
        │  │      └─label_?.png
        │  └─index.html
        └─val
        ├─images
        │   ├─epoch_0
        │   │  ├─label_0.png
        │   │  └─label_?.png
        │   ├─epoch_?
        │   │  ├─label_0.png
        │   │  └─label_?.png
        │   └─latest
        │      ├─label_0.png
        │      └─label_?.png
        └─index.html
```
Zi2zi has two ways to test the model. The first way is to test the model with the validation set. Run the following command to test the model with the validation set:

```bash
bash ./scripts/run_infer.sh <resume>
```
`resume`: which step of checkpoint to generate the image
The second way is to test the model with the source font that you can type any Chinese characters you want to convert to the target font. Run the following command to test the model with the source font:

```bash
bash ./scripts/run_infer_run_txt.sh <src_txt> <resume> <label>
```
- `src_txt`: type any Chinese characters you want to convert to the target font
- `resume`: which step of checkpoint to generate the image
- `label`: which target font you want to convert to. The label was set when you generate the dataset.



## References

- [junyanz/pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
- [kaonashi-tyc/zi2zi](https://github.com/kaonashi-tyc/zi2zi)
- [EuphoriaYan/zi2zi-pytorch](https://github.com/EuphoriaYan/zi2zi-pytorch?tab=readme-ov-file)