from src.state import PersonalityState
from src.Personality.node.retriever_memory import save_memory_file


def update_memory(state: PersonalityState):
    memory = state["memory"]

    prefs = state.get("preferences_extracted", [])
    facts = state.get("facts_extracted", [])
    emotions = state.get("emotions_extracted", [])

    # Add preferences
    for p in prefs:
        if p not in memory["preferences"]:
            memory["preferences"].append(p)

    # Add facts
    for f in facts:
        if f not in memory["facts"]:
            memory["facts"].append(f)

    # Add emotional patterns
    for e in emotions:
        if e not in memory["emotional_patterns"]:
            memory["emotional_patterns"].append(e)

    save_memory_file(memory)

    return {"memory": memory}

        

        
        
    
    
    
    