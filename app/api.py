from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from app.rag.indexer import load_products, build_vector_store
from app.rag.retriever import ProductRetriever
from app.agents.retriever_agent import RetrieverAgent, RetrieverState
from app.agents.responder_agent import ResponderAgent, ResponderState
from app.config import settings

app = FastAPI()

docs = load_products()
vector_store = build_vector_store(docs)
retriever = ProductRetriever(vector_store, top_k=settings.TOP_K)

workflow = StateGraph(dict)
retriever_agent = RetrieverAgent(retriever)
responder_agent = ResponderAgent(ChatOpenAI(model="gpt-3.5-turbo", temperature=0))
workflow.add_node("retrieve", retriever_agent)
workflow.add_node("respond", responder_agent)
workflow.add_edge("retrieve", "respond")
workflow.set_entry_point("retrieve")
chain = workflow.compile()

class QueryRequest(BaseModel):
    user_id: str
    query: str

@app.post("/query")
def query_endpoint(request: QueryRequest):
    result = chain.invoke({"query": request.query})
    return {"user_id": request.user_id, "answer": result["answer"]}