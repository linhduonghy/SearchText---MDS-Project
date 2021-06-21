# -*- coding: utf-8 -*-
import os
from preprocess_data import NLP, Dictionary
from extract_feature import TFIDF
from similarity import Similarity
from process_corpus import Corpus
from process_query import compute_tf_idf_query

# load corpus
corpusObj = Corpus()

# load file
files = corpusObj.load_files()

# # ***
# corpus = corpusObj.load_corpus()
# corpusObj.build_dictionary(corpus)

# load dictionary
dictionary = corpusObj.load_dictionary()

# # ***
# # init TFIDF with corpus, dictionary
# # compute idf, tf_idf then save to file 
# tfidf = TFIDF(corpus, dictionary)

# load idf, tf_idf
idf, tf_idf = corpusObj.load_idf_tfidf()

# Query text
query_path = 'data\\query_input.txt'
tf_idf_query = compute_tf_idf_query(query_path, dictionary, idf)

# calculate similarity between tf_idf_query with tf_idf of corpus
similarity = Similarity()
# similarities = similarity.cosine_similarity_sprase_matrix(tf_idf, tf_idf_query).flatten()
similarities = []
for tf_idf_e in tf_idf:
    similarities.append(similarity.cosine_similarity(tf_idf_e.toarray()[0], tf_idf_query.toarray()[0]))

# display similarity descending between query input with corpus
# sort similarity
similarities, files = zip(*sorted(zip(similarities, files), reverse=True))
print('\n10 file có độ tương đồng giảm dần:\n')
sim_re, files_res = similarities[:10], files[:10]

for i in range(len(files_res)):
    print('%s %f' % (files_res[i], sim_re[i]))
