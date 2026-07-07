import os
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from mcp.server.fastapi import FastApiServer
# Burada pubmedmcp'nin server nesnesini import ediyoruz
from pubmedmcp.server import server 

app = FastAPI()

# MCP protokolünü internete (SSE standardında) açan köprü
mcp_server = FastApiServer(server)

@app.get("/sse")
async def sse_endpoint():
    # Thesys platformunun bağlanacağı ana SSE çıkışı
    return mcp_server.handle_sse()

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
