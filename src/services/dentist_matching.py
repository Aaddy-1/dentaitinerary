from typing import List
from fastapi import Request, Depends
from src.utils.similarity_utils import calculate_cosine_similarity
from src.dependencies import get_dentist_tfidf
from collections import defaultdict
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

    results_dict = {}

    for i in range(len(dentist_ids)):
        current_dentist_vector = dentist_vectors[i]
        cosine_similarity = calculate_cosine_similarity(
            dental_prefs_vector, current_dentist_vector
        )
        results_dict[dentist_ids[i]] = cosine_similarity

    return results_dict
