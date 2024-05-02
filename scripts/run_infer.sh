resume=$1

python infer.py \
--experiment_dir ./experiment \
--embedding_num 40 \
--start_from 0 \
--gpu_ids cuda:0 \
--resume $resume \
--obj_path experiment/data/val.obj