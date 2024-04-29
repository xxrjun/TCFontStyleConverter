sample_count=$1
dst_font=$2
label=$3

python font2img.py --src_font ./charset/src/*.ttf \
                   --dst_font ./charset/dst/{$dst_font}.ttf \
                   --charset CN \
                   --sample_count $sample_count \
                   --sample_dir ./examples \
                   --label 0 \
                   --filter \
                   --shuffle \
                   --mode font2font