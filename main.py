import os
from reddit import check_reddit_for_algoverse
from notify import send_daily_summary

# Try to load Twitter
try:
    from twitter import check_twitter_for_algoverse
    twitter_results = check_twitter_for_algoverse()
except Exception as e:
    print(f"⚠️ Twitter fetch failed: {e}")
    twitter_results = []

# Try Reddit
try:
    reddit_results = check_reddit_for_algoverse()
except Exception as e:
    print(f"⚠️ Reddit fetch failed: {e}")
    reddit_results = []

# Notify only if webhook is defined
slack_webhook = os.getenv("SLACK_WEBHOOK")

if slack_webhook:
    send_daily_summary(reddit_results, twitter_results)
else:
    print("⚠️ SLACK_WEBHOOK is not set — skipping Slack message.")