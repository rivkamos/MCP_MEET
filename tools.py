"""
TOOLS FILE
----------

מה זה Tool?
-----------
Tool הוא פונקציה שה-AI יכול להשתמש בה כדי לקבל מידע מהעולם החיצוני.

בדוגמה שלנו:
הכלי קורא פגישות מקובץ מקומי (במקום Gmail או API אמיתי).

זה הבסיס של MCP / Agents:
AI + Tools = מערכת חכמה יותר
"""

import json
from langchain_core.tools import tool


@tool
def get_meetings():
    """
    מחזיר רשימת פגישות מהקובץ המקומי.

    ה-AI יכול לקרוא לפונקציה הזו לבד.
    """
    with open("moc_meetings.json", "r") as f:
        return json.load(f)