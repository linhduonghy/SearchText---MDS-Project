from fileProcess import FileReader, FileWriter
import settings
from pyvi import ViTokenizer

class NLP(object):

    def __init__(self, text = None):
        self.text = text
        self.__set_stopwords()


    def __set_stopwords(self):
        self.stopwords = FileReader(settings.STOP_WORDS).load_stopwords()
    

    def segmentation(self):
        return ViTokenizer.tokenize(self.text)
    

    def split_words(self):
        text = self.segmentation()
        try:
            return [w.strip(settings.SPECIAL_CHARACTER).lower() for w in text.split()]
        except TypeError:
            return []

    def remove_stopwords(self):
        return [word for word in self.split_words() if word not in self.stopwords and word != '']
    # 270

class Dictionary(object):

    def __init__(self, corpus):
        self.corpus = corpus

    def build_dictionary(self):
        print('Building dictionary')
        dictionary = set()
        
        for document in self.corpus:
            for word in document:
                dictionary.add(word)

        FileWriter(settings.DICTIONARY_PATH).save_dictionary(sorted(list(dictionary)))