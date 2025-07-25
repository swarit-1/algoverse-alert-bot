import os
import praw
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()

ua = os.getenv("REDDIT_AGENT", "")
safe_ua = ua.strip()
print(f"▶ Reddit user agent: {repr(safe_ua)}")

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=safe_ua
)

def check_reddit_for_algoverse():
    posts = []

    # Calculate start and end of "yesterday" in UTC
    now = datetime.now(timezone.utc)
    start = datetime(now.year, now.month, now.day, tzinfo=timezone.utc) - timedelta(days=1)
    end = start + timedelta(days=1)

    for submission in reddit.subreddit("all").search("Algoverse", sort="new", limit=50):
        created = datetime.fromtimestamp(submission.created_utc, tz=timezone.utc)
        if start <= created < end:
            post = {
                "title": submission.title,
                "url": submission.url,
                "permalink": f"https://reddit.com{submission.permalink}"
            }
            posts.append(post)

    return posts
