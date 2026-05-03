# Call Classifier — Frontend

A React + Vite single-page application that lets users paste a call transcript and instantly see an AI-generated classification from the backend.

For the full project overview, architecture diagram, and API reference see the [root README](../README.md).

---

## How it works

1. The user pastes a call transcript into the text area and clicks **Classify Call**.
2. The app sends `POST /classify/` to the backend API with the raw transcript.
3. The backend returns a `reason` and `category`.
4. The result is displayed on screen.

---

## Prerequisites

| Tool | Purpose | Install |
|------|---------|---------|
| Node.js ≥ 20 | Runtime | [nodejs.org](https://nodejs.org/) |
| npm | Package manager | Bundled with Node.js |

The **backend** must also be running at `http://localhost:8000` — see [call-classifier-backend/README.md](../call-classifier-backend/README.md).

---

## Running locally

```bash
cd call-classifier-frontend
npm install
npm run dev
```

The app opens at **http://localhost:5173**.

---

## Running with Docker

```bash
# Build the image
docker build -t call-classifier-frontend .

# Run — maps container port 80 to host port 3000
docker run -p 3000:80 call-classifier-frontend
```

Visit **http://localhost:3000**.

---

## Available scripts

| Command | What it does |
|---------|-------------|
| `npm run dev` | Start the Vite dev server with hot-reload |
| `npm run build` | Compile and bundle for production (output → `dist/`) |
| `npm run preview` | Serve the production build locally to test it |
| `npm run lint` | Run ESLint to check for code style issues |

---

## Project structure

```
call-classifier-frontend/
├── src/
│   ├── main.jsx       # React entry point — mounts the app into index.html
│   ├── App.jsx        # Root component — all UI logic and API calls
│   ├── App.css        # Styles for the App component
│   └── index.css      # Global styles, CSS variables, dark mode support
├── public/            # Static assets copied as-is to the build output
├── index.html         # HTML shell — Vite injects the JS bundle here
├── vite.config.js     # Vite bundler configuration
├── nginx.conf         # nginx web server config (used in the Docker image)
└── Dockerfile         # Multi-stage Docker build
```
