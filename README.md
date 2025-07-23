# Zubale RAG Bot – README

## 📌 Overview
Micro-service that receives user questions about products (simulated WhatsApp messages) via a REST endpoint, performs **Retrieval-Augmented Generation (RAG)** on a small product catalog, and answers through a LangGraph **multi-agent pipeline** (Retriever + Responder).

---

## ⚙️ Quick Start (local)

1. **Prerequisites**
   - Python 3.11
   - Docker & Docker Compose
   - OpenAI API key (for GPT-3.5)

2. **Clone / unzip** the project
   ```bash
   cd zubale-rag-bot

3. **Environment variables (optional)**
   ```bash
   export OPENAI_API_KEY="sk-xxxxxxxxxxxxxx"
   export TOP_K=3            # default

4. **Build & run**
   ```bash
   docker-compose up --build
   Service is live at http://localhost:8000.

5. **🚀 Indexing & Retrieval Flow**
   ```bash
    Data file:
    data/products.jsonl already contains 3 sample products.
    Indexing happens automatically on startup
    indexer.py → loads JSONL → HuggingFaceEmbeddings → FAISS in-memory vector store.
    Retrieval
    ProductRetriever uses cosine similarity to return the top-k documents.
    Generation
    ResponderAgent sends the retrieved docs + user query to GPT-3.5 with a strict prompt.*
6. **📡 Testing the Flow**
Manual cURL
   ```bash
    curl -X POST http://localhost:8000/query \
    -H "Content-Type: application/json" \
    -d '{"user_id":"u123","query":"Do you sell coffee?"}'
    Expected:
    JSON
     {"user_id":"u123","answer":"Yes, we have Organic Coffee Beans 100 % arabica, medium roast, 250 g bag."}

7. **Unit tests**
     ```bash
         pytest tests/
         Output:
         tests/test_retriever.py::test_retriever PASSED
        1 passed in 1.21 s

8. **🧪 Local Dev (no Docker)**
      ```bash
       python -m venv venv
       source venv/bin/activate   # Windows: .\venv\Scripts\activate
       pip install -r requirements.txt
       uvicorn app.api:app --reload --port 8000
9. **📁 Project Tree**
      ````bash
        zubale-rag-bot/
      ├── app/
      │   ├── api.py
      │   ├── config.py
      │   ├── agents/
      │   │   ├── retriever_agent.py
      │   │   └── responder_agent.py
      │   └── rag/
      │       ├── indexer.py
      │       └── retriever.py
      ├── data/products.jsonl
      ├── tests/test_retriever.py
      ├── Dockerfile
      ├── docker-compose.yml
      ├── requirements.txt
      └── README.md
11. **📞 Support**
Open an issue or reach out at andyleon000820@gmail.com

