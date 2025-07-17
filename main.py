import os
from reddit import fetch_reddit_data
from twitter import fetch_twitter_data
from notify import send_daily_summary

# Load and sanitize environment variables
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "").strip()
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "").strip()
REDDIT_AGENT = os.getenv("REDDIT_AGENT", "").strip()
TWITTER_BEARER = os.getenv("TWITTER_BEARER", "").strip()
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK", "").strip()

if not SLACK_WEBHOOK:
    raise EnvironmentError("SLACK_WEBHOOK is not set or empty.")
if not TWITTER_BEARER:
    raise EnvironmentError("TWITTER_BEARER is not set or empty.")
if not REDDIT_CLIENT_ID or not REDDIT_CLIENT_SECRET or not REDDIT_AGENT:
    raise EnvironmentError("Reddit credentials are not fully set.")

print("✅ Environment variables loaded successfully.")

# Fetch data
try:
    reddit_results = fetch_reddit_data(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_AGENT)
except Exception as e:
    print(f"\u26a0\ufe0f Reddit fetch failed: {e}")
    reddit_results = []

try:
    twitter_results = fetch_twitter_data(TWITTER_BEARER)
except Exception as e:
    print(f"\u26a0\ufe0f Twitter fetch failed: {e}")
    twitter_results = []

# Send to Slack
send_daily_summary(reddit_results, twitter_results, SLACK_WEBHOOK)
