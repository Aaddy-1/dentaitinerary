from fastapi import Request
from src.utils.tfidf_utils import tfidf_utils


def get_dentist_tfidf(request: Request) -> tfidf_utils:
    """Dependency that provides the TF-IDF utility class instance."""
    return request.app.state.tfidf_dentist
