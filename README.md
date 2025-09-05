# Algoverse Alert Bot

A minimal Python social media scraper which searches for "Algoverse" mentions on Reddit and Twitter, and notifies a Slack channel using incoming webhooks.

## Features

- Searches Reddit and Twitter for "Algoverse"
- Deploys matching results to a target Slack channel
- Simple to run locally with minimal setup

## Tech Stack

- Python 3.12.6
- Libraries: requests, praw, slack_sdk, etc.

## Setup and Usage

1. Clone the repository:
   git clone https://github.com/swarit-1/algoverse-alert-bot.git
   cd algoverse-alert-bot

2. Install dependencies:
   pip install -r requirements.txt

3. Set environment variables. You can use a `.env` file or export these in your shell:
   SLACK_WEBHOOK_URL=your_slack_webhook_url
   REDDIT_CLIENT_ID=your_reddit_client_id
   REDDIT_SECRET=your_reddit_secret
   REDDIT_USER_AGENT=your_reddit_user_agent
   TWITTER_BEARER_TOKEN=your_twitter_bearer_token (if using Twitter)

4. Start the bot:
   python main.py
