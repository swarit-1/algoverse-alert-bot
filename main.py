from datetime import datetime, timedelta
from pytz import timezone
from reddit import fetch_reddit_mentions
from twitter import fetch_twitter_mentions
from notify import send_daily_summary

# Set timezone
PST = timezone('America/Los_Angeles')
now = datetime.now(PST)
since_time = now - timedelta(hours=24)

# Fetch posts from past 24 hours
reddit_results = []
twitter_results = []

try:
    reddit_results = fetch_reddit_mentions(since_time=since_time)
except Exception as e:
    print(f"⚠️ Reddit fetch failed: {e}")

try:
    twitter_results = fetch_twitter_mentions(since_time=since_time)
except Exception as e:
    print(f"⚠️ Twitter fetch failed: {e}")

# Send to Slack
try:
    send_daily_summary(reddit_results, twitter_results)
except Exception as e:
    print(f"⚠️ Slack notify failed: {e}")
