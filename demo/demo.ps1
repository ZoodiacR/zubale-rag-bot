#Requires -Version 5.1
$hostUri = "http://localhost:8000"

Write-Host "=== Zubale RAG Bot Demo ===" -ForegroundColor Green

# Health check
try { Invoke-RestMethod "$hostUri" -TimeoutSec 5 | Out-Null }
catch { Write-Host "Service not ready"; exit 1 }

# Query 1 – coffee
$body = @{ user_id = "demo"; query = "Do you sell coffee?" } | ConvertTo-Json
$response1 = Invoke-RestMethod "$hostUri/query" -Method Post -Body $body -ContentType "application/json"
$response1 | ConvertTo-Json -Depth 3

# Query 2 – gluten-free chocolate
$body = @{ user_id = "demo"; query = "Do you have gluten-free chocolate?" } | ConvertTo-Json
$response2 = Invoke-RestMethod "$hostUri/query" -Method Post -Body $body -ContentType "application/json"
$response2 | ConvertTo-Json -Depth 3