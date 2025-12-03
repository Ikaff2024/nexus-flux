from __future__ import annotations

from typing import Any, Dict, List
import uuid

from .base import BaseCognitiveState, CognitiveNode


class InMemoryCognitiveState(BaseCognitiveState):
    """
    Implémentation simple en mémoire.
    Suffisante pour l'open-source et les tests.
    """

    def __init__(self) -> None:
        self._nodes: Dict[str, CognitiveNode] = {}

    def create_node(self, text: str, confidence: float, metadata: Dict[str, Any]) -> str:
        node_id = str(uuid.uuid4())
        self._nodes[node_id] = CognitiveNode(
            id=node_id,
            text=text,
            confidence=confidence,
            metadata=metadata,
        )
        return node_id

    def get_top_nodes(self, limit: int = 5) -> List[CognitiveNode]:
        nodes = sorted(self._nodes.values(), key=lambda n: n.confidence, reverse=True)
        return nodes[:limit]

    def export_snapshot(self) -> Dict[str, Any]:
        return {
            "nodes": [
                {
                    "id": n.id,
                    "text": n.text,
                    "confidence": n.confidence,
                    "metadata": n.metadata,
                }
                for n in self._nodes.values()
            ],
            "count": len(self._nodes),
        }
