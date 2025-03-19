import tweepy
import time
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# Authenticate with Twitter API
client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)

def search_and_reply(keywords, response, max_tweets=10):
  query = " OR ".join(keywords) + " -is:retweet"  # Avoid retweets
  replied_tweets = []
  try:
    tweets = client.search_recent_tweets(query=query, max_results=max_tweets)
    if tweets.data:
      for tweet in tweets.data:
        try:
          client.create_tweet(text=response, in_reply_to_tweet_id=tweet.id)
          replied_tweets.append(tweet.id)
          print(f"Replied to: {tweet.id}")
          # time.sleep(5)  # Avoid rate limits
        except tweepy.TooManyRequests:
          print("Rate limit exceeded! Waiting for 15 minutes...")
          # time.sleep(900)  # Wait 15 minutes
        except Exception as e:
          print(f"Error replying to {tweet.id}: {e}")
    else:
      print("No matching tweets found.")

  except tweepy.TooManyRequests:
    print("Rate limit exceeded! Waiting for 15 minutes...")
    # time.sleep(900)  
  except Exception as e:
    print(f"Error fetching tweets: {e}")
  return replied_tweets

# Define keywords and response
keywords = ["keyword1", "keyword2"]
response = "This is a bot reply"
