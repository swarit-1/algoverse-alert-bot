from reddit import check_reddit_for_algoverse
from notify import send_daily_summary

# Try to import and run Twitter fetch, but handle failure
try:
    from twitter import check_twitter_for_algoverse
    twitter_results = check_twitter_for_algoverse()
except Exception as e:
    print(f"⚠️ Twitter fetch failed: {e}")
    twitter_results = []

# Always fetch Reddit
reddit_results = check_reddit_for_algoverse()

# Send final Slack message
send_daily_summary(reddit_results, twitter_results)
