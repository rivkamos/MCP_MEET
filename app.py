"""
STREAMLIT UI
------------

מה זה Streamlit?
-----------------
ספרייה שמאפשרת לבנות UI לפייתון בקלות:
- בלי HTML
- בלי JS
- רק Python

מושלם לדמואים של AI
"""

import streamlit as st
from agent import run_agent

# -------------------------
# UI Title
# -------------------------
st.title("🧠 AI Meeting Agent")
st.write("LangChain + LangGraph + Gemini + Tools Demo")

# -------------------------
# Input
# -------------------------
user_input = st.text_input("Ask about your meetings:")

# -------------------------
# Button
# -------------------------
if st.button("Run Agent"):

    if user_input.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking... 🤖"):

            response = run_agent(user_input)

        st.success("Done!")
        st.write("### 🤖 Answer:")
        st.write(response)

# -------------------------
# Sidebar explanation
# -------------------------
st.sidebar.title("📘 What is this?")
st.sidebar.write("""
This demo shows:

✔ LangChain = connects AI + tools  
✔ LangGraph = agent reasoning flow  
✔ Tool = function (get meetings)  
✔ AI decides when to use tools  
""")