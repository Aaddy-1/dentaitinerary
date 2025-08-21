from typing import List
from src.utils.similarity_utils import calculate_cosine_similarity
from typing import Dict
from scipy.sparse import spmatrix
from src.utils.tfidf_utils import tfidf_utils


async def dentist_matcher(
    dental_preferences: List[str], tfidf_instance: tfidf_utils
) -> Dict[str, spmatrix]:
    dentist_vectors = tfidf_instance.corpus_vectors
    dentist_ids = tfidf_instance.corpus_ids
    dental_preferences = [" ".join(dental_preferences)]
    dental_prefs_vector = tfidf_instance.transform_document(dental_preferences)

    similarities = calculate_cosine_similarity(dental_prefs_vector, dentist_vectors)

    # Combine dentist IDs with their similarity scores and sort
    results = zip(dentist_ids, similarities[0])

    return {dentist_id: similarity_score for dentist_id, similarity_score in results}
