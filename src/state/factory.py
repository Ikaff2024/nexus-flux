from __future__ import annotations

from .base import BaseCognitiveState
from .memory import InMemoryCognitiveState
from .redis_backend import RedisCognitiveState
from ..config import StateConfig


def create_state_backend(config: StateConfig) -> BaseCognitiveState:
    if config.backend == "redis" and config.redis_url:
        return RedisCognitiveState(config.redis_url)
    return InMemoryCognitiveState()
