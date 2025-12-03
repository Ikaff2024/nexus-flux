from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from .engine import NexusFluxEngine, SolveResult

app = FastAPI(title="NEXUS-FLUX", version="1.0.0")
engine = NexusFluxEngine()


class SolveRequest(BaseModel):
    problem: str


class SolveResponse(BaseModel):
    solution_text: str
    confidence: float
    representative_node_id: str | None
    contributing_nodes: int


@app.post("/solve", response_model=SolveResponse)
async def solve_endpoint(payload: SolveRequest) -> SolveResponse:
    result: SolveResult = await engine.solve(payload.problem)
    return SolveResponse(
        solution_text=result.solution_text,
        confidence=result.confidence,
        representative_node_id=result.representative_node_id,
        contributing_nodes=result.contributing_nodes,
    )
