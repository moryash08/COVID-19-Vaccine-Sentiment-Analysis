import pandas as pd
import random

def getMainTweetData():
    print("Loading the dataset")
    # Database not made yet so we assume the file is directly loaded
    try:
        df_main = pd.read_csv('modified_english_india_tweets.csv')
    except Exception as e:
        df_main = pd.read_csv('modified_english_india_tweets.csv')

    print("Dataset loaded.")
    return df_main

def getLabelledTweetData():
    print("Loading the dataset")
    # Database not made yet so we assume the file is directly loaded
    try:
        df_labelled = pd.read_csv('labelled_tweets_compiled.csv')
    except Exception as e:
        df_labelled = pd.read_csv('labelled_tweets_compiled.csv')

    print("Dataset loaded.")
    return df_labelled

def splitData(df_main, df_labelled):
    print(df_main.shape[0])
    print(df_labelled.shape[0])
    # print(df_main.iloc[:]['full_text'].value_counts())
    # print(df_labelled.iloc[:]['full_text'].value_counts())

    for tweet in df_labelled['full_text']:
        df_main = df_main[df_main['full_text']!=tweet]
        
    return df_main

if __name__=="__main__":
    df_main = getMainTweetData()
    df_labelled = getLabelledTweetData()
    df = splitData(df_main, df_labelled)
    
    # Save the ordered dataset
    df.to_csv('final_tweets.csv')