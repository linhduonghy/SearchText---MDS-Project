# -*- coding: utf-8 -*-
import pickle

class FileReader(object):
    
    """ Class load data from disk: stopwords, dictionary, tf-idf """

    def __init__(self, filePath):
        self.filePath = filePath

    def read(self):
        """ read text document , format encoding utf-16-le

        Returns:
            str: whole text in document
        """
        # print(self.filePath)
        with open(self.filePath, encoding='utf-8') as f:
            s = f.read()
        return s

    def load_stopwords(self):
        with open(self.filePath, encoding='utf-8') as f:
            stopwords = set([w.strip().replace(' ', '_')
                             for w in f.readlines()])
        return stopwords

    def load_synonym(self):
        """ load synonym word

        Returns:
            dict: value is a synonym of key 
        """
        synonym = {}
        with open(self.filePath, encoding='utf8') as f:
            for line in f.readlines():
                if len(line.strip().split()) == 2:
                    x, y = line.strip().split()                
                synonym[y] = x
        return synonym

    def load_data(self):
        with open(self.filePath, 'rb') as f:
            return pickle.load(f)

class FileWriter(object):
    """ Class save data to disk """
    def __init__(self, path):
        self.path = path

    # def save_dictionary(self, data):
    #     with open(self.path, 'wb') as f:
    #         # for word in data:
    #         #     f.write('%s\n' % word)
    #         pickle.dump(data, f)

    # def save_tf_idf(self, tf_idf):
    #     with open(self.path, 'wb') as f:
    #         pickle.dump(tf_idf, f)

    def save_data(self, data):
        with open(self.path, 'wb') as f:
            pickle.dump(data, f)