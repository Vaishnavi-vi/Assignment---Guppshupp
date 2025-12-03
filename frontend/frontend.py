import sys
import os
import json 
import streamlit as st
from PIL import Image

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


from src.Personality.Workflow.pipeline import workflow
from src.state import PersonalityState



def load_json_file(uploaded_file):
    try:
        return json.load(uploaded_file)
    except:
        st.error("Invalid JSON format in uploaded file.")
        return None


st.set_page_config("GuppShupp AI – Memory & Personality Engine", layout="wide")
page = st.sidebar.radio("Navigation:", ["Home", "Assignment"])

if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "preload" not in st.session_state:
    st.session_state["preload"] = False
if "last_node" not in st.session_state:
    st.session_state["last_node"] = None
if "memory" not in st.session_state:
    st.session_state["memory"] = {
        "preferences": [],
        "emotional_patterns": [],
        "facts": []
    }

if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""


if page == "Home":
    st.header("💬 GuppShupp")
    image = Image.open("C:\\Users\\Dell\\Downloads\\Rag chatbot.png")
    st.image(image, use_container_width=True)
    st.write("""
    Conversational Chatbot:\n
    1. Understands user context over time.\n
    2. Remembers important details.\n
    3. Updates memories when the user changes their mind.\n
    4. Responds in any chosen personality style.\n
    5. Produces JSON memory suitable for storage or analysis.
    """)
    st.sidebar.markdown("---")
    st.sidebar.subheader("About App")
    st.sidebar.info(
        "This project is an AI conversational agent that extracts user preferences, facts, "
        "and emotional patterns from messages, updating its memory dynamically. "
        "It generates responses in a chosen personality or tone, making interactions more personalized and human-like. "
        "The system outputs structured JSON memory for analysis or storage."
    )
    st.sidebar.markdown("---")
    st.sidebar.write("*Created by Vaishnavi Barolia*")


elif page == "Assignment":
    st.header("📝 Guppshupp Chatbot")


    st.sidebar.markdown("---")
    st.sidebar.header("Chatbot Settings:")
    st.sidebar.subheader("Tone")
    tone = st.sidebar.selectbox(
        "Select Personality Tone:",
        [None, "calm_mentor", "witty_friend", "therapist", "concise_professional"]
    )

    st.sidebar.subheader("Input Type:")
    run_node = st.sidebar.radio(
        "Test Input Type",
        ["User Predefined Test Messages","Manual Input", "Upload JSON Messages"]
    )

    # Reset messages if mode changed
    if st.session_state["last_node"] != run_node:
        st.session_state["messages"] = []
        st.session_state["preload"] = False
        st.session_state["last_node"] = run_node


    if run_node == "Manual Input":
        user_msg = st.text_area("Start a new conversation, Enter Your test message here:")
        if st.button("Run"):
            if user_msg.strip():
                st.session_state["messages"].append({"role": "user", "content": user_msg})
            else:
                st.warning("Please enter a message!")

    elif run_node == "User Predefined Test Messages" and not st.session_state["preload"]:
        st.info("Using example test messages:")
        predefined_list = [
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
        ]
        st.code(json.dumps(predefined_list, indent=2), language="json")
        st.session_state["messages"]=(predefined_list)
        st.session_state["preload"] = True

    elif run_node == "Upload JSON Messages":
        uploaded = st.file_uploader("Upload JSON file (list of messages)")
        if uploaded:
            upload_messages = load_json_file(uploaded)
            if upload_messages and isinstance(upload_messages, list):
                st.session_state["messages"]=(upload_messages)


    st.session_state["user_input"] = st.text_input(
        "Type your message here:",
        st.session_state["user_input"]
    )

    if st.button("Send") and st.session_state["user_input"].strip():
        st.session_state["messages"].append({
            "role": "user",
            "content": st.session_state["user_input"]
        })
        st.session_state["user_input"] = ""  

  
    if st.session_state["messages"]:
        input_state: PersonalityState = {
            "messages": st.session_state["messages"],
            "tone": tone,
            "memory": st.session_state["memory"],
            "base_response": "",
            "final_response": ""
        }

        with st.spinner("Thinking..."):
            result = workflow.invoke(input_state)

        # Update memory
        st.session_state["memory"] = result.get("memory", st.session_state["memory"])

        base_resp = result.get("base_response", "")
        final_resp = result.get("final_response", "")

        assistant_reply = final_resp
        if assistant_reply:
            st.session_state["messages"].append({
                "role": "assistant",
                "content": assistant_reply
            })


        st.subheader("Conversation")
        for msg in st.session_state["messages"]:
            if msg["role"] == "user":
                st.markdown(f"**You:** {msg['content']}")
            else:
                st.markdown(f"**AI:** {msg['content']}")


        if base_resp or final_resp:
            st.markdown("---")
            st.subheader("📝 Latest Message Responses")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Before Personality (Neutral):**")
                st.info(base_resp)
            with col2:
                st.markdown("**After Personality (With Tone):**")
                st.success(final_resp)

        # Display memory in sidebar
    st.sidebar.subheader("Current Memory")
    st.sidebar.json(st.session_state["memory"])


                
                


