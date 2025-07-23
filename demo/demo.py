#!/usr/bin/env python3
import requests
import json

HOST = "http://localhost:8000"
HEADERS = {"Content-Type": "application/json"}

queries = [
    {"user_id": "demo", "query": "Do you sell coffee?"},
    {"user_id": "demo", "query": "Do you have gluten-free chocolate?"},
    {"user_id": "demo", "query": "Is there any plant-based milk?"}
]

print("=== Zubale RAG Bot Demo ===")
for q in queries:
    resp = requests.post(f"{HOST}/query", headers=HEADERS, data=json.dumps(q))
    print(resp.status_code, resp.json())