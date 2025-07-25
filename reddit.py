import praw
from datetime import datetime
import os
from pytz import timezone

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = "Algoverse keyword monitor"

KEYWORDS = ["algoverse", "#algoverse", "algoverse.ai", "algoverseairesearch"]

def fetch_reddit_mentions(since_time):
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )

    mentions = []

    for submission in reddit.subreddit("all").new(limit=100):
        created = datetime.fromtimestamp(submission.created_utc, tz=timezone('UTC'))
        if created < since_time:
            continue
        text = f"{submission.title} {submission.selftext}".lower()
        if any(keyword in text for keyword in KEYWORDS):
            mentions.append({
                "source": "Reddit",
                "title": submission.title,
                "url": submission.url,
                "permalink": f"https://reddit.com{submission.permalink}",
                "created": created
            })

    return mentions
