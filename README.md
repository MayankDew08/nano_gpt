# 🎭 NanoGPT: Shakespeare Text Generator

<div align="center">

[![Live Demo](https://img.shields.io/badge/Demo-Live-success?style=for-the-badge&logo=netlify)](https://inspiring-axolotl-af5e73.netlify.app/)
[![API](https://img.shields.io/badge/API-Live-blue?style=for-the-badge&logo=fastapi)](https://nano-gpt.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)](https://www.docker.com/)

**A production-ready GPT-based text generation system trained on Shakespeare's complete works**

[Live Demo](https://inspiring-axolotl-af5e73.netlify.app/) • [API Docs](https://nano-gpt.onrender.com/docs) • [Report Bug](https://github.com/YOUR_USERNAME/nano_gpt/issues)

</div>

---

## 📋 Table of Contents

- [Demo](#-demo)
- [Overview](#-overview)
- [Architecture](#-architecture)
- [Features](#-features)
- [Live Deployment](#-live-deployment)
- [Local Development](#-local-development)
- [Docker Deployment](#-docker-deployment)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Technical Details](#-technical-details)
- [Screenshots](#-screenshots)
- [Acknowledgments](#-acknowledgments)
- [License](#-license)

---

## 🎬 Demo

### Live Application
**Frontend:** [https://inspiring-axolotl-af5e73.netlify.app/](https://inspiring-axolotl-af5e73.netlify.app/)  
**Backend API:** [https://nano-gpt.onrender.com](https://nano-gpt.onrender.com)  
**API Documentation:** [https://nano-gpt.onrender.com/docs](https://nano-gpt.onrender.com/docs)

### Demo Video
<!-- Add your demo video here -->
_Coming soon..._

---

## 🌟 Overview

NanoGPT is a **decoder-only transformer architecture** implementation for character-level text generation, trained on the complete works of William Shakespeare. This project demonstrates end-to-end deep learning workflow from training to production deployment.

### Key Highlights

- 🧠 **Decoder-Only Transformer** - GPT-style architecture with 6 layers and 6 attention heads
- 🎭 **Shakespeare Dataset** - Trained on 1MB of Shakespearean text
- 🐋 **Dockerized** - Fully containerized backend for easy deployment
- ☁️ **Cloud Deployed** - Backend on Render, Frontend on Netlify
- ⚡ **FastAPI Backend** - High-performance REST API with automatic documentation
- 🎨 **Modern UI** - Beautiful, responsive frontend with real-time statistics
- 📊 **Production Ready** - Optimized inference, logging, and error handling

### Built Following

This implementation follows **Andrej Karpathy's** ["Let's build GPT: from scratch, in code, spelled out"](https://www.youtube.com/watch?v=kCc8FmEb1nY) video tutorial, extended with production deployment capabilities.

---

## 🏗️ Architecture

### Model Architecture: Decoder-Only Transformer

```
Input Text (Character-Level)
         ↓
   Token Embedding (384-dim)
         +
   Positional Embedding (256 ctx)
         ↓
   ┌─────────────────────┐
   │  Transformer Block  │ × 6 layers
   │  ├─ Multi-Head Attn │   (6 heads each)
   │  ├─ Layer Norm      │
   │  ├─ Feed Forward    │
   │  └─ Layer Norm      │
   └─────────────────────┘
         ↓
   Linear + Softmax (65 vocab)
         ↓
   Generated Character
```

**Architecture Specifications:**
- **Type:** Decoder-only GPT
- **Layers:** 6 transformer blocks
- **Attention Heads:** 6 per layer
- **Embedding Dimension:** 384
- **Context Window:** 256 tokens
- **Vocabulary Size:** 65 unique characters
- **Total Parameters:** ~10M
- **Dropout:** 0.2

### System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend (Netlify)                   │
│  ┌───────────────────────────────────────────────────┐  │
│  │  HTML/CSS/JavaScript (Static Hosting)            │  │
│  │  - Interactive UI                                 │  │
│  │  - Real-time generation statistics                │  │
│  └───────────────────────────────────────────────────┘  │
└───────────────────────┬─────────────────────────────────┘
                        │ HTTPS/REST API
                        ↓
┌─────────────────────────────────────────────────────────┐
│              Backend API (Render + Docker)              │
│  ┌───────────────────────────────────────────────────┐  │
│  │  FastAPI + Uvicorn                                │  │
│  │  ├─ /generate - Text generation endpoint         │  │
│  │  ├─ /docs - Swagger UI                           │  │
│  │  └─ CORS enabled for cross-origin requests       │  │
│  └───────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────┐  │
│  │  Model Service                                    │  │
│  │  ├─ Pre-loaded GPT model (model.pth)             │  │
│  │  ├─ Cached vocabulary (input.txt)                │  │
│  │  └─ Encode/Decode functions                      │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## ✨ Features

### Frontend
- 🎨 **Beautiful UI** - Theatrical theme with smooth animations
- 📝 **Flexible Input** - Optional prompts with customizable generation length
- 🎲 **Smart Randomization** - Auto-select token count from predefined options
- ⚡ **Real-time Stats** - Display generation time, tokens, and character count
- 📋 **One-Click Copy** - Copy generated text to clipboard
- 📱 **Fully Responsive** - Works seamlessly on all devices
- 🌐 **CORS Enabled** - Connects to deployed backend API

### Backend
- 🚀 **High Performance** - Optimized inference with cached vocabulary
- 🧠 **Smart Loading** - Model and vocabulary loaded once at startup
- 📊 **Detailed Logging** - Request/response times and generation metrics
- 🔧 **Configurable** - Environment-based configuration
- 📖 **Auto Documentation** - Swagger UI at `/docs`
- 🐋 **Docker Ready** - Containerized for consistent deployment
- ☁️ **Cloud Deployed** - Running on Render with auto-scaling

---

## 🌐 Live Deployment

### Access the Application

| Component | URL | Description |
|-----------|-----|-------------|
| **Frontend** | [https://inspiring-axolotl-af5e73.netlify.app/](https://inspiring-axolotl-af5e73.netlify.app/) | Interactive web interface |
| **Backend API** | [https://nano-gpt.onrender.com](https://nano-gpt.onrender.com) | REST API endpoint |
| **API Docs** | [https://nano-gpt.onrender.com/docs](https://nano-gpt.onrender.com/docs) | Interactive API documentation |

### Deployment Stack

- **Frontend:** Netlify (Static Site Hosting)
- **Backend:** Render (Containerized Web Service)
- **Containerization:** Docker
- **Base Image:** `python:3.10.13-slim`

---

## 💻 Local Development

### Prerequisites

- Python 3.10+
- Docker (optional, for containerized deployment)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/nano_gpt.git
cd nano_gpt
```

2. **Install backend dependencies**
```bash
cd Backend
pip install -r requirements.txt
```

3. **Start the backend**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4. **Open the frontend**
```bash
# In a new terminal
cd Frontend
python -m http.server 8080
```

5. **Access locally**
- Frontend: `http://localhost:8080`
- Backend API: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`

---

## 🐋 Docker Deployment

### Build & Run with Docker

```bash
# Build the image
docker build --platform=linux/amd64 -f Backend/Dockerfile -t nano_gpt .

# Run the container
docker run -d -p 8000:8000 --name nano_gpt nano_gpt

# View logs
docker logs -f nano_gpt

# Stop the container
docker stop nano_gpt
```

### Docker Configuration

The Dockerfile is optimized for production:
- Multi-stage dependency installation for faster rebuilds
- Slim Python base image to reduce size
- Proper layer caching for efficient builds
- Health checks and logging enabled

**Build Context:** Repository root  
**Dockerfile Location:** `Backend/Dockerfile`  
**Exposed Port:** 8000

---

## 📚 API Documentation

### Endpoints

#### `GET /`
**Health check and API information**

**Response:**
```json
{
  "message": "API for NanoGPT is up and running!",
  "status": "online",
  "endpoints": {
    "generate": "/generate",
    "docs": "/docs"
  }
}
```

#### `POST /generate`
**Generate Shakespearean text**

**Request Body:**
```json
{
  "text": "To be or not to be",  // Optional prompt
  "new_tokens": 500              // Optional (uses random if null)
}
```

**Response:**
```json
{
  "prompt": "To be or not to be",
  "generated_text": "To be or not to be...",
  "tokens_generated": 500,
  "total_length": 2847,
  "generation_time_seconds": 12.456,
  "total_response_time_seconds": 12.523
}
```

**Random Token Options:** If `new_tokens` is `null`, randomly selects from `[500, 750, 1000, 1500, 2000, 2500]`

---

## 📂 Project Structure

```
nano_gpt/
├── Backend/
│   ├── Dockerfile              # Docker build configuration
│   ├── main.py                 # FastAPI application
│   ├── model.py                # GPT model architecture
│   ├── requirements.txt        # Python dependencies
│   ├── run_server.bat          # Windows startup script
│   ├── .gitignore              # Git ignore patterns
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── prompt.py           # Pydantic request/response models
│   └── services/
│       ├── __init__.py
│       └── model_load.py       # Model loading and caching
├── Frontend/
│   ├── index.html              # Single-page application
│   └── README.md               # Frontend documentation
├── Makemore/                   # Training experiments
│   └── *.ipynb                 # Jupyter notebooks
├── model.pth                   # Trained model weights (10M params)
├── input.txt                   # Shakespeare training corpus
├── gpt.py                      # Original training script
├── biagram.py                  # Bigram baseline model
├── gpt_dev.ipynb              # Development notebook
├── START.bat                   # Quick start launcher
└── README.md                   # This file
```

---

## 🔧 Technical Details

### Model Configuration

| Parameter | Value |
|-----------|-------|
| Architecture | Decoder-only Transformer (GPT) |
| Layers | 6 |
| Attention Heads | 6 |
| Embedding Dimension | 384 |
| Context Length | 256 tokens |
| Vocabulary Type | Character-level |
| Vocabulary Size | 65 unique characters |
| Dropout Rate | 0.2 |
| Total Parameters | ~10M |
| Training Data | Shakespeare corpus (1MB) |

### Backend Stack

- **Framework:** FastAPI 0.100+
- **Server:** Uvicorn (ASGI)
- **Deep Learning:** PyTorch 2.10+
- **Validation:** Pydantic
- **Containerization:** Docker
- **Deployment:** Render

### Performance Optimizations

- ✅ Vocabulary loaded once at module import (zero request overhead)
- ✅ Model weights loaded at startup (fast inference)
- ✅ Encode/decode functions cached globally
- ✅ Async request handling
- ✅ Efficient Docker layer caching
- ✅ Minimal base image (`python:3.10.13-slim`)

---

## 📸 Screenshots

### Frontend Interface
<!-- Add screenshots here -->
_Coming soon..._

### API Documentation (Swagger UI)
<!-- Add screenshot of /docs -->
_Coming soon..._

### Docker Deployment
<!-- Add screenshot of Docker running -->
_Coming soon..._

---

## 🙏 Acknowledgments

### Inspiration & Learning

This project was built following **[Andrej Karpathy's](https://karpathy.ai/)** exceptional tutorial series:

- 📺 **Video:** ["Let's build GPT: from scratch, in code, spelled out"](https://www.youtube.com/watch?v=kCc8FmEb1nY)
- 📝 **Paper:** ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762) (Vaswani et al., 2017)
- 🎓 **Course:** [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)

### Key Concepts Learned

- Decoder-only transformer architecture
- Multi-head self-attention mechanism
- Positional embeddings
- Layer normalization and residual connections
- Character-level tokenization
- Autoregressive text generation
- Production deployment with Docker

### Technologies Used

- **PyTorch** - Deep learning framework
- **FastAPI** - Modern Python web framework
- **Docker** - Containerization platform
- **Render** - Cloud deployment platform
- **Netlify** - Static site hosting

---

## 📄 License

This project is open source and available for educational purposes.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

<div align="center">

**Built with 💜 by following Andrej Karpathy's teachings**

⭐ Star this repo if you found it helpful!

</div>
