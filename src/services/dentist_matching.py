import numpy as np
from typing import List
from src.utils.similarity_utils import calculate_cosine_similarity
from typing import Dict
from scipy.sparse import spmatrix
from src.utils.tfidf_utils import tfidf_utils


async def dentist_matcher(
    dental_preferences: List[str], tfidf_instance: tfidf_utils
) -> Dict[str, spmatrix]:

    # Extracting our vectorized dentist data and ids from the global instance
    dentist_vectors = tfidf_instance.corpus_vectors
    dentist_ids = tfidf_instance.corpus_ids

    # Converting users dental prefrences to a numpy array and then vectorizing it
    dental_preferences = [" ".join(dental_preferences)]
    dental_prefs_vector = tfidf_instance.transform_document(dental_preferences)

    # Calculating cosine similarities which returns a 2d array of size (1, len(dentist_vectors))
    similarities = calculate_cosine_similarity(dental_prefs_vector, dentist_vectors)

    # Combine dentist IDs with their similarity scores
    results = zip(dentist_ids, similarities[0])

    return {dentist_id: similarity_score for dentist_id, similarity_score in results}
