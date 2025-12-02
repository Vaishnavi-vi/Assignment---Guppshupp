import json
from src.state import MemoryState

def save_memory(state:MemoryState):
    preferences=state.get("preferences",[])
    emotional_pattrens=state.get("emotional_pattrens",[])
    facts=state.get("facts",[])

    memory_data = {
        "preferences": preferences,
        "emotional_patterns":emotional_pattrens,
        "facts":facts
    }

    with open("memory.json", "w") as f:
        json.dump(memory_data, f, indent=2)

    return state
