import os
import requests
from datetime import datetime
from pytz import timezone

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

def format_item(item):
    return f"- <{item['url']}|{item['title'].strip()}> ({item['source']}, {item['created'].astimezone(timezone('America/Los_Angeles')).strftime('%b %d, %I:%M %p')})"

def send_daily_summary(reddit_results, twitter_results):
    all_results = reddit_results + twitter_results
    all_results.sort(key=lambda x: x["created"], reverse=True)

    if not all_results:
        message = "No Algoverse mentions found in the past 24 hours."
    else:
        message = "*Daily Algoverse Keyword Mentions Summary:*\n\n"
        message += "\n".join(format_item(item) for item in all_results)

    response = requests.post(SLACK_WEBHOOK, json={"text": message})
    if not response.ok:
        raise Exception(f"Slack webhook failed: {response.status_code} - {response.text}")
