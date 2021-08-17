import os
import glob

directory = "datasets_korean/train_data"

def main():
    for dir1 in os.listdir(directory):  # KsponSpeech_01
        dir1_filepath = os.path.join(directory, dir1)
        for dir2 in os.listdir(dir1_filepath):    # KsponSpeech_0001
            dir2_filepath = os.path.join(dir1_filepath, dir2)
            encoded_dest = f"{dir1}-{dir2}.trans.txt"
            destination = os.path.join(dir2_filepath, encoded_dest)

            read_files = glob.glob(f"{dir2_filepath}/*.txt")     # read all txt files
            with open(destination, "w") as outfile:
                for f in read_files:
                    if f.split("/")[-1] != destination.split("/")[-1]:
                        with open(f, "r", encoding="cp949") as infile:
                            try:
                                x = infile.read()
                                outfile.write(f"{str(f)[:-4].split('/')[-1]} {x}")
                            except:     # ignore if outfile (UTF-8)
                                print(f, "writing error")
                                pass


if __name__ == '__main__':
    main()
