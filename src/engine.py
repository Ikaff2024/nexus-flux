from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List

from .config import load_config
from .services.llm_service import LLMService
from .services.semantic_logger import SemanticLogger
from .state.base import BaseCognitiveState
from .state.factory import create_state_backend
from .agents.cognitive_agents import (
    EntropicAgent,
    NegentropicAgent,
    DoubtAgent,
    ContextualAgent,
    PragmaticAgent,
)


@dataclass
class SolveResult:
    solution_text: str
    confidence: float
    representative_node_id: str | None
    contributing_nodes: int


class NexusFluxEngine:
    """
    Version safe / publique :
    - structure cohérente avec la doc
    - mais logique épistémique interne simplifiée.
    """

    def __init__(self) -> None:
        self.config = load_config()
        self.state: BaseCognitiveState = create_state_backend(self.config.state)
        self.llm = LLMService(self.config.llm)
        self.logger = SemanticLogger()

        # Agents cognitifs (version simplifiée)
        self.agents = [
            EntropicAgent(self.state, self.llm, self.logger),
            NegentropicAgent(self.state, self.llm, self.logger),
            DoubtAgent(self.state, self.llm, self.logger),
            ContextualAgent(self.state, self.llm, self.logger),
            PragmaticAgent(self.state, self.llm, self.logger),
        ]

    async def solve(self, problem: str) -> SolveResult:
        """
        Pipeline safe :
        - crée un premier nœud d'idée
        - fait intervenir les agents quelques tours
        - synthétise une réponse finale
        """

        self.logger.log_event("session_start", {"problem": problem})

        # 1. Initialisation : créer un nœud racine
        root_node_id = self.state.create_node(
            text=problem,
            confidence=0.5,
            metadata={"type": "problem"},
        )

        # 2. Quelques ticks cognitifs simplifiés
        max_ticks = 4
        for tick in range(max_ticks):
            self.logger.log_event("tick_start", {"tick": tick})
            for agent in self.agents:
                await agent.act(tick=tick)
            self.logger.log_event("tick_end", {"tick": tick})

        # 3. Consensus vectoriel SAFE = on récupère les meilleurs nœuds
        top_nodes = self.state.get_top_nodes(limit=5)
        combined_context = "\n\n".join(n.text for n in top_nodes)

        # 4. Appel LLM pour produire la solution finale
        solution = await self.llm.generate_solution(
            problem=problem,
            context=combined_context,
        )

        self.logger.log_event(
            "session_end",
            {
                "root_node_id": root_node_id,
                "top_nodes_count": len(top_nodes),
            },
        )

        representative_id = top_nodes[0].id if top_nodes else root_node_id
        return SolveResult(
            solution_text=solution,
            confidence=0.9,
            representative_node_id=representative_id,
            contributing_nodes=len(top_nodes),
        )

    def get_raw_state_snapshot(self) -> Dict[str, Any]:
        """Utile pour des analyses ou outils de debug."""
        return self.state.export_snapshot()
