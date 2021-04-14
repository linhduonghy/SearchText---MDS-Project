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

nlp = NLP()

for filename in os.listdir(settings.DATA_PATH):
    files.append(filename)
    text = FileReader(os.path.join(settings.DATA_PATH, filename)).read()
    nlp.set_text(text)
    corpus.append(nlp.preprocess())

# build dictionary from corpus
# Dictionary(corpus).build_dictionary()

# load dictionary
dictionary = FileReader(settings.DICTIONARY_PATH).load_data()

# # init TFIDF with corpus input
# tfidf = TFIDF(corpus)

# # save idf value to disk
# tfidf.save_idf()

# load idf
idf = FileReader(settings.IDF_PATH).load_data()

# # compute tf-idf value of whole document 
# tf_idf = tfidf.compute_tf_idf()

# # save tf-idf value of who document to disk
# FileWriter(settings.TFIDF_PATH).save_data(tf_idf)

# load tf_idf of whole document
tf_idf = FileReader(settings.TFIDF_PATH).load_data()
# print(tf_idf)

# query input as document
query_path = 'data\\query_input.txt'
text = FileReader(query_path).read()

# init TFIDF with dictionary and idf value
tfidf = TFIDF(dictionary=dictionary, idf=idf)
# compute query tf_idf
query_tf_idf = tfidf.compute_query_tf_idf(NLP(text).preprocess())

# calculate similarity between query_tf_idf with tf_idf collection
similarity = Similarity().similarity(tf_idf, query_tf_idf).flatten()

# sort similarity
similarity, files = zip(*sorted(zip(similarity, files)))

print('\nSimilarity descending:')
for i in range(len(files)-1, -1, -1):
    print('%s\t%f' % (files[i], similarity[i]))
