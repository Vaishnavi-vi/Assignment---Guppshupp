from src.Memory.llm.llm import model
from src.state import MemoryState
from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

def load_facts(state: MemoryState):
    text = state["all_messages"]

    # Define Pydantic model
    class FactsPattern(BaseModel):
        facts: List[str] = Field(default_factory=list)

    parser = PydanticOutputParser(pydantic_object=FactsPattern)

    # Prompt for LLM
    prompt = PromptTemplate(template="""Extract objective facts from the text below.Return ONLY a valid JSON object with a key "facts" as a list of strings.
        Text: {text} {format_instructions}""",
        input_variables=["text"],
        partial_variables={"format_instructions": parser.get_format_instructions()})

    chain = prompt | model | parser

    try:
        result = chain.invoke({"text": text})
        return {"facts": result.facts}
    except Exception as e:
        print("Error parsing output:", e)