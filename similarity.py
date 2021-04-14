# from numpy import dot
# from numpy.linalg import norm
from sklearn.metrics.pairwise import cosine_similarity

class Similarity(object):
    """ Class calculate measure similarity between query vector and whole vector document """

    def similarity(self, tf_idf, query_tf_idf):
        """ calculate similarity using cosine similarity(sklearn)

        Args:
            tf_idf (sparse_matrix): tf-idf value of query input
            query_tf_idf (sparse_matrix): tf-idf value of corpos

        Returns:
            list: cosine similarity with list vector whole document
        """
        return cosine_similarity(tf_idf, query_tf_idf)

    # def cosine_similarity(self, vector_x, vector_y):
    #     return dot(vector_x, vector_y) / (norm(vector_x) * norm(vector_y))

    # def euclidean_distance(self, vector_x, vector_y):
    #     return norm(vector_x - vector_y)