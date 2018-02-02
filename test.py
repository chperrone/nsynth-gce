BUNDLE_PATH='Downloads/basic_rnn.mag'
CONFIG='basic_rnn'

melody_rnn_generate \
--config='basic_rnn' \
--bundle_file='Download/basic_rnn.mag' \
--output_dir='/tmp/melody_rnn/generated' \
--num_outputs=10 \
--num_steps=128 \
--primer_melody="[60]"
