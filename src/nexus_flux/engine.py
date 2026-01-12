from .state import SharedState
from .consensus import compute_consensus
from .config import settings
class Engine:
    def run(self):
        s=SharedState()
        for _ in range(settings.MAX_TICKS): s.add(1.0)
        return compute_consensus(s.vectors)
