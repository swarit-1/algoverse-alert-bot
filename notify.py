import os
import requests
from datetime import datetime
import pytz  # Added for timezone support

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL", "").strip()

def send_daily_summary(reddit_posts, twitter_posts):
    if not SLACK_WEBHOOK or not SLACK_WEBHOOK.startswith("https://hooks.slack.com/"):
        print("⚠️ Invalid SLACK_WEBHOOK:", repr(SLACK_WEBHOOK))
        return

    # Changed to use US Eastern Time
    eastern = pytz.timezone("US/Eastern")
    now = datetime.now(eastern).strftime("%Y-%m-%d %H:%M")
    message_lines = [f"*Algoverse Alerts — {now} ET*"]  # Updated PT -> ET

    if reddit_posts:
        message_lines.append("\n*Reddit Mentions:*")
        for post in reddit_posts:
            message_lines.append(f"- <{post['permalink']}|{post['title']}>")
    else:
        message_lines.append("\nNo Reddit mentions found.")

    if twitter_posts:
        message_lines.append("\n*Twitter Mentions:*")
        for tweet in twitter_posts:
            message_lines.append(f"- {tweet}")
    else:
        message_lines.append("\nNo Twitter mentions found.")

    message = "\n".join(message_lines)
    
    try:
        response = requests.post(SLACK_WEBHOOK, json={"text": message})
        print(f"✅ Slack message sent: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Error sending Slack message: {e}")