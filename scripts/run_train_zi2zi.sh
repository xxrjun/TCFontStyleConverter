epoch=50
batch_size=64
sample_steps=200
checkpoint_steps=500


python trainZi2zi.py \
--experiment_dir ./experiment \
--gpu_ids cuda:0 \
--epoch $epoch \
--batch_size $batch_size \
--sample_steps $sample_steps \
--checkpoint_steps $checkpoint_steps \
--input_nc 1 \
