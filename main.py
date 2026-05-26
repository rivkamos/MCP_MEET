"""
MAIN FILE
--------

כאן המשתמש מדבר עם ה-Agent.

אין לוגיקה מורכבת — רק ממשק פשוט.
"""

from agent import run_agent

print("\n📅 AI Agent with LangChain + LangGraph\n")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = run_agent(user_input)

    print("\n🤖 AI:", response, "\n")