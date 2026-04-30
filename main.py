from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup

app = FastAPI(title="Sovereign Agentic API")

@app.get("/")
def home():
    return {
        "message": "Sovereign AI Infrastructure is LIVE", 
        "author": "Md. Tarequddin Shikder",
        "org": "Pinnacle AI Research Center"
    }

@app.get("/search")
async def search(url: str, token: str = None):
    if token != "pinnacle-secure-2026":
        raise HTTPException(status_code=403, detail="Unauthorized Access")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        for tag in soup(["script", "style"]):
            tag.decompose()
        clean_text = " ".join(soup.get_text().split())[:1000]
        return {"source": url, "data": clean_text}
    except Exception as e:
        return {"error": str(e)}
