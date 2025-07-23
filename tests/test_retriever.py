from app.rag.indexer import load_products, build_vector_store
from app.rag.retriever import ProductRetriever

def test_retriever():
    docs = load_products()
    vs = build_vector_store(docs)
    retriever = ProductRetriever(vs, top_k=2)
    results = retriever.retrieve("milk")
    assert len(results) == 2
    assert any("Almond Milk" in doc.page_content for doc in results)