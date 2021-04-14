import math
from scipy.sparse import csr_matrix
import numpy as np
from fileProcess import FileReader, FileWriter
import settings
from collections import Counter
from sklearn import preprocessing

class TFIDF(object):
    """ Class compute tf-idf following https://en.wikipedia.org/wiki/Tf-idf

    """
    def __init__(self, corpus=None, dictionary=None, idf=None):
        self.corpus = corpus
        if dictionary == None: # load dictionary
            self.dictionary = FileReader(settings.DICTIONARY_PATH).load_data()
        else:
            self.dictionary = dictionary
        if idf == None: # load idf     
            self.idf = FileReader(settings.IDF_PATH).load_data()
        else:
            self.idf = idf


    def save_idf(self):
        """ save idf value to disk
        """
        self.idf = self.__set_idf()
        FileWriter(settings.IDF_PATH).save_data(self.idf)

    def __set_idf(self):
        """ compute idf each word of whole document

        Returns:
            dict: idf value every word in dictionary
        """
        idf = {}

        D = len(self.corpus)

        for word in self.dictionary:
            count = 0
            for document in self.corpus:
                if word in document:
                    count += 1
            idf[word] = 1 + math.log((D) / (count + 1))

        return idf

    def compute_tf_idf(self):
        """ compute tf-idf of each document in whole document

        Returns:
            sparse_matrix: row: document, col: word in dictinary, value: tf-idf value
        """
        vocal = {j:i for i,j in enumerate(self.dictionary)}
        sparse_matrix= csr_matrix( (len(self.corpus), len(self.dictionary)), dtype=np.float64)
        
        for row in range(len(self.corpus)):
            number_of_words_in_document = Counter(self.corpus[row])
            for word in self.corpus[row]:
                tf_idf_value = (number_of_words_in_document[word] / float(len(self.corpus[row]))) * self.idf[word]
                sparse_matrix[row, vocal[word]] = tf_idf_value        
                
        output = preprocessing.normalize(sparse_matrix, norm='l2', axis=1, copy=True, return_norm=False)

        return output

    def compute_query_tf_idf(self, document):
        """ compute tf-idf a document query

        Args:
            document (list): a document query input

        Returns:
            sparse_matrix: row:document query, col:word in dictionary, value: tf-idf value
        """
        vocal = {j:i for i,j in enumerate(self.dictionary)}
        sparse_matrix= csr_matrix( (1, len(self.dictionary)), dtype=np.float64)
        
        for row in range(1):
            number_of_words_in_document = Counter(document)
            for word in document:
                if word in self.dictionary:                                   
                    tf_idf_value = (number_of_words_in_document[word] / float(len(document))) * self.idf[word]
                    sparse_matrix[row, vocal[word]] = tf_idf_value                        
        output = preprocessing.normalize(sparse_matrix, norm='l2', axis=1, copy=True, return_norm=False)

        return output