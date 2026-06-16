# utils/tfidf_utils.py

from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix


class tfidf_utils:

    def __init__(self):
        self.name = None
        self.corpus = []
        self.vectorizer = None
        self.corpus_vectors = None
        self.corpus_ids = []

    def fit_vectorizer(self, corpus: List[str], corpus_ids: List[str]) -> csr_matrix:
        if not corpus:
            raise ValueError(
                "Corpus is empty. Cannot fit vectorizer on an empty corpus."
            )
        self.vectorizer = TfidfVectorizer()
        self.corpus_vectors = self.vectorizer.fit_transform(corpus)
        self.corpus_ids = corpus_ids

        print(f"Vectorizer fitted with a corpus of {len(self.corpus_ids)} documents.")
        return self.corpus_vectors

    def transform_document(self, document: List[str]) -> csr_matrix:
        if not self.vectorizer:
            raise ValueError("Vectorizer is not fitted. Run fit_vectorizer first.")

        return self.vectorizer.transform(document)
