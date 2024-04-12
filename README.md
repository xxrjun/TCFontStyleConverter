# Traditional Chinese Font Style Transfer using CycleGAN

- [Environment Building](#environment-building)
- [Dataset](#dataset)
  - [Paired Dataset for pix2pix](#paired-dataset-for-pix2pix)
  - [Unpaired Dataset for cycleGAN](#unpaired-dataset-for-cyclegan)
- [Training and Testing](#training-and-testing)
  - [Train and test Pix2pix](#train-and-test-pix2pix)
  - [Train and test CycleGAN](#train-and-test-cyclegan)
- [References](#references)

## Environment Building

According to the original repo, the following dependencies are required:

- `torch>=1.4.0`
- `torchvision>=0.5.0`
- `dominate>=2.4.0`
- `visdom>=0.1.8.8`
- `wandb`

And the prerequisites are as follows:

- Linux or macOS
- Python 3
- CPU or NVIDIA GPU + CUDA CuDNN

I personally use miniconda to manage my environment. You can create a new environment with the following command:

```bash
conda create -n font-transfer python=3.10
```

To activate the environment, use the following command:

```bash
conda activate font-transfer
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Dataset

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

Then, move to the directory `scripts` by running the following command:

```bash
cd scripts
```

### Paired Dataset for pix2pix

Run the following shell script:

```bash
./download_aligned_font_dataset.sh
```

### Unpaired Dataset for cycleGAN

Run the following shell script:

```bash
./download_font_dataset.sh
```

## Training and Testing

### Train and test Pix2pix

Run the following shell script:

```bash
./train_test_pix2pix.sh
```

### Train and test CycleGAN

Run the following shell script:

```bash
./train_test_cycleGAN.sh
```

## References

- [junyanz/pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)