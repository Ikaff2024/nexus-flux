# Nexus-Flux

## ✨ Vision
Nexus-Flux is a **post-LangChain cognitive engine** based on vector-space reasoning instead of message passing. Its architecture mirrors biological cognition and ensures mathematical convergence.

## 🚀 Why Nexus-Flux Is Revolutionary
- Zero-message architecture → no hallucination cascades
- Multi-agent cognition through holographic state
- Momentum-based convergence guarantees stability
- Enterprise-ready and academically rigorous
- Designed for patents, research labs, and production

## 🧩 Core Principles
1. **Holography** — shared latent cognitive field
2. **Emergence** — ideas arise from agent interaction
3. **Convergence** — semantic momentum ensures stability
4. **Modularity** — agents plug-and-play
5. **Reproducibility** — deterministic under fixed seeds

## 💼 Use Cases
### Industrial
- Autonomous technical reporting
- Multi-agent cognitive monitoring
- AI-driven R&D assistants

### Business
- Strategy synthesis
- Market intelligence cognition

### Scientific
- Hypothesis generation
- Model interpretability

## 📊 Benchmarks (Preview)
Benchmarks coming in v1.1:
- Convergence tick distribution
- Semantic stability metrics
- Agent contribution maps
- Throughput under heavy load



![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)  
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)  
![Maintained](https://img.shields.io/badge/Maintained%20by-IKAFFANAN%20LTD-purple.svg)  
![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)  
![Docs](https://img.shields.io/badge/Documentation-Complete-success.svg)  
![OpenAI](https://img.shields.io/badge/Compatible-OpenAI%20API-orange.svg)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg) — Installation Guide

**Created by: YEO Kaffanan Issa**  
**Supported by: IKAFFANAN LTD (UK)**

This guide explains how to install, configure and run Nexus-Flux on your machine.
It is designed to be simple and accessible — even if you are not a technical expert.

---

# 🧩 1. Requirements
Before installing Nexus-Flux, ensure you have:

### ✔ Python 3.10 or higher
Check your version:
```bash
python --version
```

### ✔ pip (Python package manager)
Check with:
```bash
pip --version
```

### ✔ Git (optional, recommended)
```bash
git --version
```

---

# 📥 2. Download the Nexus-Flux Project
You have two options:

## Option A — Download ZIP (Easy)
1. Go to the GitHub repository
2. Click **Code → Download ZIP**
3. Extract the folder on your computer

## Option B — Clone with Git (Recommended)
```bash
git clone https://github.com/your-username/nexus-flux.git
cd nexus-flux
```

---

# 📦 3. Create a Virtual Environment (Recommended)
A virtual environment keeps dependencies clean.

### Create venv
```bash
python -m venv venv
```

### Activate it
**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

---

# 📚 4. Install Dependencies
Inside the project folder:

```bash
pip install -r requirements.txt
```

Or to install Nexus-Flux itself as a package:
```bash
pip install -e .
```

---

# 🔐 5. Configure Environment Variables
Nexus-Flux uses a `.env` file to store API keys and settings.

### Step 1 — Copy example file
```bash
cp .env.example .env
```

### Step 2 — Open `.env` and edit your settings
```
LLM_API_KEY="your_openai_api_key"
LLM_GENERATION_MODEL="gpt-4-turbo-preview"
LLM_EMBEDDING_MODEL="text-embedding-3-small"
STATE_BACKEND="memory"
```

### Where to get an API key?
You can obtain one from:
- OpenAI
- Any OpenAI-compatible provider

---

# 🚀 6. Running Nexus-Flux (CLI)
Run a cognitive reasoning session:

```bash
python -m src.cli solve "Explain black holes in simple terms"
```

Output example:
```
--- RÉSULTAT DU CONSENSUS ---
Black holes are regions of space where gravity is extremely strong...
```

A `solution.md` file will be created automatically by the PragmaticAgent.

---

# 🖥️ 7. Running the API Server
Launch the FastAPI server:
```bash
uvicorn src.api:app --reload
```

Then open in your browser:
```
http://localhost:8000/docs
```
You now have a full interactive API.

---

# 🧪 8. Running Tests
To ensure everything is working:
```bash
pytest
```

---

# ⚠️ Troubleshooting

### 🟥 Error: "LLM API key missing"
Solution: Edit your `.env` file and set:
```
LLM_API_KEY=your_key_here
```

### 🟥 Error: "Model not found"
Check that your `.env` contains valid model names.

### 🟥 Redis errors
Only appears if `STATE_BACKEND="redis"`.
Make sure Redis is installed:
```bash
redis-server
```

---

# 🎉 Installation Complete!
You are ready to use Nexus-Flux.

If you'd like:
- a Docker installation guide,
- a Windows installer,
- a 1-click setup script,
I can generate that too.

---

**Maintainers:**  
**YEO Kaffanan Issa** — Creator & Lead Architect  
**IKAFFANAN LTD (UK)** — Official Maintainer and Sponsor
