
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    MAX_TICKS: int = 5
    CONVERGENCE_THRESHOLD: float = 0.01
settings = Settings()
