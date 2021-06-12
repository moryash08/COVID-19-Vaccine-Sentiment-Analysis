import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import aspect_based_sentiment_analysis as absa
import pandas as pd
import threading

#The value in BoundedSemaphore decides the number of threads(windows) which can simultaneously run.
lock = threading.BoundedSemaphore(8)

df = pd.read_csv('final_tweets.csv')
target_col = 'sentiments_absa'
df[target_col] = 20
classified = []
nlp = absa.load()
def classify(num1, num2, df):
    
    for i in range(num1, num2, 1):
        try:
            lock.acquire()
            text = df.iloc[i]['full_text'] #+ '.'
            completed_task = nlp(text=text,aspects=['vaccine covid-19 vaccines vaccination abusive vaccinations covaxin astra-zeneca astrazeneca covishield inoculation jab pfizer cowin co-vaxin biotech','safety'])#'shot taken dose efficacy safety'])#'safety'])
            vaccine, safety = completed_task.examples
            
            if vaccine.sentiment == absa.Sentiment.negative:
                df.at[i,target_col] = -1
            elif vaccine.sentiment == absa.Sentiment.positive:
                df.at[i,target_col] = 1
            elif vaccine.sentiment == absa.Sentiment.neutral:
                df.at[i,target_col] = 0
            classified.append(i)
            print("No of tweets classified: " + str(len(classified)))
            lock.release()
        except:
            print("Exception in classify method")

thread_array = []
#Used to allocate the number of tweets to each thread. The value of denominator can be adjusted as needed.
step = round(len(df) / 400, ndigits=None)
for i in range(0, len(df), step):
    if (i != 0):
        i += 1
    if (i + step < len(df)):
        t = threading.Thread(target=classify, args=(i, i + step, df,))
    else:
        t = threading.Thread(target=classify, args=(i, i + len(df) % step - 1, df,))
    thread_array.append(t)
for i in thread_array:
    i.start()
for i in thread_array:
    i.join()

df.to_csv('labelled_set9.csv',index=False,encoding='utf-8')