from langgraph.graph import StateGraph,START,END
from src.state import PersonalityState
from src.Personality.node.retriever_memory import retriever_memory
from src.Personality.node.neutral_response import generate_neutral_response
from src.Personality.node.apply_personality import apply_personality
from src.Personality.node.update_memory import update_memory
from src.Personality.node.extract_facts import extract_facts
from src.Personality.node.extract_preference import extract_preferences
from src.Personality.node.extracts_emotion import extract_emotions
from typing import Literal


def check_condition(state:PersonalityState)->Literal["apply","skip"]:
    if state["tone"]==None:
        return "skip"
    else:
        return "apply"
    

graph=StateGraph(PersonalityState)
graph.add_node("retriever_memory",retriever_memory)
graph.add_node("generate_neutral_response",generate_neutral_response)
graph.add_node("apply_personality",apply_personality)
graph.add_node("update_memory",update_memory)
graph.add_node("extract_preferences", extract_preferences)
graph.add_node("extract_facts", extract_facts)
graph.add_node("extract_emotions", extract_emotions)

graph.add_edge(START,"retriever_memory")
graph.add_edge("retriever_memory","extract_preferences")
graph.add_edge("extract_preferences","extract_facts")
graph.add_edge("extract_facts","extract_emotions")
graph.add_edge("extract_emotions","update_memory")
graph.add_edge("update_memory","generate_neutral_response")
graph.add_conditional_edges("generate_neutral_response",check_condition,{"skip":END,"apply":"apply_personality"})
graph.add_edge("generate_neutral_response","apply_personality")
graph.add_edge("generate_neutral_response",END)
graph.add_edge("apply_personality",END)

workflow=graph.compile()
