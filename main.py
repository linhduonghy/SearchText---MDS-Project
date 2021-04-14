# -*- coding: utf-8 -*-
import os
import settings
from preprocessData import NLP, Dictionary
from fileProcess import FileReader, FileWriter
from extract_feature import TFIDF
from similarity import Similarity

# load corpus
corpus = []
files = [] # list filename of documents
for filename in os.listdir(settings.DATA_PATH):
    files.append(filename)
    text = FileReader(os.path.join(settings.DATA_PATH, filename)).read()
    corpus.append(NLP(text).remove_stopwords())

# # build dictionary from corpus
# Dictionary(corpus).build_dictionary()

# # init class compute tfidf of whole document
# tfidf = TFIDF(corpus)
# tf_idf = tfidf.compute_tf_idf()

# # save tfidf value of who document to disk
# FileWriter(settings.TFIDF_PATH).save_data(tf_idf)

# load tf_idf collection
tf_idf = FileReader(settings.TFIDF_PATH).load_data()
# print(tf_idf)

# query input as document
query_path = 'data\\query_input.txt'
text = FileReader(query_path).read()

# init tfidf 
tfidf = TFIDF()
# compute query tf_idf
query_tf_idf = tfidf.compute_query_tf_idf(NLP(text).remove_stopwords())


# calculate similarity between query_tf_idf with tf_idf collection
similarity = Similarity().similarity(tf_idf, query_tf_idf).flatten()

# sort similarity
similarity, files = zip(*sorted(zip(similarity, files)))

print('\nSimilarity descending:')
for i in range(len(files)-1, -1, -1):
    print('%s\t%f' % (files[i], similarity[i]))
