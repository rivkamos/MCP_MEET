import json

def get_meetings():
    """Load meetings from local file (MCP-style tool)."""
    with open("moc_meetings.json", "r") as f:
        data = json.load(f)
    return data