import settings
import math
from scipy.sparse import csr_matrix
import numpy as np
from fileProcess import FileReader, FileWriter
from collections import Counter
from sklearn import preprocessing

class TFIDF(object):
    """ Class compute tf-idf following https://en.wikipedia.org/wiki/Tf-idf

    """
    def __init__(self, corpus=None, dictionary=None, idf=None):
        self.corpus = corpus        
        self.dictionary = dictionary
        if idf == None:
            self.save_idf()
            # save tf idf 
            self.save_tf_idf()
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
            idf[word] = math.log(D / count)
        return idf

    def __compute_tf_idf(self):
        """ compute tf-idf of each document in whole document

        Returns:
            sparse_matrix: row: document, col: word in dictionary, value: tf-idf value
        """
        vocal = {j:i for i,j in enumerate(self.dictionary)}
        sparse_matrix= csr_matrix( (len(self.corpus), len(self.dictionary)), dtype=np.float64)
        
        for row in range(len(self.corpus)):
            number_of_words_in_document = Counter(self.corpus[row])
            for word in self.corpus[row]:
                tf_idf_value = (number_of_words_in_document[word] / float(len(self.corpus[row]))) * self.idf[word]
                sparse_matrix[row, vocal[word]] = tf_idf_value              

        return sparse_matrix

    def save_tf_idf(self):
        tfidf = self.__compute_tf_idf()
        FileWriter(settings.TFIDF_PATH).save_data(tfidf)
        
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

        return sparse_matrix