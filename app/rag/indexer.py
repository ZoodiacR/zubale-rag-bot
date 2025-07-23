import json
from typing import List
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_products(path: str = "data/products.jsonl") -> List[Document]:
    docs = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            content = f"{data['name']}: {data['description']}"
            docs.append(Document(page_content=content, metadata={"id": data["id"]}))
    return docs

def build_vector_store(docs: list) -> FAISS:
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_documents(docs, embeddings)