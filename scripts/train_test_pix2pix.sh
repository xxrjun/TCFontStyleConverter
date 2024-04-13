# 設置一個函數來檢查上一個命令是否成功執行
check_status() {
  if [ $? -ne 0 ]; then
    echo "Error: $1"
    exit 1
  fi
}

# 進行模型訓練
echo "Starting model training..."
python ../train.py --dataroot ../datasets/FontHandWriting_Dataset_pix2pix \
                  --name fontA2B \
                  --model pix2pix \
                  --direction AtoB \
                  --dataset_mode unaligned \
                  --no_flip \
                  --input_nc 1 \
                  --output_nc 1 \
                  --display_id 0 \
                  --gpu_ids 0 \
                  --checkpoints_dir ../checkpoints
check_status "Model training failed."

# 檢查模型檔案是否存在，如果不存在則退出
if [ ! -f "../checkpoints/fontA2B/latest_net_G.pth" ]; then
  echo "Model file not found."
  exit 1
fi

# 進行模型測試
echo "Starting model testing..."
python ../test.py --dataroot ../datasets/FontHandWriting_Dataset_pix2pix \
                  --name fontA2B \
                  --model pix2pix \
                  --dataset_mode unaligned \
                  --input_nc 1 \
                  --output_nc 1 \
                  --no_dropout \
                  --no_flip \
                  --direction AtoB \
                  --checkpoints_dir ../checkpoints\
                  --results_dir ../results
check_status "Model testing failed."

echo "Training and testing completed successfully."
