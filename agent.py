import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from tools import get_meetings

# LLM (Gemini)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Tools list
tools = [get_meetings]

# Agent עם ReAct (Reason + Act)
agent = create_react_agent(llm, tools)


def run_agent(user_input: str):
    result = agent.invoke(
        {"messages": [("user", user_input)]}
    )
    return result["messages"][-1].content