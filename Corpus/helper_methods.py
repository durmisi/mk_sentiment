#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def getNegativeFilteredTranslations():
    words = []
    with open('negative_filtered_translations.txt', 'r') as f:
        for word in f.readlines():
            words.append(word)
    return words

def getPositiveFilteredTranslations():
    words = []
    with open('positive_filtered_translations.txt', 'r') as f:
        for word in f.readlines():
            words.append(word)
    return words