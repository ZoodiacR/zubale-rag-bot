from typing import List, TypedDict
from langchain.schema import Document
from app.rag.retriever import ProductRetriever

class RetrieverState(TypedDict):
    query: str
    documents: List[Document]

class RetrieverAgent:
    def __init__(self, retriever: ProductRetriever):
        self.retriever = retriever

    def __call__(self, state: RetrieverState) -> RetrieverState:
        docs = self.retriever.retrieve(state["query"])
        state["documents"] = docs
        return state