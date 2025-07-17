import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

def send_daily_summary(reddit_posts, twitter_posts):
    date_str = (datetime.now() - timedelta(days=1)).strftime("%B %d, %Y")
    header = f":loudspeaker: *Algoverse Mentions* - {date_str}"

    total_mentions = len(reddit_posts) + len(twitter_posts)
    if total_mentions == 0:
        message = f"{header}\nNo new mentions of 'Algoverse' found yesterday."
        requests.post(SLACK_WEBHOOK, json={"text": message})
        return

    counts = f"Reddit ({len(reddit_posts)}) | X/Twitter ({len(twitter_posts)})"

    lines = []

    for post in reddit_posts:
        line = f"- <{post['url']}|r/{post['subreddit']}: “{post['title']}”>"
        lines.append(line)

    for tweet in twitter_posts:
        text = post_preview(tweet['text'])
        line = f"- <{tweet['url']}|X: {text}>"
        lines.append(line)


    message = f"{header}\n{counts}\n" + "\n".join(lines)

    requests.post(SLACK_WEBHOOK, json={"text": message})


def post_preview(text, limit=80):
    text = text.replace("\n", " ")
    return text[:limit] + ("..." if len(text) > limit else "")
