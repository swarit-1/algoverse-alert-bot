import os
import praw
from dotenv import load_dotenv

load_dotenv()

# Reddit credentials from .env
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_SECRET"),
    user_agent=os.getenv("REDDIT_AGENT")
)

def check_reddit_for_algoverse(limit=10):
    print("🔍 Checking Reddit for 'Algoverse'...")
    results = []

    # Search all of Reddit
    for submission in reddit.subreddit("all").search("Algoverse", sort="new", limit=limit):
        results.append({
            "title": submission.title,
            "url": submission.url,
            "created_utc": submission.created_utc,
            "id": submission.id
        })

    return results
