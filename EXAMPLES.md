# Nexus-Flux — Examples

**Created by: YEO Kaffanan Issa**  
**Supported by: IKAFFANAN LTD (UK)**

This guide provides practical examples to help you use Nexus-Flux via:
- CLI (Command Line Interface)
- REST API (FastAPI)
- Python script

---

# 🟦 1. CLI Examples
Nexus-Flux ships with a full Typer-powered CLI.

Launch a problem-solving session:
```bash
python -m src.cli solve "Explain black holes like I'm 12"
```
Output example:
```
--- RÉSULTAT DU CONSENSUS ---
A black hole is a region where gravity is so strong that not even light can escape...

--- PHASE D'ACTION ---
Statut de l'action: success
Fichier de sortie: solution.md
```

---

# 🟩 2. API Examples (FastAPI)
First, run the API locally:
```bash
uvicorn src.api:app --reload
```


## ▶️ Example 1 — Solve a Problem (cURL)
```bash
curl -X POST http://localhost:8000/solve \
  -H "Content-Type: application/json" \
  -d '{"problem": "Give me three startup ideas for African agriculture"}'
```

Typical JSON response:
```json
{
  "status": "success",
  "solution_text": "Here are three startup ideas...",
  "ticks": 6,
  "momentum": 0.0031,
  "consensus_vector": [...],
  "representative_node": {
    "text": "Agri-sensor network for farmers",
    "confidence": 0.82
  }
}
```

---

## ▶️ Example 2 — Solve a Problem (Python)
```python
import requests

response = requests.post(
    "http://localhost:8000/solve",
    json={"problem": "Summarize the principles of Islamic finance"}
)
print(response.json())
```

---

# 🟧 3. Using Nexus-Flux Inside Python
You can call the engine directly in your code.

```python
import asyncio
from src.engine import NexusFluxEngine
from src.config import load_settings
from src.services.llm_service import VectorizationService
from src.state.factory import get_state_backend
from src.agents.factory import get_default_agents

async def main():
    problem = "Explain neural networks in simple terms"

    settings = load_settings()
    llm = VectorizationService(settings)
    state = get_state_backend(settings)
    agents = get_default_agents(llm, problem)

    engine = NexusFluxEngine(
        agents=agents,
        state=state,
        settings=settings,
        problem_statement=problem
    )

    await engine.run()
    result = await engine.get_consensus_result()

    print("Solution:", result["solution_text"])

asyncio.run(main())
```

---

# 🟥 4. Example of Generated `solution.md`
After a problem is solved, the **PragmaticAgent** creates a Markdown file.

Example content:
```
# Solution: Benefits of Solar Energy

## Summary
Solar energy is renewable, affordable, and increasingly efficient.

## Key Points
- Reduces electricity bills
- Minimal maintenance
- Helps fight climate change
```

---

# 🟪 5. Example Problems You Can Try
Here are some interesting problems for testing Nexus-Flux:

### Creativity
- "Invent a new fintech product for West Africa."
- "Give me 5 innovative business ideas for Côte d'Ivoire."

### Science
- "Explain quantum entanglement using everyday analogies."

### Strategy
- "How can a small company outperform big competitors?"

### Learning
- "Teach me the basics of machine learning in 10 bullet points."

---

# 🧭 Notes
- The system automatically converges based on momentum.
- Redis backend support is partial but evolving.
- PragmaticAgent execution can be disabled via `.env`.

---

# 🙌 Maintainers
**YEO Kaffanan Issa** — Creator & Lead Architect  
**IKAFFANAN LTD (UK)** — Official maintainer & sponsor

If you want more advanced examples (multi-step reasoning, chains, or benchmarks), je peux les créer aussi.