import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(DIR_PATH, 'data\\collections')
STOP_WORDS = os.path.join(DIR_PATH, 'vietnamese_ref\\vietnamese-stopwords.txt') #https://github.com/stopwords/vietnamese-stopwords/blob/master/vietnamese-stopwords.txt
SYNONYM_PATH = os.path.join(DIR_PATH, 'vietnamese_ref\\synonym_vietnamese.txt') #https://github.com/NLP-Projects/Word-Similarity
PUNCTUATION_NUMBER_CHARACTER = '0123456789%@$.,=+-!;/()*"&^:#|?\"\n\t\'\xa0”“‘’…–'

DICTIONARY_PATH = 'dictionary.txt'
TFIDF_PATH = 'tfidf.pkl'
IDF_PATH = 'idf.pkl'


