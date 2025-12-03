import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


class SemanticLogger:
    """
    Logger simple qui écrit dans execution_log.jsonl
    sans exposer de logique interne sensible.
    """

    def __init__(self, path: str = "execution_log.jsonl") -> None:
        self.path = Path(path)

    def log_event(self, event_type: str, payload: Optional[Dict[str, Any]] = None) -> None:
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "payload": payload or {},
        }
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
