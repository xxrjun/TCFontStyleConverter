# 設置一個函數來檢查上一個命令是否成功執行
check_status() {
  if [ $? -ne 0 ]; then
    echo "Error: $1"
    exit 1
  fi
}

# 調用Python腳本並評估其輸出以設置環境變量
eval $(python ./util/load_env.py)

# 使用環境變量中的ACCESS_TOKEN來下載datasets
echo "Cloning the dataset repository..."
git clone https://YCHM0304:${ACCESS_TOKEN}@github.com/YCHM0304/FontHandWriting_Dataset_CycleGAN.git
check_status "Failed to clone the dataset repository."

# 檢查數據集目錄是否存在，如果不存在則退出
if [ ! -d "./FontHandWriting_Dataset_CycleGAN" ]; then
  echo "Dataset directory not found."
  exit 1
fi

# 移動數據集目錄到正確的位置
echo "Moving dataset directory..."
mv ./FontHandWriting_Dataset_CycleGAN ../datasets/FontHandWriting_Dataset_CycleGAN
check_status "Failed to move the dataset directory."

echo "Dataset cloning and moving completed successfully."
