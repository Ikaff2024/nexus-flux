from __future__ import annotations

from typing import Any

from ..state.base import BaseCognitiveState
from ..services.llm_service import LLMService
from ..services.semantic_logger import SemanticLogger
from .base import BaseAgent


class BaseCognitiveAgent(BaseAgent):
    def __init__(
        self,
        name: str,
        state: BaseCognitiveState,
        llm: LLMService,
        logger: SemanticLogger,
    ) -> None:
        self.name = name
        self.state = state
        self.llm = llm
        self.logger = logger

    async def act(self, tick: int) -> None:  # type: ignore[override]
        raise NotImplementedError


class EntropicAgent(BaseCognitiveAgent):
    """Explore : génère de nouvelles idées à partir du problème ou des nœuds existants."""

    async def act(self, tick: int) -> None:
        # Version SAFE : ne fait qu'un petit enrichissement symbolique
        self.logger.log_event("agent_entropic_tick", {"tick": tick})
        # Dans la version safe, on n'appelle pas encore le LLM ici.


class NegentropicAgent(BaseCognitiveAgent):
    """Raffine : en version SAFE, ne fait que logguer l'intention."""

    async def act(self, tick: int) -> None:
        self.logger.log_event("agent_negentropic_tick", {"tick": tick})


class DoubtAgent(BaseCognitiveAgent):
    """Ajoute de la contradiction productive (ici : simple trace)."""

    async def act(self, tick: int) -> None:
        self.logger.log_event("agent_doubt_tick", {"tick": tick})


class ContextualAgent(BaseCognitiveAgent):
    """Vérifie la cohérence globale (ici : trace simplifiée)."""

    async def act(self, tick: int) -> None:
        self.logger.log_event("agent_contextual_tick", {"tick": tick})


class PragmaticAgent(BaseCognitiveAgent):
    """En version complète, déclencherait les actions concrètes. Ici, uniquement trace."""

    async def act(self, tick: int) -> None:
        self.logger.log_event("agent_pragmatic_tick", {"tick": tick})
