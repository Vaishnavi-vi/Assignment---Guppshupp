from src.state import PersonalityState
from src.Personality.llm.llm import model
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from typing import Literal,List
from langchain_core.output_parsers import PydanticOutputParser

def extract_emotions(state: PersonalityState):
    
    message = state["messages"][-1].content
    
    class Emotion(BaseModel):
        emotions:List[str]=Field(default_factory=list)
    
    parser = PydanticOutputParser(pydantic_object=Emotion)
    
    prompt = PromptTemplate(template="""Extract the user's stable emotiona from the following message:{message} below.Return ONLY valid JSON that matches this format:{format_instructions}""",
        input_variables=["message"],
        partial_variables={"format_instructions": parser.get_format_instructions()})
    
    chain=prompt|model|parser
    
    result=chain.invoke({"message":message})
    
    return {"emotions_extracted":result.emotions}