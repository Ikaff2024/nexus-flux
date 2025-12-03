from __future__ import annotations

import asyncio

import typer

from .engine import NexusFluxEngine

app = typer.Typer(help="CLI pour le moteur NEXUS-FLUX (version safe).")


@app.command()
def solve(problem: str) -> None:
    """Résoudre un problème via le moteur Nexus-Flux."""
    async def _run() -> None:
        engine = NexusFluxEngine()
        result = await engine.solve(problem)
        typer.echo("--- RÉSULTAT DU CONSENSUS ---")
        typer.echo(result.solution_text)
        typer.echo()
        typer.echo(f"Confiance : {result.confidence:.2f}")
        typer.echo(f"Nœud représentatif : {result.representative_node_id}")
        typer.echo(f"Nœuds contributeurs : {result.contributing_nodes}")

    asyncio.run(_run())


if __name__ == "__main__":
    app()
