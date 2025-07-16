import os
import praw
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_SECRET"),
    user_agent=os.getenv("REDDIT_AGENT")
)

def check_reddit_for_algoverse(limit=50):
    yesterday = datetime.now(timezone.utc).date() - timedelta(days=1)
    results = []

    for submission in reddit.subreddit("all").search("Algoverse", sort="new", limit=limit):
        created_date = datetime.fromtimestamp(submission.created_utc, tz=timezone.utc).date()
        if created_date == yesterday:
            results.append({
                "title": submission.title,
                "url": submission.url,
                "subreddit": submission.subreddit.display_name
            })

    return results
