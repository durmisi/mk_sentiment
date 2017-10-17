#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8
from __future__ import division
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import io, json
from nltk import word_tokenize, sent_tokenize
from helper_methods import getNegativeFilteredTranslations
from helper_methods import getPositiveFilteredTranslations

positive_translations=getPositiveFilteredTranslations()
negative_translations=getNegativeFilteredTranslations()

def tokenize(movie_review):
    words = []
    for sent in sent_tokenize(movie_review):
        for word in word_tokenize(sent):
            words.append(word)
    return words

def calculateScore(movie_review):
    movie_review_words = tokenize(movie_review)

    total_positive_words_in_review = 0;
    for word in movie_review_words:
        for pt in positive_translations :
            if(pt.strip() == word.strip()):
                total_positive_words_in_review +=1

    positive_score = total_positive_words_in_review / len(positive_translations)

    total_negative_words_in_review = 0;
    for word in movie_review_words:
        for pt in negative_translations :
            if(pt.strip() == word.strip()):
                total_negative_words_in_review +=1

    negative_score = total_negative_words_in_review / len(negative_translations)

    return positive_score, negative_score

def calculate_femina_mk_reviews_score(femina_mk_json):

    result = []
    total_movies = len(femina_mk_json)
    for i in range(0, total_movies):

        movie = femina_mk_json[i]
        movie_title = movie[0]
        movie_reviews = movie[1]

        print '========================================================================'
        print movie_title
        print '========================================================================'

        movie_reviews_scored = []
        for j in range(0, len(movie_reviews)):
            movie_review= movie_reviews[j][0].strip()
            if len(movie_review) > 0:
                print movie_review
                print str(j)+'.------------------------------------------------------'
                movie_review_score = calculateScore(movie_review)
                print movie_review_score
                movie_reviews_scored.append([movie_review, movie_review_score[0], movie_review_score[1]])

        result.append([movie_title, movie_reviews_scored])

    return result

#1. Load reviews
with open('femina_mk_filtered.json') as file:
   femina_mk_json = json.load(file)

#2. score
moview_reviews_scored = calculate_femina_mk_reviews_score(femina_mk_json)

#3. update json
with io.open('femina_mk_scored.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(moview_reviews_scored, ensure_ascii=False))