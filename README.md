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
To use the provided dataset:
1. Put `.env` file in the directory `datasets` of the project.
2. Run the following shell script:
```bash
./train_test.sh
```

The dataset will be downloaded.

## Testing
According to the original repo, if the parameter `--model` is set to `test` and you only test one direction, the file name of the saved model `latest_net_G_A.pth` should be manually changed to `latest_net_G.pth`.

Run the following shell script to change the file name of the saved model:
```python
os.rename("./checkpoints/*name/latest_net_G_A.pth", "./checkpoints/*name/latest_net_G.pth")
```
*Replace `*name` with the value of `--name` you set earlier in the training process.*

