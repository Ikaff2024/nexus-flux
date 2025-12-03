# Architecture du moteur NEXUS-FLUX

```
src/
 ├── agents/
 ├── state/
 ├── services/
 ├── engine.py
 ├── api.py
 ├── cli.py
 └── config.py
```

---

## 1. State Layer
Backend mémoire ou Redis.

---

## 2. Agents Layer
Chaque agent implémente `.act(tick)`.

---

## 3. Engine Layer
- crée le nœud racine,  
- exécute les agents,  
- sélectionne les nœuds dominants,  
- génère la solution finale.

---

## 4. Services Layer
- LLMService  
- SemanticLogger

---

## 5. API Layer
FastAPI pour exposer `/solve`.

---

## 6. CLI Layer
Interface ligne de commande.
