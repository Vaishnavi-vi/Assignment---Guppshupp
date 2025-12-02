from src.Memory.llm.llm import model
from src.state import MemoryState
from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate



def emotional_pattrens(state: MemoryState):
    text = state["all_messages"]

    class EmotionPattern(BaseModel):
        emotional_pattrens: List[str] = Field(default_factory=list)

    parser = PydanticOutputParser(pydantic_object=EmotionPattern)

    # Prompt for LLM
    prompt = PromptTemplate(template="""Extract user emotions from the text below. Return ONLY a valid JSON object with a key "emotional_pattrens" as a list of strings.
                            Text:
        {text} {format_instructions} """,
        input_variables=["text"],
        partial_variables={"format_instructions": parser.get_format_instructions()})

    chain = prompt | model | parser

    try:
        result = chain.invoke({"text": text})
        return {"emotional_pattrens": result.emotional_pattrens}
    except Exception as e:
        print("Error parsing output:", e)
        raw_output = chain.invoke({"text": text}, return_raw=True)
        print("Raw output:", raw_output)