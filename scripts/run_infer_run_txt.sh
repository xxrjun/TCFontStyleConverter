src_txt=$1

python infer.py \
--experiment_dir ./experiment \
--embedding_num 40 \
--gpu_ids cuda:0 \
--resume 4950 \
--batch_size 32 \
--from_txt \
--src_txt $src_txt \
--label 0 \
--type_file type/宋黑类字符集.txt \
