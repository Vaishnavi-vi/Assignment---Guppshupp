from src.state import PersonalityState
from langchain_core.prompts import PromptTemplate
from src.Personality.llm.llm import model
from langchain_core.output_parsers import StrOutputParser

def apply_personality(state: PersonalityState):
    """
    Rewrites the neutral response into the requested tone using memory to personalize.
    """
    tone = state["tone"]
    memory = state["memory"]
    neutral = state["base_response"]


    tone_instructions = {
        "calm_mentor": "Rewrite the reply so it sounds like a calm, supportive mentor. Keep it gentle, encouraging, and slightly explanatory.",
        "witty_friend": "Rewrite the reply to sound like a witty, playful friend. Keep it light, humorous, and brief.",
        "therapist": "Rewrite the reply to sound like a therapist: reflective, empathetic, non-judgmental, and supportive.",
        "concise_professional": "Rewrite the reply to be concise and professional, suitable for workplace communication."
    }

    # FIX 1: Get actual tone
    instr = tone_instructions.get(tone, "")

    prompt = PromptTemplate(
        template="""You are a personality transformer.User memory:{memory},Base reply: {base},Task: {instr}, Rules:
        Preserve the original meaning of the base reply.
        - Personalize the reply using the memory if relevant.
        - Do NOT invent new facts.
        - Output only the rewritten reply in 2-3 lines""",
        input_variables=["base", "instr", "memory"]
    )


    chain = prompt | model | StrOutputParser()

    final = chain.invoke({
        "base": neutral,
        "instr": instr,
        "memory": memory
    })

    return {"final_response": final}