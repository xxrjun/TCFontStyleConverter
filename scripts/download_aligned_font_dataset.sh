# 設置一個函數來檢查上一個命令是否成功執行
check_status() {
  if [ $? -ne 0 ]; then
    echo "Error: $1"
    exit 1
  fi
}


# 下載datasets
echo "Downloading the dataset..."
gdown --id 18myYEqh3jXodfWPqiR_fB5qSNuwQbKeJ --output "../datasets/FontHandWriting_Dataset_pix2pix.zip"
check_status "Failed to download the dataset repository."

echo "Unzipping the dataset..."
unzip -q "../datasets/FontHandWriting_Dataset_pix2pix.zip" -d "../datasets/"
check_status "Failed to unzip the dataset."

rm "../datasets/FontHandWriting_Dataset_pix2pix.zip"

# 檢查數據集目錄是否存在，如果不存在則退出
if [ ! -d "../datasets/FontHandWriting_Dataset_CycleGAN" ]; then
  echo "Dataset directory not found."
  exit 1
else
  echo "Dataset downloading and unzipping completed successfully."
fi



# 解壓縮dataset

echo "Dataset downloading and unzipping completed successfully."
