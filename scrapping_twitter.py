import tweepy
import os

consumer_key = '***********'
consumer_secret = '*****************'


auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

import pandas as pd
dataset = []
item_search = ['#Tunisia','AI'] # seach item, hashtag ...
for search in item_search : 
  for tweet in tweepy.Cursor(api.search_tweets, q=f"({search}) -filter:retweets", lang = 'en',tweet_mode='extended', count = 100 ).items(500):

      tweet_data = {'user_name':tweet.user.screen_name,
                    'text':tweet.full_text
                  }

      dataset.append(tweet_data)

df = pd.DataFrame(dataset)
df