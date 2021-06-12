# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:47:14 2021

@author: morya
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream

import tweepy
import pandas as pd
import pprint
import ast

import twitter_credentials as tcred

class TwitterStreamer():
    # Class for streaming and processing live tweets.
    
    def __init__(self):
        pass
    
    def stream_tweets(self):
        # This function handles Authentication and connection to Twitter Streaming API.
        
        auth = OAuthHandler(tcred.CONSUMER_KEY, tcred.CONSUMER_SECRET)
        auth.set_access_token(tcred.ACCESS_TOKEN, tcred.ACCESS_TOKEN_SECRET)
        
        api = tweepy.API(auth)

        filter_list = "vaccine OR covid vaccine OR coronavirus OR covishield OR astrazeneca OR covaxin AND exclude:retweets AND exclude:replies"
        geocode = "19.0759899,72.8773928,30km"

        results = api.search(q=filter_list, geocode=geocode, count=100, since_id="")

        json_data = [r._json for r in results]

        df = pd.json_normalize(json_data)
        print(df.head())
        df.to_csv("vaccine_tweets2.csv")
            

if __name__ == "__main__":
    
    twitterStreamer = TwitterStreamer()
    twitterStreamer.stream_tweets()

if __name__ != "__main__":
    
    twitterStreamer = TwitterStreamer()
    twitterStreamer.stream_tweets()