“The project runs locally using Streamlit.
Instructions are provided in README.”

💬 GuppShupp - AI Conversational Chatbot

**Author:** Vaishnavi Barolia

---

## 📝 Project Overview

GuppShupp is an AI conversational agent designed to understand and remember user context over time. It extracts key details such as user preferences, emotional patterns, and facts worth remembering, allowing personalized interactions. The agent can respond in different personality tones, such as calm mentor, witty friend, or therapist-style, and outputs structured JSON memory for analysis or storage.

---

## ⚙ Features

1. **Memory Extraction**  
   - Identifies user preferences from chat messages.  
   - Detects emotional patterns.  
   - Extracts factual information.

2. **Personality Engine**  
   - Rewrites responses in a chosen personality tone.  
   - Shows before/after differences in responses.

3. **JSON Memory Output**  
   - Saves extracted memory into `memory.json`.  
   - Dynamically updates when user changes their preferences.

4. **Interactive UI**  
   - Built with Streamlit.  
   - Simple and intuitive interface for chat interactions.

---

## 🧰 Tech Stack

- Python 3.10+  
- Streamlit (frontend interface)  
- LangChain / LLM model (memory extraction and personality transformation)  
- JSON storage for memory

---

## 🚀 Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Vaishnavi-vi/Assignment---Guppshupp.git
cd Assignment
In the Powershell streamlit run frontend/frontend.py
url _link=assignment---guppshupp-mmujjv7azjtftp5m6vb46j
But to run the application you need to create huggingface api_key and then run streamlit app 

