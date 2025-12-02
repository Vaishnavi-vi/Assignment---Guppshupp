from langgraph.graph import StateGraph,START,END
from src.state import PersonalityState
from src.Personality.node.retriever_memory import retriever_memory
from src.Personality.node.neutral_response import generate_neutral_response
from src.Personality.node.apply_personality import apply_personality




graph=StateGraph(PersonalityState)
graph.add_node("retriever_memory",retriever_memory)
graph.add_node("generate_neutral_response",generate_neutral_response)
graph.add_node("apply_personality",apply_personality)

graph.add_edge(START,"retriever_memory")
graph.add_edge("retriever_memory","generate_neutral_response")
graph.add_edge("generate_neutral_response","apply_personality")
graph.add_edge("apply_personality",END)

workflow2=graph.compile()