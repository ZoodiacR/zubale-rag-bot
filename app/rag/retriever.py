from typing import List
from langchain.schema import Document
from langchain_community.vectorstores import FAISS

class ProductRetriever:
    def __init__(self, vector_store: FAISS, top_k: int = 3):
        self.vector_store = vector_store
        self.top_k = top_k

    def retrieve(self, query: str) -> List[Document]:
        return self.vector_store.similarity_search(query, k=self.top_k)