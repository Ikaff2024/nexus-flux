# Installation

---

## Prérequis
- Python 3.10+
- pip

---

## Installation

```bash
git clone https://github.com/<votre-compte>/nexus-flux.git
cd nexus-flux
pip install -r requirements.txt
pip install -e .
```

---

## Configuration

```bash
cp .env.example .env
```

Paramètres :

```
LLM_API_KEY=
STATE_BACKEND=memory
REDIS_URL=
```

---

## Lancer la CLI

```
python -m src.cli solve "Créer une application"
```

---

## Lancer l’API

```
uvicorn src.api:app --reload
```

Documentation interactive :

```
http://127.0.0.1:8000/docs
```
