from sklearn.metrics.pairwise import cosine_similarity
class Similarity(object):
    """ Class calculate measure similarity between query vector and whole vector document """

    @staticmethod
    def dot(v1, v2):
        return sum(a * b for a, b in zip(v1, v2))

    def cosine_similarity(self, v1, v2):
        "cosine similarity of v1 to v2: (v1.v2)/{||v1||*||v2||)"
        return self.dot(v1, v2) / (self.dot(v1, v1)**.5 * self.dot(v2,v2)**.5)

    def cosine_similarity_sprase_matrix(self, tf_idf, query_tf_idf):
        """ calculate similarity using cosine similarity(sklearn)

        Args:
            tf_idf (sparse_matrix): tf-idf value of query input
            query_tf_idf (sparse_matrix): tf-idf value of corpos

        Returns:
            list: cosine similarity with list vector whole document
        """
        return cosine_similarity(tf_idf, query_tf_idf)