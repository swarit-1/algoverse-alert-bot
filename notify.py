import os
import requests
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

def send_slack_alert(text, url):
    if not SLACK_WEBHOOK:
        print("Slack webhook not set!")
        return

    message = f"📢 *New Reddit mention of Algoverse!*\n*Title:* {text}\n🔗 {url}"
    payload = {"text": message}

    response = requests.post(SLACK_WEBHOOK, json=payload)
    
    if response.status_code != 200:
        print("Failed to send Slack message:", response.text)
