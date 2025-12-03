from __future__ import annotations

from typing import Optional

try:
    import openai
except ImportError:  # sécurité si la lib n'est pas installée
    openai = None  # type: ignore

from ..config import LLMConfig


class LLMService:
    """
    Service LLM simple.
    - Si LLM_API_KEY est présent → tente d'utiliser l'API OpenAI.
    - Sinon → mode MOCK déterministe (pas de dépendance externe).
    """

    def __init__(self, config: LLMConfig) -> None:
        self.config = config
        if openai and config.api_key:
            openai.api_key = config.api_key

    async def generate_solution(self, problem: str, context: str) -> str:
        if not openai or not self.config.api_key:
            # Mode mock safe
            return (
                "Solution (mode simulation) pour le problème : "
                f"« {problem} ».\n\n"
                "Contexte traité :\n"
                f"{context[:800]}...\n\n"
                "[Remplacez ce mode par un appel LLM réel si nécessaire.]"
            )

        # Version simple : un seul appel, prompt concaténé
        prompt = (
            "Tu es un moteur d'intelligence collective. À partir du problème "
            "et du contexte ci-dessous, produis une solution claire, structurée "
            "et actionnable.\n\n"
            f"PROBLÈME :\n{problem}\n\n"
            f"CONTEXTE COGNITIF :\n{context}\n\n"
            "RÉPONSE :"
        )

        # Ici on peut utiliser le client OpenAI moderne, mais pour rester générique
        # on garde une version classique.
        response = await openai.ChatCompletion.acreate(  # type: ignore[attr-defined]
            model=self.config.generation_model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message["content"]  # type: ignore[index]
