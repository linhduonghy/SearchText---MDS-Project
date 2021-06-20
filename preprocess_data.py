import settings
from fileProcess import FileReader, FileWriter
from pyvi import ViTokenizer
from string import punctuation

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

    def __remove_punctuation_and_number(self):
        """ remove punctuation and number character in text
        """
        self.text = self.text.translate({ord(c): " " for c in settings.PUNCTUATION_NUMBER_CHARACTER})

    def __segment_words(self):
        """ word segmentation using Pyvi """
        self.text = ViTokenizer.tokenize(self.text)
        self.words = self.text.split()

    def __remove_stopwords(self):
        """ remove stopwords
        """
        self.words = [word for word in self.words if word not in self.stopwords and word != '']

    def __replace_synonym(self):
        """ replace synonyms to original word """
        words = []
        for word in self.words:
            if word in self.synonym:
                words.append(self.synonym[word])
            else:
                words.append(word)
        self.words = words

    def preprocess(self):
        self.__remove_punctuation_and_number()
        self.__segment_words()
        self.__remove_stopwords()
        self.__replace_synonym()        
        return self.words

class Dictionary(object):

    """ Class building dictionary from corpus """
    def __init__(self, corpus):
        self.corpus = corpus

    def build_save_dictionary(self):
        print('Building dictionary')
        dictionary = set() # unique list
        
        for document in self.corpus:
            for word in document:
                dictionary.add(word)
        
        # save dictionary to file
        FileWriter(settings.DICTIONARY_PATH).save_data(sorted(list(dictionary)))