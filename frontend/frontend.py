import sys
import os
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.Memory.Workflow.pipeline import workflow1
from src.Personality.Workflow.pipeline import workflow2

st.set_page_config("Assignment===Guppsgupp", layout="centered")
page=st.sidebar.radio("Navigation:",["Home","Assignment"])

if page=="Home":
    st.header("💬 GuppShupp")
    image = Image.open("C:\\Users\\Dell\\Downloads\\Rag chatbot.png")
    st.image(image,use_container_width=True)
    st.write(""" Conversational Chatbot:\n
             1. Understands user context over time.\n
             2. Remembers important details.\n
             3. Updates memories when the user changes their mind.\n
             4. Responds in any chosen personality style\n
             5. Produces JSON memory suitable for storage or analysis.\n""")
    st.sidebar.markdown("---")
    st.sidebar.subheader("About App")
    st.sidebar.info("This project is an AI conversational agent that extracts user preferences, facts, and emotional patterns from messages, updating its memory dynamically. It generates responses in a chosen personality or tone, making interactions more personalized and human-like. The system outputs structured JSON memory for analysis or storage")
    
    st.sidebar.markdown("---")
    st.sidebar.write("*Created by Vaishnavi Barolia*")
    

elif page == "Assignment":
    st.header("📝 Assignment Chatbot")

    # ---------------- INITIAL MESSAGES ----------------
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "user", "content": "I love eating Italian food and pizza."},
            {"role": "user", "content": "I usually wake up at 6 AM every day."},
            {"role": "user", "content": "I feel stressed whenever deadlines approach."},
            {"role": "user", "content": "I enjoy watching sci-fi movies in my free time."},
            {"role": "user", "content": "I am an introverted person and like quiet places."},
            {"role": "user", "content": "I like listening to classical music while working."},
            {"role": "user", "content": "I live in New York and work as a software engineer."},
            {"role": "user", "content": "I prefer working at night instead of mornings."},
            {"role": "user", "content": "I am allergic to peanuts and always avoid them."},
            {"role": "user", "content": "I feel excited when learning new programming languages."}
            # ... add up to 30
        ]

    # ---------------- MEMORY ----------------
    if "memory" not in st.session_state:
        output_memory = workflow1.invoke({
            "messages": st.session_state.messages,
            "memory": {}
        })
        st.session_state.memory = output_memory.get("memory", {})

    st.subheader("Current Memory")
    st.json(st.session_state.memory)

    # ---------------- USER INPUT ----------------
    user_input = st.text_input("Type your message:")
    tone = st.selectbox("Select a tone for your response:", ["Calm_mentor", "Witty_friend", "Therapist", "None"])

    if st.button("Send") and user_input:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Update memory
        st.session_state.memory = workflow1.invoke({
            "messages": st.session_state.messages,
            "memory": st.session_state.memory
        }).get("memory", {})

        # Generate personality response
        output2 = workflow2.invoke({
            "messages": st.session_state.messages,
            "memory": st.session_state.memory,
            "tone": tone
        })

        base_response = output2.get("base_response", "")
        final_response = output2.get("final_response", "")

        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": final_response})

    # ---------------- DISPLAY CHAT ----------------
    st.subheader("Chat History")
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Bot:** {msg['content']}")

    # Optional: show memory
    st.subheader("Updated Memory")
    st.json(st.session_state.memory)
