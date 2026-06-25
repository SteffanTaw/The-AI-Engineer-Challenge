from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS so the frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

CLAUDE_URL = "https://lgts1tetamapi01.azure-api.net/claude/anthropic/v1/messages"

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/api/chat")
def chat(request: ChatRequest):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="ANTHROPIC_API_KEY not configured")

    try:
        response = httpx.post(
            CLAUDE_URL,
            params={"subscription-key": api_key},
            json={
                "model": "claude-sonnet-4-6",
                "max_tokens": 1024,
                "system": "You are an expert physics tutor. Answer physics questions clearly and accurately. Break down concepts step by step, use equations where relevant (formatted clearly), and give intuitive explanations suitable for a student. If a question is not about physics, politely redirect the user back to physics topics.",
                "messages": [{"role": "user", "content": request.message}],
            },
            timeout=30.0,
        )
        response.raise_for_status()
        return {"reply": response.json()["content"][0]["text"]}
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"Anthropic API error: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calling Anthropic API: {str(e)}")
