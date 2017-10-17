#!/usr/bin/env python
# -*- coding: utf-8 -*-

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from googletrans import Translator
translator = Translator()

print ("=============================== NEGATIVE =====================================")
with open('negative_filtered_translations.txt', 'w') as nft:
    with open('negative_filtered.txt', 'r') as f:
        for word in f.readlines():
            try:
                translation = translator.translate(word.rstrip(), dest='mk')
                if translation is not None:
                    print (word)
                    print (translation.text)
                    nft.write(translation.text+"\n")
            except:
                pass

print("=============================== POSITIVE =====================================")
with open('positive_filtered_translations.txt', 'w') as pft:
    with open('positive_filtered.txt', 'r') as f:
        for word in f.readlines():
            try:
                translation = translator.translate(word.rstrip(), dest='mk')
                if translation is not None:
                    print (word)
                    print (translation.text)
                    pft.write(translation.text+"\n")
            except:
                pass

