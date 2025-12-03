from __future__ import annotations

from typing import Protocol


class BaseAgent(Protocol):
    async def act(self, tick: int) -> None:
        ...
