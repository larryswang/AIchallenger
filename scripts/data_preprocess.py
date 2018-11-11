#!/user/bin/env python
# -*- coding:utf-8 -*-
from data_process import load_data_from_csv, seg_words
from sklearn.feature_extraction.text import TfidfVectorizer
import config
import numpy as np
import pickle

if __name__ == '__main__':

    # load train data
    train_data_df = load_data_from_csv(config.train_data_path)
    validate_data_df = load_data_from_csv(config.validate_data_path)

    content_train = train_data_df.iloc[:, 1]

    print("start seg train data")
    content_train = seg_words(content_train)
    print("complete seg train data")

    print("start train feature extraction")
    vectorizer_tfidf = TfidfVectorizer(analyzer='word', ngram_range=(1, 5), min_df=5, norm='l2')
    vectorizer_tfidf.fit(content_train)
    print("complete train feature extraction models")
    print("vocab shape: ")
    print(vectorizer_tfidf.vocabulary_.keys())

    pickle.dump(vectorizer_tfidf, open("../model/vectorizer_tfidf.pkl", 'w'))