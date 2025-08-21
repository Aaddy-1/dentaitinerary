from scipy.sparse import spmatrix
from sklearn.metrics.pairwise import cosine_similarity


def calculate_cosine_similarity(vec1: spmatrix, vec2: spmatrix) -> spmatrix:
    return cosine_similarity(vec1, vec2)
