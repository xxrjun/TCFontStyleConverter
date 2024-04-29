sample_count=1000

python font2img.py --src_font ./charset/src/PMingLiU-02.ttf \
                   --dst_font ./charset/dst/DFHsiu-W3-WIN-BF-01.ttf \
                   --charset CN \
                   --sample_count $sample_count \
                   --sample_dir ./examples \
                   --label 0 \
                   --filter \
                   --shuffle \
                   --mode font2font