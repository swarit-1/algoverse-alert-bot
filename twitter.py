import os
import tweepy
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()

client = tweepy.Client(bearer_token=os.getenv("TWITTER_BEARER_TOKEN"))

def check_twitter_for_algoverse(limit=25):
    yesterday = datetime.now(timezone.utc) - timedelta(days=1)
    today = datetime.now(timezone.utc)

    tweets = client.search_recent_tweets(
        query="Algoverse -is:retweet",
        max_results=limit,
        tweet_fields=["created_at", "author_id"]
    )

    results = []

    for tweet in tweets.data or []:
        if yesterday.date() <= tweet.created_at.date() < today.date():
            results.append({
                "text": tweet.text,
                "url": f"https://twitter.com/i/web/status/{tweet.id}",
                "author_id": tweet.author_id
            })

    return results
