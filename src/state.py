from typing import TypedDict, List, Any, Dict, Annotated
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class MemoryState(TypedDict):
    messages:List[Dict[str,str]]
    all_messages:str
    preferences:List[str]
    emotional_pattrens:List[str]
    facts:List[str]

class PersonalityState(TypedDict):
    messages:Annotated[List[BaseMessage],add_messages]   
    memory: Dict[str,Any]     
    tone:str                                                 
    base_response: str                    
    final_response: str      