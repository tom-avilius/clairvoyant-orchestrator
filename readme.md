# Clairvoyant Orchestrator

Clairvoyant Orchestrator is the backend coordination service for the Clairvoyant platform — a lightweight, multi-layered pipeline designed to detect and analyze fake news using NLI, sentiment analysis, and classifier models. It acts as the central API layer, integrating scraping, preprocessing, inference, and token-based feedback mechanisms.

## 🚀 Getting Started

### 1. Clone and Install

```bash
git clone https://github.com/tom-avilius/clairvoyant-orchestrator.git
cd clairvoyant-orchestrator
npm install
```

### 2. Setup Environment Variables

> Use PORT 8001

### 3. Run Development Server

```bash
npm run dev

📦 API Highlights
```

| Endpoint                | Description                          |
| ----------------------- | ------------------------------------ |
| `POST /analyze`         | Accepts query and runs full pipeline |
| `GET /sources?uuid=...` | Returns parsed source articles       |
|                         |                                      |

---

```

---

## 📄 License

GNU GPL v3

---

```
