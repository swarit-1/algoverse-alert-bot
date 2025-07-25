import os
import praw
from dotenv import load_dotenv

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
    for submission in reddit.subreddit("all").search("Algoverse", sort="new", limit=10):
        post = {
            "title": submission.title,
            "url": submission.url,
            "permalink": f"https://reddit.com{submission.permalink}"
        }
        posts.append(post)
    return posts
