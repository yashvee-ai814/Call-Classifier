# Call Classifier — Backend

A FastAPI service that classifies phone call transcripts by sending them to a locally-running LLM via [Ollama](https://ollama.com).

For the full project overview, architecture diagram, and API reference see the [root README](../README.md).

---

## How it works

1. A client sends `POST /classify/` with a raw call transcript.
2. The backend builds a structured prompt and forwards it to the Ollama HTTP API.
3. Ollama runs the LLM locally and returns a generated JSON response.
4. The backend parses the response and returns a `reason` and `category` to the caller.

---

## Prerequisites

| Tool | Purpose | Install |
|------|---------|---------|
| Python ≥ 3.11 | Runtime | [python.org](https://www.python.org/downloads/) |
| [uv](https://github.com/astral-sh/uv) | Package manager | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| [Ollama](https://ollama.com) | Run LLMs locally | [ollama.com/download](https://ollama.com/download) |

Pull the default model after installing Ollama:

```bash
ollama pull gpt-oss:120b-cloud
```

---

## Running locally

```bash
# 1. Install dependencies
cd call-classifier-backend
uv sync

# 2. Start Ollama in a separate terminal
ollama serve

# 3. Start the API server with hot-reload
uv run uvicorn main:app --reload
```

The API is live at **http://localhost:8000**.
Interactive docs: **http://localhost:8000/docs**

---

## Running with Docker

```bash
# Build the image
docker build -t call-classifier-backend .

# Run — point OLLAMA_API_URL to Ollama on the host machine
docker run -p 8000:8000 \
  -e OLLAMA_API_URL=http://host.docker.internal:11434/api/generate \
  call-classifier-backend
```

---

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_API_URL` | `http://localhost:11434/api/generate` | Full URL of the Ollama generate endpoint |
| `OLLAMA_MODEL` | `gpt-oss:120b-cloud` | Model tag to use for inference |

Set these in `.env` or pass them at runtime (see examples above).

---

## Project structure

```
call-classifier-backend/
├── main.py          # FastAPI app — creates app, registers middleware and routers
├── middleware.py    # CORS middleware configuration
├── models.py        # Pydantic request/response models
├── routers/
│   ├── __init__.py  # Makes routers/ a Python package
│   └── llm.py       # POST /classify/ endpoint + Ollama integration
├── test/
│   └── test_transcript.md  # Sample transcript for manual testing
├── pyproject.toml   # Project metadata and dependencies (managed by uv)
└── Dockerfile       # Multi-stage Docker build
```
