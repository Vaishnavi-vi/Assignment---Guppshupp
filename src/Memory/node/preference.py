from src.Memory.llm.llm import model
from src.state import MemoryState
from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate


def load_preference(state: MemoryState):
    text = state["all_messages"]

    class Pattern(BaseModel):
        preferences: List[str] = Field(default_factory=list)

    parser = PydanticOutputParser(pydantic_object=Pattern)

    # Prompt
    prompt = PromptTemplate(template="""Extract the user's stable preferences from the conversation below.Return ONLY valid JSON that matches this format:{format_instructions} Conversation text:{text}""",
        input_variables=["text"],
        partial_variables={"format_instructions": parser.get_format_instructions()})

    chain = prompt | model | parser

    try:
        result = chain.invoke({"text": text})
        return {"preferences": result.preferences}

    except Exception as e:
        print("Error parsing output:", e)
