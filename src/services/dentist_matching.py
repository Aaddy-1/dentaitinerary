from typing import List
from fastapi import Request
from src.utils.similarity_utils import calculate_cosine_similarity
from main import app


async def dentist_matcher(dental_preferences: List[str]):
    tfidf_instance = app.state.tfidf_dentist
    dentist_vectors = tfidf_instance.corpus_vectors
    dentist_ids = tfidf_instance.corpus_ids
    dental_prefs_vector = [
        tfidf_instance.transform_document(i) for i in dental_preferences
    ]

    cosine_similarity = calculate_cosine_similarity(
        dentist_vectors, dental_prefs_vector
    )
    return cosine_similarity
