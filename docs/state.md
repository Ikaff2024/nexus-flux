# State System — État holographique partagé

Le State System est le cœur de la mémoire de NEXUS-FLUX.  
Il représente l’espace cognitif dans lequel les agents lisent, écrivent, modifient et évaluent des nœuds cognitifs.

Chaque nœud contient 

```json
{
  id uuid,
  text contenu d'une idée,
  confidence 0.72,
  metadata { source agent_entropic }
}
