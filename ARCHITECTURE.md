# Nexus-Flux — Architecture détaillée

**Créé par : YEO Kaffanan Issa**  
**Supporté par : IKAFFANAN LTD (UK)**

---

# 🧠 Architecture Globale
Nexus-Flux repose sur une **architecture cognitive holographique**, où des agents spécialisés ne communiquent pas par messages, mais uniquement via un **état partagé vectoriel**.

L’ensemble forme une intelligence collective stable, mathématiquement convergente.

---

# 🏛️ Vue d'ensemble (High-Level Diagram)
```
                    ┌───────────────────────────────┐
                    │         Cognitive Agents       │
                    │───────────────────────────────│
                    │ Entropic (Génération)          │
                    │ Negentropic (Raffinement)      │
                    │ Doubt (Challenge)              │
                    │ Contextual (Cohérence)         │
                    │ Pragmatic (Action)             │
                    └─────────────────────▲─────────┘
                                          │
                                 Perception via Attention Mask
                                          │
                                          ▼
                    ┌───────────────────────────────┐
                    │     Holographic Shared State   │
                    │───────────────────────────────│
                    │ Cognitive Nodes (vecteurs)     │
                    │ Global Context Vector (C_t)    │
                    │ Cognitive Momentum (M_t)       │
                    └─────────────────────▲─────────┘
                                          │ Updates
                                          ▼
                    ┌───────────────────────────────┐
                    │         Nexus-Flux Engine      │
                    │───────────────────────────────│
                    │ Tick Loop                      │
                    │ Convergence Logic              │
                    │ Consensus Synthesis            │
                    └─────────────────────▲─────────┘
                                          │
                                          ▼
                    ┌───────────────────────────────┐
                    │     Output / Execution Layer   │
                    │ (PragmaticAgent → Actions)     │
                    └───────────────────────────────┘
```

---

# 🔍 1. Les Agents Cognitifs (Cognitive Agents)
Chaque agent joue un rôle épistémique spécifique. Ensemble, ils forment une intelligence collective.

### **1. EntropicAgent (Générateur-Alpha)**
- Produit des idées divergentes
- Explore l’espace latent
- Injecte de l’entropie contrôlée

### **2. NegentropicAgent (Raffineur-Beta, Gamma)**
- Réduit la dispersion sémantique
- Cherche la cohérence et améliore les idées
- Applique une forme de "descente cognitive"

### **3. DoubtAgent (Challenger-Delta)**
- Introduit l’incertitude constructive
- Détecte les idées trop confiantes
- Évite les consensus faux-positifs

### **4. ContextualAgent (Historien-Epsilon)**
- Garde la mémoire logique du raisonnement
- Détecte contradictions et incohérences

### **5. PragmaticAgent (Exécuteur-Omega)**
- Transforme le consensus final en action concrète
- Ex : création d’un fichier, exécution, formatage

---

# 🧬 2. Holographic Shared State
Le cœur de Nexus-Flux : un état vectoriel partagé qui fonctionne comme un **substrat cognitif commun**.

Il contient :
- tous les **nœuds cognitifs** (CognitiveNode),
- le **contexte global** (C_t),
- le **momentum cognitif** (M_t),
- l’attention contextuelle.

### Structure d’un CognitiveNode
```
CognitiveNode(
    vector: ndarray,
    confidence: float,
    origin_agent_id: str,
    metadata: dict,
    created_at: timestamp
)
```

### Backend disponibles
- **InMemoryState** : rapide, simple, idéal pour développement
- **RedisState** : persistant, scalable, distribué (bientôt complet)

---

# ⚙️ 3. Nexus-Flux Engine
Le moteur central orchestre le fonctionnement des agents.

### Pipeline du moteur
```
for tick in range(MAX_TICKS):
    1) Perception (attention mask)
    2) Contribution des agents
    3) Mise à jour du contexte global
    4) Calcul du momentum
    5) Vérification de la convergence
```

### Critère de convergence
```
M_t = || C_t - C_{t-1} ||  <  ε
```

---

# 🌀 4. Attention Mask (Filtrage Cognitif)
Chaque agent ne voit qu’une partie de l’état global.

Exemple :
- un agent orienté vers la "créativité" regarde les nœuds sémantiquement proches de son profil
- un agent contextuel consulte les nœuds "fortement établis"

```
attention_mask = cos_similarity(node.vector, agent.profile_vector)
if attention_mask > threshold:
    agent_perceives(node)
```

---

# 🧮 5. Consensus Vector (Contexte Global)
Le consensus final est calculé via :
```
C_t = Σ(c_i * v_i) / Σ(c_i)
```

Puis le moteur effectue :
- une extraction du nœud représentatif
- une synthèse générative via LLM


---

# 🔧 6. FastAPI & CLI Interfaces
### API
```
POST /solve
{
  "problem": "Explain quantum gravity"
}
```

### CLI
```
python -m src.cli solve "My problem here"
```

---

# 🗂️ 7. Architecture Dossier
```
Nexus-Flux/
│ README.md
│ overview.md
│ ARCHITECTURE.md
│ SECURITY.md
│ CONTRIBUTING.md
│ CODE_OF_CONDUCT.md
│
├── src/
│   ├── api.py
│   ├── cli.py
│   ├── engine.py
│   ├── config.py
│   ├── services/
│   ├── agents/
│   └── state/
│
└── tests/
```

---

# 🧭 Conclusion
L’architecture de Nexus-Flux est conçue pour :
- être **mathématiquement stable**,
- réduire la complexité inhérente aux agents LLM,
- permettre une cognition multi-agent **biologiquement inspirée**,
- fournir une base solide pour l’IA collective de nouvelle génération.

Cette architecture marque une rupture avec les frameworks classiques et prépare le terrain pour un futur où les systèmes IA pourront raisonner **en essaim**, **sans messages**, et avec une stabilité garantie.

---

**Créateur : YEO Kaffanan Issa**  
**Support institutionnel : IKAFFANAN LTD (UK)**
