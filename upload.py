# upload
import tweepy
from secret import *

def upload(content):
    # authenticate
    client = tweepy.Client(consumer_key=API_KEY,
                           consumer_secret=API_SECRETS,
                           access_token=ACCESS_TOKEN,
                           access_token_secret=ACCESS_SECRET)
    response = client.create_tweet(text=content)
    print(response)

