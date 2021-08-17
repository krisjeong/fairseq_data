import subprocess
import os
#!/usr/bin/env python3

directory = os.path.abspath("datasets_korean/train_data")
# directory = os.path.abspath("datasets_korean/test_data/eval_clean")
# directory = os.path.abspath("datasets_korean_copy/train_data")

def main():
    for dir1 in os.listdir(directory):  # KsponSpeech_01
        dir1_filepath = os.path.join(directory, dir1)
        for dir2 in os.listdir(dir1_filepath):    # KsponSpeech_0001
            dir2_filepath = os.path.join(dir1_filepath, dir2)
            os.chdir(dir2_filepath)
            print(os.getcwd())
            subprocess.run(['sh', "/home/kris/workspace/repo/fairseq/pcm2wav.sh"])

if __name__ == '__main__':
    main()