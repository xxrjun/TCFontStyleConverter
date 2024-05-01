sample_count=1250
src_font=PMingLiU-02
dst_font=DFHsiu-W3-WIN-BF-01
split_ratio=0.2

check_status() {
  if [ $? -ne 0 ]; then
    echo "Error: $1"
    exit 1
  fi
}

echo "Generating the dataset..."
python ./font2img.py --src_font ./datasets/charset/src/$src_font.ttf \
                   --dst_font ./datasets/charset/dst/$dst_font.ttf \
                   --charset CN \
                   --sample_count $sample_count \
                   --sample_dir ./datasets/Dataset_Pix2pix \
                   --filter \
                   --shuffle \
                   --mode font2font \
                   --for_cycleGAN

# 檢查數據集目錄是否存在，如果不存在則退出
if [ ! -d "./datasets/Dataset_Pix2pix" ]; then
  echo "Dataset directory not found."
  exit 1
fi

echo "Spliting dataset into training dataset and testing dataset..."
python ./util/split_train_val.py \
--dir ./datasets/Dataset_Pix2pix \
--split_ratio $split_ratio
check_status "Failed to split the dataset."

