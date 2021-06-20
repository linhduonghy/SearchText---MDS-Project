from fileProcess import FileReader
from extract_feature import TFIDF
from preprocess_data import NLP

# compute tf-idf of query text
def compute_tf_idf_query(query_path, dictionary, idf):

    query_text = FileReader(query_path).read()
    # init TFIDF with dictionary and idf value
    tfidf = TFIDF(dictionary=dictionary, idf=idf)
    # compute query tf_idf
    tf_idf_query = tfidf.compute_query_tf_idf(NLP(query_text).preprocess())

    return tf_idf_query