from fileProcess import FileReader, FileWriter
import settings
from pyvi import ViTokenizer

class NLP(object):
    """ Class Natural Language Processing

    Args:
        text (str): initial text, default None
    """
    def __init__(self, text = None):
        self.text = text
        self.__set_stopwords()
        self.__set_synonym()
        
    def set_text(self, text):
        self.text = text
        self.words = []

    def __set_stopwords(self):
        self.stopwords = FileReader(settings.STOP_WORDS).load_stopwords()
    
    def __set_synonym(self):
        self.synonym = FileReader(settings.SYNONYM_PATH).load_synonym()        

    def __segmentation(self):
        """ word segmentation using Pyvi """
        self.text = ViTokenizer.tokenize(self.text)

    def __split_words(self):
        """ split word using word segmentation and 
            remove special character
        """
        try:
            self.words =  [w.strip(settings.SPECIAL_CHARACTER).lower() for w in self.text.split()]
        except TypeError:
            self.words = []

    def __replace_synonym(self):
        """ replace synonyms to original word """
        words = []
        for word in self.words:
            if word in self.synonym:
                words.append(self.synonym[word])
            else:
                words.append(word)
        self.words = words

    def __remove_stopwords(self):
        """ remove stopwords
        """
        self.words = [word for word in self.words if word not in self.stopwords and word != '']

    def preprocess(self):

        self.__segmentation()
        self.__split_words()
        self.__replace_synonym()
        self.__remove_stopwords()

        return self.words

class Dictionary(object):

    """ Class building dictionary from corpus """
    def __init__(self, corpus):
        self.corpus = corpus

    def build_dictionary(self):
        print('Building dictionary')
        dictionary = set()
        
        for document in self.corpus:
            for word in document:
                dictionary.add(word)
        
        # save dictionary to disk
        FileWriter(settings.DICTIONARY_PATH).save_data(sorted(list(dictionary)))