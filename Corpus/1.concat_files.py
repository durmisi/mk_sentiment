import glob2

pos_filenames = glob2.glob('pos/*.txt')  # list of all .txt files in the directory
neg_filenames = glob2.glob('neg/*.txt')  # list of all .txt files in the directory

with open('positive.txt', 'w') as f:
    for file in pos_filenames:
        with open(file) as infile:
            f.write(infile.read()+'\n')


with open('negative.txt', 'w') as f:
    for file in neg_filenames:
        with open(file) as infile:
            f.write(infile.read()+'\n')