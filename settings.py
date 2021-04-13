import os
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(DIR_PATH, 'data/data')
STOP_WORDS = 'vietnamese-stopwords.txt'
DICTIONARY_PATH = 'dictionary.pickle'
TFIDF_PATH = 'tfidf.pickle'
IDF_PATH = 'idf.pkl'
SPECIAL_CHARACTER = '0123456789%@$.,=+-!;/()*"&^:#|?\"\n\t\'\xa0”“‘’…–'

