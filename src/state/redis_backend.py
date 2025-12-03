from __future__ import annotations

from typing import Any, Dict, List
import json
import uuid

import redis

from .base import BaseCognitiveState, CognitiveNode


class RedisCognitiveState(BaseCognitiveState):
    """
    Version simplifiée pour backend Redis.

    ⚠ Cette implémentation est volontairement simple.
    Pour de la prod, il faudra optimiser les structures et clés.
    """

    def __init__(self, url: str) -> None:
        self.client = redis.from_url(url)
        self.root_key = "nexusflux:nodes"

    def create_node(self, text: str, confidence: float, metadata: Dict[str, Any]) -> str:
        node_id = str(uuid.uuid4())
        data = {
            "id": node_id,
            "text": text,
            "confidence": confidence,
            "metadata": metadata,
        }
        self.client.hset(self.root_key, node_id, json.dumps(data, ensure_ascii=False))
        return node_id

    def get_top_nodes(self, limit: int = 5) -> List[CognitiveNode]:
        all_nodes_raw = self.client.hgetall(self.root_key)
        nodes: List[CognitiveNode] = []
        for value in all_nodes_raw.values():
            decoded = json.loads(value)
            nodes.append(
                CognitiveNode(
                    id=decoded["id"],
                    text=decoded["text"],
                    confidence=float(decoded["confidence"]),
                    metadata=decoded.get("metadata", {}),
                )
            )
        nodes.sort(key=lambda n: n.confidence, reverse=True)
        return nodes[:limit]

    def export_snapshot(self) -> Dict[str, Any]:
        all_nodes_raw = self.client.hgetall(self.root_key)
        nodes = [json.loads(v) for v in all_nodes_raw.values()]
        return {"nodes": nodes, "count": len(nodes)}
