### Front End

A single-file chat interface (`index.html`) that talks to the FastAPI backend at `http://localhost:8000`.

#### How to run

**1. Start the backend first** (from the project root):
```bash
uv run uvicorn api.index:app --reload
```

**2. Open the frontend** — two options:

**Option A — open directly in browser (simplest):**
```
Just double-click frontend/index.html, or drag it into your browser.
```

**Option B — serve with Python (avoids any CORS quirks with file:// URLs):**
```bash
cd frontend
python -m http.server 3000
# then open http://localhost:3000
```

The chat UI sends `POST http://localhost:8000/api/chat` with `{"message": "..."}` and displays the `{"reply": "..."}` response.
