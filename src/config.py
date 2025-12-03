import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class LLMConfig:
    api_key: str | None
    generation_model: str
    embedding_model: str


@dataclass
class StateConfig:
    backend: str  # "memory" ou "redis"
    redis_url: str | None


@dataclass
class AppConfig:
    llm: LLMConfig
    state: StateConfig


def load_config() -> AppConfig:
    return AppConfig(
        llm=LLMConfig(
            api_key=os.getenv("LLM_API_KEY"),
            generation_model=os.getenv("LLM_GENERATION_MODEL", "gpt-4-turbo-preview"),
            embedding_model=os.getenv("LLM_EMBEDDING_MODEL", "text-embedding-3-small"),
        ),
        state=StateConfig(
            backend=os.getenv("STATE_BACKEND", "memory"),
            redis_url=os.getenv("REDIS_URL"),
        ),
    )
