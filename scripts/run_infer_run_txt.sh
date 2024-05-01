src_txt=$1
resume=$2
label=$3


python infer.py \
--experiment_dir ./experiment \
--embedding_num 40 \
--gpu_ids cuda:0 \
--resume $resume \
--from_txt \
--src_txt $src_txt \
--label $label
