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

def orderData(df):
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

    # print(tweet_dates)
    # dates = dict.fromkeys(set(tweet_dates), [])
    # print(dates)
    
    # print(len(df[df['created_at']=='Feb 22']['full_text'])) = 129 (lowest)

    df2 = pd.DataFrame()

    for date in set(tweet_dates):
        tweet_count = 140
        if date == 'Feb 22':
            tweet_count = 120
        df2 = df2.append(other=df[df['created_at']==date].sample(n=tweet_count), ignore_index=True)
        
        # dates[date].append(random.sample(list(df[df['created_at']==date]['full_text']), tweet_count))

    print(df2.shape[0])
    # print(dates)
    # print(type(tweet_dates[0]))
    # print(tweet_dates[0])
    return df2

if __name__=="__main__":
    df = getTweetData()
    df = orderData(df)
    
    # Save the ordered dataset
    df.to_csv('ordered_english_tweets.csv')