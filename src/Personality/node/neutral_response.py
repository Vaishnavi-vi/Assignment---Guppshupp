from src.state import PersonalityState
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.Personality.llm.llm import model


def generate_neutral_response(state:PersonalityState):
    """Generate a neutral, plain response before applying personality tone."""
    message=state["messages"][-1].content
    
    prompt=PromptTemplate(template="""You are a helpful assistant. Given the user's message below, produce a concise helpful reply in 2-3 lines.
    Do NOT adopt any specific persona or unusual tone — neutral and informative.user_message:{user_message}""",input_variables=["user_message"])
    
    parser=StrOutputParser()
    
    chain=prompt|model|parser
    
    result=chain.invoke({"user_message":message})
    
    return {"base_response":result}