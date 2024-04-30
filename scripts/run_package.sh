
split_ratio=$1

python ./package.py \
--dir ./datasets/examples \
--save_dir ./experiment/data \
--split_ratio $split_ratio \