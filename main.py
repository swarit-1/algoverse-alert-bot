from reddit import check_reddit_for_algoverse
from twitter import fetch_recent_tweets
from notify import send_slack_alert
from storage import load_seen_ids, save_seen_ids

# Load previously seen IDs from file
seen_ids = load_seen_ids()

# --- Reddit Monitoring ---
reddit_results = check_reddit_for_algoverse(limit=10)

for post in reddit_results:
    if post["id"] not in seen_ids:
        send_slack_alert(post["title"], post["url"])
        seen_ids.add(post["id"])

# --- Twitter Monitoring ---
tweets = fetch_recent_tweets(query="Algoverse", max_results=10)

for tweet in tweets:
    tweet_id = str(tweet.id)
    if tweet_id not in seen_ids:
        tweet_url = f"https://twitter.com/i/web/status/{tweet.id}"
        tweet_title = tweet.text.replace('\n', ' ')[:100] + "..."
        send_slack_alert(tweet_title, tweet_url)
        seen_ids.add(tweet_id)

# Save updated seen IDs to file
save_seen_ids(seen_ids)
