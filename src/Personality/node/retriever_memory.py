import os, json
from typing import Any, Dict
from src.state import PersonalityState


MEMORY_FILE = "memory.json"

def load_memory_file() -> Dict[str, Any]:
    """Load memory.json if exists, else return empty structured memory."""
    with open(MEMORY_FILE, "r") as f:
        try:
            return json.load(f)
        except Exception:
            return {"preferences": {},"facts": {},"emotional_patterns": {}}

def retriever_memory(state:PersonalityState):
    memory=load_memory_file()
    
    return {"memory":memory}