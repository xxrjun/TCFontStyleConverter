# Traditional Chinese Font Style Transfer using CycleGAN

## Environment
According to the original repo, the following dependencies are required:
- torch>=1.4.0
- torchvision>=0.5.0
- dominate>=2.4.0
- visdom>=0.1.8.8
- wandb

And the prerequisites are as follows:
- Linux or macOS
- Python 3
- CPU or NVIDIA GPU + CUDA CuDNN

To use the required tools for downloading the dataset, please make sure you have the following tools installed:
- gdown
- pyenv

I personally use miniconda to manage my environment. You can create a new environment with the following command:

```bash
conda env create -n yourenvname
```

To activate the environment, use the following command:
```bash
conda activate yourenvname
```

Install the required packages:
```bash
pip install -r requirements.txt
```

## Dataset
First, download `.env` which has the access token for dataset by running the following command:
```bash
!gdown --id xxxxxxxxxxxxxxxxxxxxxxx(Please ask author for the access token)
```

Then, move to the directory `scripts` by running the following command:
```bash
cd ./scripts
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

