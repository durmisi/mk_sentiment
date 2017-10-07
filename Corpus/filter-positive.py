# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')


import nltk, re, pprint
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string

stop_words = set(stopwords.words('english'))

print '=========================================positive====================================='
all_words = []
with open('positive.txt', 'r') as f:
    for line in f.readlines():
        for sent in sent_tokenize(line):
            # print sent
            word_tokens = word_tokenize(sent)
            for w in word_tokens:
                if w not in stop_words:
                    all_words.append(w.lower())


all_words_cleaned = [''.join(x for x in par if x not in string.punctuation) for par in all_words]
all_words_cleaned = [x for x in all_words_cleaned if x != '']

# print all_words_cleaned

all_words_freq_dist = nltk.FreqDist(all_words_cleaned)
for mc in all_words_freq_dist.most_common(300):
    print mc


with open('positive_filtered.txt', 'w') as output:
    for word,freqin in all_words_freq_dist.most_common(300):
        output.write("{}\n".format(word))
