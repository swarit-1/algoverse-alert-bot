import os
import tweepy
import requests
from dotenv import load_dotenv
import time

load_dotenv()

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def fetch_recent_tweets(query="Algoverse", max_results=10):
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    try:
        tweets = client.search_recent_tweets(
            query=query,
            max_results=max_results,
            tweet_fields=["created_at", "author_id"]
        )
        return tweets.data if tweets.data else []
    except tweepy.TooManyRequests as e:
        reset_time = e.response.headers.get("x-rate-limit-reset")
        print("⚠️ Twitter rate limit reached. Skipping this run.")
        if reset_time:
            print(f"⏳ Rate limit resets at UNIX time: {reset_time}")
        return []
    except Exception as e:
        print("❌ Twitter fetch failed:", str(e))
        return []

def send_slack_notification(tweet):
    message = f"📢 New Tweet mentioning *Algoverse*:\nhttps://twitter.com/i/web/status/{tweet.id}\n\n_@{tweet.author_id}_ said:\n>{tweet.text}"
    payload = {"text": message}
    try:
        requests.post(SLACK_WEBHOOK_URL, json=payload)
    except Exception as e:
        print("❌ Failed to send Slack message:", str(e))

def monitor_twitter(seen_ids):
    tweets = fetch_recent_tweets()
    if not tweets:
        return
    new_tweets = [t for t in tweets if str(t.id) not in seen_ids]
    for tweet in new_tweets:
        send_slack_notification(tweet)
        seen_ids.add(str(tweet.id))
