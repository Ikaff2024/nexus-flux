# Moteur Nexus-Flux

Le moteur exécute :

---

## 1. Initialisation
- chargement des configs,
- choix du backend (memory / redis),
- création du nœud racine,
- instanciation des agents.

---

## 2. Boucle de ticks
Chaque tick :

1. EntropicAgent agit  
2. NegentropicAgent agit  
3. DoubtAgent agit  
4. ContextualAgent agit  
5. PragmaticAgent agit  

---

## 3. Consensus vectoriel (version safe)
- sélection des meilleurs nœuds,
- construction d’un contexte global,
- génération de la solution finale.

---

## 4. Résultat final
Renvoie :

- texte de solution,
- confiance,
- id du nœud représentatif,
- nombre de nœuds contributeurs.
