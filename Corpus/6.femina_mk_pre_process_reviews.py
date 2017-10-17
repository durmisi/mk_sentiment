#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8
from __future__ import division
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json
import re
from cyrillic_converter import  isTextLatin

with open('femina_mk.json') as file:
    femina_mk_json = json.load(file)

threads_with_comments = []
total_movies = len(femina_mk_json)
for i in range(0, total_movies):

    movie = femina_mk_json[i]
    movie_title = movie[0][0]
    movie_reviews = movie[1][0]

    movie_reviews_filtered = []
    print '========================================================================'
    print movie_title
    print '========================================================================'

    for j in range(0, len(movie_reviews)):
        movie_review = movie_reviews[j][1]
        if len(movie_review) > 0:

            movie_review = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', movie_review)
            movie_review = re.sub(r'https?:\/\/.*\.(?:png|jpg)', '', movie_review)
            movie_review = re.sub(r'.*\.(?:png|jpg)', '', movie_review)
            movie_review = movie_review.replace('Прикачени фајлови:','')
            movie_review = re.sub(ur'Големина на фајлот: (?:\d*\.)?\d+,?(?:\d*\.)?\d+ KB', '', movie_review)
            movie_review = re.sub(ur'Прегледи: (?:\d*\.)?\d+', '', movie_review)
            movie_review = movie_review.strip()

            print movie_review
            print str(j) + '.========================================================================'

            is_review_latin = isTextLatin(movie_review)
            movie_reviews_filtered.append([movie_review, is_review_latin])

    print '========================================================================'
    threads_with_comments.append([movie_title, movie_reviews_filtered])

# write to file
import io, json
with io.open('femina_mk_filtered.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(threads_with_comments, ensure_ascii=False))