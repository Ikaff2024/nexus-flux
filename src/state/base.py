from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Protocol


@dataclass
class CognitiveNode:
    id: str
    text: str
    confidence: float
    metadata: Dict[str, Any]


class BaseCognitiveState(Protocol):
    def create_node(self, text: str, confidence: float, metadata: Dict[str, Any]) -> str:
        ...

    def get_top_nodes(self, limit: int = 5) -> List[CognitiveNode]:
        ...

    def export_snapshot(self) -> Dict[str, Any]:
        ...
