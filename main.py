from src.Memory.Workflow.pipeline import workflow1
from src.Personality.Workflow.pipeline import workflow
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage


load_dotenv()

if __name__=="__main__":
    initial_state1={"messages": [
    {"role": "user", "content": "I love eating Italian food and pizza."},
    {"role": "user", "content": "I usually wake up at 6 AM every day."},
    {"role": "user", "content": "I feel stressed whenever deadlines approach."},
    {"role": "user", "content": "I enjoy watching sci-fi movies in my free time."},
    {"role": "user", "content": "I am an introverted person and like quiet places."},
    {"role": "user", "content": "I like listening to classical music while working."},
    {"role": "user", "content": "I live in New York and work as a software engineer."},
    {"role": "user", "content": "I prefer working at night instead of mornings."},
    {"role": "user", "content": "I am allergic to peanuts and always avoid them."},
    {"role": "user", "content": "I feel excited when learning new programming languages."}]}
    
    output=workflow1.invoke(initial_state1)
    
    initial_state2={"messages":HumanMessage(content="I am so stressed about exams"),"tone":"calm_mentor"}
    
    try:
        output=workflow.invoke(initial_state2)
        print("===Base-Message===")
        print(output["base_response"])
        print()
        print("===Final-Response===")
        print(output["final_response"])
    except Exception as e:
        print("Error:",e)