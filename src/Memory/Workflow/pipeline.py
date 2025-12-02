from langgraph.graph import StateGraph,START,END
from src.state import MemoryState
from src.Memory.node.extract import extract
from src.Memory.node.preference import load_preference
from src.Memory.node.emotional_pattren import emotional_pattrens
from src.Memory.node.facts import load_facts
from src.Memory.node.memory_saver import save_memory


graph=StateGraph(MemoryState)

graph.add_node("extract",extract)
graph.add_node("load_preference",load_preference)
graph.add_node("emotional_pattrens",emotional_pattrens)
graph.add_node("load_facts",load_facts)
graph.add_node("save_memory",save_memory)

graph.add_edge(START,"extract")
graph.add_edge("extract","load_preference")
graph.add_edge("load_preference","emotional_pattrens")
graph.add_edge("emotional_pattrens","load_facts")
graph.add_edge("load_facts","save_memory")
graph.add_edge("save_memory",END)


workflow1=graph.compile()