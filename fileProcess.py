# -*- coding: utf-8 -*-
 
import pickle

class FileReader(object):

    def __init__(self, filePath):
        self.filePath = filePath

    def read(self):
        with open(self.filePath, encoding='utf-16-le') as f:
            s = f.read()
        return s

    def load_stopwords(self):
        with open(self.filePath, encoding='utf-8') as f:
            stopwords = set([w.strip().replace(' ', '_')
                             for w in f.readlines()])
        return stopwords

    def load_dictionary(self):
        with open(self.filePath, 'rb') as f:
            # return [word for word in f.readlines()]
            return pickle.load(f)
    
    def load_tf_idf(self):
        with open(self.filePath, 'rb') as f:
            return pickle.load(f)

    def load_data(self):
        with open(self.filePath, 'rb') as f:
            return pickle.load(f)

class FileWriter(object):

    def __init__(self, path):
        self.path = path

    def save_dictionary(self, data):
        with open(self.path, 'wb') as f:
            # for word in data:
            #     f.write('%s\n' % word)
            pickle.dump(data, f)

    def save_tf_idf(self, tf_idf):
        with open(self.path, 'wb') as f:
            pickle.dump(tf_idf, f)

    def save_data(self, data):
        with open(self.path, 'wb') as f:
            pickle.dump(data, f)