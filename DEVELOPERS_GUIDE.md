# Nexus-Flux — Developer's Guide

**Created by: YEO Kaffanan Issa**  
**Supported by: IKAFFANAN LTD (UK)**

This guide explains how the internal components of Nexus-Flux work, how to extend the engine, and how to contribute high-quality code.

---

# 🧠 1. System Overview
Nexus-Flux is organized into the following core modules:

```
src/
 ├── agents/        → Cognitive agents (generation, refinement, doubt…)
 ├── analysis/      → Post-mortem tools
 ├── services/      → LLM + embeddings service
 ├── state/         → Holographic shared state (memory / Redis)
 ├── engine.py      → Core cognitive engine
 ├── api.py         → REST API (FastAPI)
 ├── cli.py         → Command line interface
 ├── config.py      → Environment + settings
```

The heart of Nexus-Flux is the **holographic shared state**, where agents contribute ideas as vectors.

---

# 🧩 2. Cognitive Engine Internals

## Engine Loop (Simplified)
```python
for tick in range(settings.max_ticks):
    for agent in agents:
        perception = state.get_attention_mask(agent.profile_vector)
        node = await agent.reason(perception)
        if node:
            await state.add_node(node)

    await state.update_context_vector()
    momentum = state.compute_momentum()

    if momentum < settings.convergence_threshold:
        break
```

### Key Concepts
- **Perception Filtering**: Agents only “see” nodes relevant to their profile.
- **Node Contribution**: Agents generate new CognitiveNodes.
- **Context Update**: Global consensus vector is recomputed each tick.
- **Momentum**: Measures stability. Once low → convergence.

---

# 🔍 3. Agents — How They Work
All agents inherit from `BaseAgent`:

```python
class BaseAgent:
    async def reason(self, state):
        raise NotImplementedError
```

## Agent Pipeline
Each agent:
1. Reads filtered state
2. Generates text via LLM
3. Converts text → vector embedding
4. Creates a CognitiveNode
5. Returns node to engine

## Adding a New Agent
To add a custom agent:
```python
class MyAgent(BaseAgent):
    async def reason(self, state):
        text = "my cognitive insight"
        vector = await self.llm.get_embedding(text)
        return CognitiveNode(
            vector=vector,
            confidence=0.7,
            origin_agent_id=self.id,
            metadata={"text": text}
        )
```
Add it to the factory:
```python
from .my_agent import MyAgent
```

---

# 📦 4. Holographic Shared State
The `BaseHolographicState` defines the cognitive memory interface:

```python
class BaseHolographicState:
    async def add_node(self, node): ...
    async def get_all_nodes(self): ...
    async def get_attention_mask(self, profile): ...
    async def get_context_vector(self): ...
    async def compute_momentum(self): ...
```

Two implementations exist:
- **InMemoryState** — fastest, default
- **RedisState** — scalable, persistent (partial)

---

# 🧪 5. Testing & Quality

## Run all tests
```bash
pytest
```

## Structure tests by module
```
tests/
 ├── test_state.py
 ├── test_agents.py
 └── test_engine.py
```

Write tests for:
- Node creation
- Momentum calculation
- API responses
- Agent behaviour

All PRs must include tests.

---

# ⚙️ 6. Config & Environment
Settings are loaded from `.env` via `pydantic-settings`:
```python
from pydantic_settings import BaseSettings
```

Important variables:
```
LLM_API_KEY
STATE_BACKEND
EMBEDDING_DIM
MAX_TICKS
CONVERGENCE_THRESHOLD
```

---

# 🖥️ 7. API & CLI Integration
The engine is wrapped by:
- **FastAPI** (`src/api.py`)
- **Typer CLI** (`src/cli.py`)

Both call the same engine code — consistency guaranteed.

---

# 🚀 8. Extending the Framework
Ways to extend Nexus-Flux:

### ✔ Add new agent types
Such as:
- emotional agent
- planning agent
- retrieval-augmented agent

### ✔ Add new backends
- Redis full
- PostgreSQL vector DB
- Weaviate / Qdrant

### ✔ Add new execution layers
- Action pipelines
- Tools / plugins

### ✔ Add distributed cognition
Multi-machine clusters.

---

# 🧭 9. Contribution Workflow
1. Fork repository
2. Create feature branch
3. Write clean, typed, tested code
4. Run tests locally
5. Submit PR with explanation
6. Maintainers review

---

# 📝 10. Internal Coding Guidelines
- Async everywhere (`async def`)
- Pure Python, no side effects in agents
- Meaningful variable names
- Small, testable functions
- Document your classes and methods

---

# 👥 Maintainers
- **YEO Kaffanan Issa** — Creator & Lead Architect  
- **IKAFFANAN LTD (UK)** — Official Maintainer

If you want a **flowchart**, **sequence diagram**, or **agent lifecycle diagram**, je peux les ajouter ici !