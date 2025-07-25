import os
import requests
from datetime import datetime, timedelta
from pytz import timezone

TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
KEYWORDS = ["algoverse", "#algoverse", "algoverse.ai", "algoverseairesearch"]

def fetch_twitter_mentions(since_time):
    headers = {
        "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}",
    }

    query = " OR ".join(KEYWORDS)
    since_str = since_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&start_time={since_str}&tweet.fields=created_at,author_id&expansions=author_id"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Twitter API Error: {response.status_code} - {response.text}")

    data = response.json()
    tweets = []

    for tweet in data.get("data", []):
        tweet_time = datetime.fromisoformat(tweet["created_at"].replace("Z", "+00:00"))
        if tweet_time >= since_time:
            tweets.append({
                "source": "Twitter",
                "title": tweet["text"].split("\n")[0][:80] + "...",
                "url": f"https://twitter.com/i/web/status/{tweet['id']}",
                "created": tweet_time
            })

    return tweets
