
# API REST — FastAPI

---

## Endpoint : POST /solve

### Requête :
```json
{
  "problem": "Créer une application anti-procrastination"
}
```

### Réponse :
```json
{
  "solution_text": "...",
  "confidence": 0.92,
  "representative_node_id": "uuid",
  "contributing_nodes": 5
}
```

---

L’API utilise :

- Pydantic  
- FastAPI  
- NexusFluxEngine
