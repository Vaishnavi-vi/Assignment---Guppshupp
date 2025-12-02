from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    llm_endpoint = HuggingFaceEndpoint(
        repo_id="openai/gpt-oss-20b",
        temperature=0.7,
        task="text_generation"
    )
    return ChatHuggingFace(llm=llm_endpoint)

model = get_llm()