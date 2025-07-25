import os
from dotenv import load_dotenv

from reddit import check_reddit_for_algoverse
from notify import send_daily_summary

load_dotenv()

print("🔍 DEBUG ENV")
for var in ["REDDIT_AGENT", "REDDIT_CLIENT_ID", "REDDIT_SECRET", "TWITTER_BEARER", "SLACK_WEBHOOK"]:
    print(f"{var} = {repr(os.getenv(var))}")

# Twitter fetch with safe handling
try:
    from twitter import check_twitter_for_algoverse
    twitter_results = check_twitter_for_algoverse()
except Exception as e:
    print(f"⚠️ Twitter fetch failed: {e}")
    twitter_results = []

# Reddit fetch with stripping Reddit agent
try:
    reddit_results = check_reddit_for_algoverse()
except Exception as e:
    print(f"⚠️ Reddit fetch failed: {e}")
    reddit_results = []

try:
    send_daily_summary(reddit_results, twitter_results)
except Exception as e:
    print(f"⚠️ Slack message failed: {e}")
