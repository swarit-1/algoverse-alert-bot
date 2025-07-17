import os
import praw
from dotenv import load_dotenv
from datetime import datetime, timezone
from utils import get_yesterday_bounds

load_dotenv()

# Initialize Reddit client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_AGENT")
)

def check_reddit_for_algoverse(limit=50):
    start, end = get_yesterday_bounds()  # Get UTC window for yesterday
    results = []

    for submission in reddit.subreddit("all").search("Algoverse", sort="new", limit=limit):
        created_time = datetime.fromtimestamp(submission.created_utc, tz=timezone.utc)
        if start <= created_time < end:
            results.append({
                "title": submission.title,
                "url": submission.url,
                "subreddit": submission.subreddit.display_name
            })

    return results
