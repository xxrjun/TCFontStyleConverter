
split_ratio=$1

python ./util/package.py \
--dir ./datasets/examples \
--save_dir ./experiment/data \
--split_ratio $split_ratio \