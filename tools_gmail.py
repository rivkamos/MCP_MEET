import os
import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

TOKEN_FILE = "token.json"
CREDENTIALS_FILE = "credentials.json"


def authenticate_gmail():
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIALS_FILE, SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def get_gmail_emails(max_results: int = 10):
    """
    Fetch recent Gmail messages and return simplified data.
    """

    service = authenticate_gmail()

    results = service.users().messages().list(
        userId="me",
        maxResults=max_results
    ).execute()

    messages = results.get("messages", [])

    output = []

    for msg in messages:
        data = service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()

        headers = data["payload"].get("headers", [])

        subject = ""
        for h in headers:
            if h["name"] == "Subject":
                subject = h["value"]

        snippet = data.get("snippet", "")

        output.append({
            "subject": subject,
            "snippet": snippet
        })

    return output