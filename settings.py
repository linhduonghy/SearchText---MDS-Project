import os
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(DIR_PATH, 'data/collection')
STOP_WORDS = 'vietnamese-stopwords.txt'
DICTIONARY_PATH = 'dictionary.pkl'
TFIDF_PATH = 'tfidf.pkl'
IDF_PATH = 'idf.pkl'
SPECIAL_CHARACTER = '0123456789%@$.,=+-!;/()*"&^:#|?\"\n\t\'\xa0”“‘’…–'

