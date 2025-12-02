from src.state import MemoryState

def extract(state:MemoryState):
    all_msg="\n".join(msg["content"] for msg in state["messages"] if msg["role"]=="user")
    
    return {"all_messages":all_msg}