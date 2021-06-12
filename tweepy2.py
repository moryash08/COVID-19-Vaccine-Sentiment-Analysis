import tweepy
import webbrowser
import time
import csv
import argparse
import os

import twitter_credentials as tcred
from tweepy import OAuthHandler, Stream

def compose_dict_obj(raw_data, keys, search_words):
    """
    Return a dictionary of selected keys from raw_data
    """
    d = {}
    for key in keys:
        if key == "keyword":
            d[key] = search_words
        else:
            if key == "entities":
                hashtag_string = ""
                hashtag_array = raw_data.get(key)["hashtags"]
                for i in range(0,len(hashtag_array)):
                    if i != len(hashtag_array) - 1:
                        hashtag_string += hashtag_array[i]["text"] + ","
                    else:
                        hashtag_string += hashtag_array[i]["text"]
                d["hashtags"] = hashtag_string
            elif key == "user":
                d["user_handle"] = raw_data.get(key)["name"]
                d["user_screen_name"] = raw_data.get(key)["screen_name"]
                d["user_location"] = raw_data.get(key)["location"]
                d["user_followers_count"] = raw_data.get(key)["followers_count"]
                d["user_verified"] = raw_data.get(key)["verified"]
            else:
                d[key] = raw_data.get(key)
    return d

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process each .")
    # parser.add_argument("-k", "--keyword", help="The keyword to search", required=True)
    parser.add_argument("--num", help="Max number of data to scrape", default=20000)
    parser.add_argument(
        "-o", "--output", help="The filepath of the output file", default="./raw_india4.csv"
    )

    args = parser.parse_args()

    consumer_key = tcred.CONSUMER_KEY
    consumer_secret = tcred.CONSUMER_SECRET

    # search_words = "Covid19 vaccine -filter:retweets"
    search_words = "vaccine OR covid vaccine OR coronavirus OR covishield OR Covishield OR astrazeneca OR AstraZeneca OR COVAXIN OR covaxin AND exclude:retweets AND exclude:replies"
    max_num = int(args.num)
    csv_file = args.output

    keys = [
        "created_at",
        "id",
        "full_text",
        "source",
        "retweet_count",
        "favorite_count",
        "entities",
        "user",
        "keyword",
    ]

    callback_uri = "oob"  # https://cfe.sh/twitter/callback
    
    auth = OAuthHandler(tcred.CONSUMER_KEY, tcred.CONSUMER_SECRET)
    auth.set_access_token(tcred.ACCESS_TOKEN, tcred.ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    # Mumbai
    geocode = "19.0759899,72.8773928,60km"
    # UP
    geocode = "26.8467,80.9462,500km"
    # India
    geocode = "23.609382,79.460456,1160km"

    tweetCursor = tweepy.Cursor(
        api.search, q=search_words, lang="en", tweet_mode="extended", count = 100, geocode = geocode
    ).items(1)
    try:
        fieldnames = [
            "created_at",
            "id",
            "full_text",
            "source",
            "retweet_count",
            "favorite_count",
            "hashtags",
            "user_handle",
            "user_screen_name",
            "user_location",
            "user_followers_count",
            "user_verified",
            "keyword",
        ]
        with open(csv_file, "w", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i, tweet in enumerate(tweetCursor):
                if i % 1000 == 0:
                    if i == max_num:
                        break
                    #print(i)
                big_json = tweet._json
                if "retweeted_status" in big_json:
                    data = big_json["retweeted_status"]
                else:
                    data = big_json
                print(data)
                struct_data = compose_dict_obj(data, keys, search_words)
                print(str(i) + " created at:" + str(struct_data['created_at']))
                writer.writerow(struct_data)
    except IOError:
        print("I/O error")