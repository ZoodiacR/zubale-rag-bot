#!/bin/bash
echo "=== Zubale RAG Bot Demo ==="

HOST=http://localhost:8000

echo "1️⃣  Health check"
curl -s -o /dev/null -w "%{http_code}\n" "$HOST" || { echo "Service not ready"; exit 1; }

echo "2️⃣  POST /query – coffee"
curl -s -X POST "$HOST/query" \
  -H "Content-Type: application/json" \
  -d '{"user_id":"demo","query":"Do you sell coffee?"}' | jq .

echo "3️⃣  POST /query – gluten-free chocolate"
curl -s -X POST "$HOST/query" \
  -H "Content-Type: application/json" \
  -d '{"user_id":"demo","query":"Do you have gluten-free chocolate?"}' | jq .