import os
import settings
from preprocess_data import NLP, Dictionary
from fileProcess import FileReader, FileWriter


class Corpus:

    def __init__(self):
        self.data_path = settings.DATA_PATH


    def load_files(self):
        files = [] # list filename of documents
        lens = []
        for filename in os.listdir(self.data_path):
            files.append(filename)
            with (open(os.path.join(self.data_path, filename), 'r', encoding='utf-8')) as f:
                lens.append(len(f.read().split()))
        # print(lens)
        return files


    def load_corpus(self):
        corpus = []
        nlp = NLP()
        for filename in os.listdir(self.data_path):
            text = FileReader(os.path.join(self.data_path, filename)).read()
            nlp.set_text(text)
            corpus.append(nlp.preprocess())
        return corpus

    def build_dictionary(self, corpus):

        # build dictionary from corpus
        Dictionary(corpus).build_save_dictionary()

    def load_dictionary(self):

        return FileReader(settings.DICTIONARY_PATH).load_dict_data()

    def load_idf_tfidf(self):

        # load idf
        idf = FileReader(settings.IDF_PATH).load_data()
        # load tf_idf of whole document
        tf_idf = FileReader(settings.TFIDF_PATH).load_data()
        
        return idf, tf_idf
