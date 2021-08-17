#!/usr/bin/env bash

# Find all .pcm files and convert them to .wav format.
for input_file in `find . -name "*.pcm"`
do
  output_file="${input_file%.pcm}.wav"
  ffmpeg -v quiet -f s16le -ar 16k -ac 1 -i $input_file $output_file
done