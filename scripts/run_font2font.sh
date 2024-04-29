sample_count=$1
src_font=$2
dst_font=$3
label=$4

python font2img.py --src_font ./charset/src/{$src_font}.ttf \
                   --dst_font ./charset/dst/{$dst_font}.ttf \
                   --charset CN \
                   --sample_count $sample_count \
                   --sample_dir ./examples \
                   --label 0 \
                   --filter \
                   --shuffle \
                   --mode font2font