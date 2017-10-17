#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8
from __future__ import division
import sys
reload(sys)
sys.setdefaultencoding('utf8')

replacements = []
replacements.append(['Gj', u'Ѓ'])
replacements.append(['Dz', u'Ѕ'])
replacements.append(['J', u'Ј'])
replacements.append(['Lj', u'Љ'])
replacements.append(['Nj', u'Њ'])
replacements.append(['Kj', u'Ќ'])
replacements.append(['Dzh', u'Џ'])
replacements.append(['A', u'А'])
replacements.append(['B', u'Б'])
replacements.append(['V', u'В'])
replacements.append(['G', u'Г'])
replacements.append(['D', u'Д'])
replacements.append(['E', u'Е'])
replacements.append(['Zh', u'Ж'])
replacements.append(['Z', u'З'])
replacements.append(['I', u'И'])
replacements.append(['K', u'К'])
replacements.append(['L', u'Л'])
replacements.append(['M', u'М'])
replacements.append(['N', u'Н'])
replacements.append(['O', u'О'])
replacements.append(['P', u'П'])
replacements.append(['R', u'Р'])
replacements.append(['S', u'С'])
replacements.append(['T', u'Т'])
replacements.append(['U', u'У'])
replacements.append(['F', u'Ф'])
replacements.append(['H', u'Х'])
replacements.append(['C', u'Ц'])
replacements.append(['Ch', u'Ч'])
replacements.append(['Sh', u'Ш'])
replacements.append(['a', u'а'])
replacements.append(['b', u'б'])
replacements.append(['v', u'в'])
replacements.append(['g', u'г'])
replacements.append(['d', u'д'])
replacements.append(['e', u'е'])
replacements.append(['zh', u'ж'])
replacements.append(['z', u'з'])
replacements.append(['i', u'и'])
replacements.append(['k', u'к'])
replacements.append(['l', u'л'])
replacements.append(['m', u'м'])
replacements.append(['n', u'н'])
replacements.append(['o', u'о'])
replacements.append(['p', u'п'])
replacements.append(['r', u'р'])
replacements.append(['s', u'с'])
replacements.append(['t', u'т'])
replacements.append(['u', u'у'])
replacements.append(['f', u'ф'])
replacements.append(['f', u'х'])
replacements.append(['h', u'ц'])
replacements.append(['c', u'ч'])
replacements.append(['ch', u'ш'])
replacements.append(['sh', u'ѓ'])
replacements.append(['gj', u'ѕ'])
replacements.append(['dz', u'ј'])
replacements.append(['j', u'ј'])
replacements.append(['lj', u'љ'])
replacements.append(['nj', u'њ'])
replacements.append(['kj', u'ќ'])
replacements.append(['dzh', u'Џ'])

def convert_to_cyrillic(text):
    replacements_ordered = sorted(replacements, key=lambda x: len(x[0]) , reverse=True)
    for ro in replacements_ordered:
        text = text.replace(ro[0], ro[1])
    return text;

from nltk import word_tokenize
import string

def isTextLatin(text):

    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper_mk= "АБВГДЃЕЖЗЅИЈКЛЉМНЊОПРСТЧУФХЦЌЏШ"
    lower_mk = "абвгдѓежзѕијклљмнњопрстчуфхцќџш"

    # strip punctuation
    text = ''.join(ch for ch in text if ch not in set(string.punctuation))

    if not isinstance(text, unicode):
        text = unicode(text, 'utf-8')

    words = word_tokenize(text)

    totalWords = len(words)

    if totalWords ==0:
        return False

    totalLatinWords = 0

    for word in words:
        totalLatinChars = 0
        totalCyrChars = 0
        for ch in word:
            if (upper_mk.find(ch) != -1 or lower_mk.find(ch) != -1):
                totalCyrChars +=1
                pass
            if (upper.find(ch) != -1 or lower.find(ch) != -1):
                totalLatinChars += 1

        word_length = len(word)-(totalCyrChars/2)
        # print word, word_length

        if ((totalLatinChars / word_length)  > 0.75):
            totalLatinWords +=1

    # print (totalLatinWords/totalWords)
    # IF 50% of the words are latin the  the Text is Latin
    return (totalLatinWords/totalWords) >= 0.5


print(convert_to_cyrillic('Nekoj latinicen zbor ovde !!!'))
print isTextLatin('Nekoj кирилилчен zbor ovde !!!')

# https://stackoverflow.com/questions/38722464/check-if-string-latin-or-cyrillic