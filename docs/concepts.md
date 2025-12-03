# Concepts fondamentaux

NEXUS-FLUX repose sur cinq concepts principaux :

---

## 1. Communication vectorielle
Les agents ne s’échangent **aucun message textuel**.
Ils lisent/écrivent dans un espace vectoriel partagé.

---

## 2. État holographique partagé
L’état cognitif global est une collection de nœuds :

- texte,
- score de confiance,
- métadonnées,
- optionnellement embeddings.

Cet état est modifié par tous les agents.

---

## 3. Agents cognitifs
Chaque agent représente une **posture cognitive**, pas un rôle humain :

- EntropicAgent → exploration  
- NegentropicAgent → raffinement  
- DoubtAgent → contradictions  
- ContextualAgent → cohérence  
- PragmaticAgent → production de la sortie

---

## 4. Convergence cognitive
Le moteur effectue plusieurs **ticks** où les agents agissent successivement.
La convergence est atteinte lorsque les meilleurs nœuds dominent la dynamique.

---

## 5. Consensus vectoriel
À la fin :

- les meilleurs nœuds sont sélectionnés,
- un contexte global est construit,
- une solution finale est générée via LLM ou mode simulation.
