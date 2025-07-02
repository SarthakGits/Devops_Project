from fastapi import FastAPI, Request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST, CollectorRegistry
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()

# Using a separate registry to avoid global duplication
registry = CollectorRegistry()
REQUEST_COUNTER = Counter(
    "api_requests_total", 
    "Total number of API requests", 
    registry=registry
)

@app.post("/api")
@app.get("/api")
@app.put("/api")
@app.delete("/api")
async def handle_request(request: Request):
    REQUEST_COUNTER.inc()

    headers = dict(request.headers)
    method = request.method
    body = await request.body()

    response = (
        "Welcome to our demo API, here are the details of your request:\n\n"
        "***Headers***:\n" +
        "\n".join(f"{k}: {v}" for k, v in headers.items()) +
        f"\n\n***Method***:\n{method}\n\n***Body***:\n{body.decode('utf-8')}"
    )

    return PlainTextResponse(response)

@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest(registry), media_type=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
