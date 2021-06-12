import pandas as pd
import random

def getTweetData():
    print("Loading the dataset")
    # Database not made yet so we assume the file is directly loaded
    try:
        df = pd.read_csv('final_tweets.csv')
    except:
        df = pd.read_csv('final_tweets.csv')

    print("Dataset loaded.")
    return df

def getDates(df):
    total_rows = df.shape[0]
    tweet_dates_full = df['created_at']
    tweet_dates = []
    index = 0
    
    for date in tweet_dates_full:
        month_date_list = date.split(' ')
        month_date = ' '.join(month_date_list[1:3])
        tweet_dates.append(month_date)
        df.loc[index, 'created_at'] = month_date
        index+=1

    print(set(tweet_dates))

    return set(tweet_dates)

def getFebTweets(df, tweet_dates):

    df_feb = pd.DataFrame()

    for date in tweet_dates:
        if date.split(' ')[0] == 'Feb':
            df_feb = df_feb.append(other=df[df['created_at']==date], ignore_index=True)
        
        # dates[date].append(random.sample(list(df[df['created_at']==date]['full_text']), tweet_count))

    print(df_feb.shape[0])
    
    return df_feb

def getMarTweets(df, tweet_dates):

    df_mar = pd.DataFrame()

    for date in set(tweet_dates):
        if date.split(' ')[0] == 'Mar':
            df_mar = df_mar.append(other=df[df['created_at']==date], ignore_index=True)
        
        # dates[date].append(random.sample(list(df[df['created_at']==date]['full_text']), tweet_count))

    print(df_mar.shape[0])
    
    return df_mar

if __name__=="__main__":
    df = getTweetData()
    tweet_dates = getDates(df)

    df_feb = getFebTweets(df, tweet_dates)
    df_mar = getMarTweets(df, tweet_dates)
    
    # Save the ordered dataset
    df_feb.to_csv('final_tweets_feb.csv')
    df_mar.to_csv('final_tweets_mar.csv')