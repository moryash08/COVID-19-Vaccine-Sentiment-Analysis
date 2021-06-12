#!/usr/bin/env python
# coding: utf-8

# In[21]:


get_ipython().system('pip install textblob')


# In[22]:


from textblob import TextBlob

def sentiment_analysis(tweet):
    def getSubjectivity(text):
        return TextBlob(text).sentiment.subjectivity
  
    #Create a function to get the polarity
    def getPolarity(text):
        return TextBlob(text).sentiment.polarity
  
    #Create two new columns ‘Subjectivity’ & ‘Polarity’
    tweet['TextBlob_Subjectivity'] = tweet['tweet'].apply(getSubjectivity)
    tweet['TextBlob_Polarity'] = tweet['tweet'].apply(getPolarity)
    
    def getAnalysis(score):
        if score < 0:
            return 'Negative'
        elif score == 0:
            return 'Neutral'
        else:
            return 'Positive'
        tweet['TextBlob_Analysis'] = tweet['TextBlob_Polarity'].apply(getAnalysis)

    return tweet


# In[23]:


import pandas as pd
df = pd.read_csv('../Tweets CSV/final_labelled_set.csv')
df


# In[24]:


test = TextBlob("The movie was good!")
print(test.sentiment)


# In[25]:


sentiment_textblob = []

for text in df['full_text']:
    blob = TextBlob(text)
    if blob.sentiment.polarity >= 0.3:
        sentiment_textblob.append(1)
    elif blob.sentiment.polarity <= -0.3:
        sentiment_textblob.append(-1)
    else:
        sentiment_textblob.append(0)
        
sentiment_textblob


# In[26]:


df['sentiments_textblob'] = sentiment_textblob


# In[27]:


df['sentiments'].value_counts()


# In[28]:


df['sentiments_absa'].value_counts()


# In[29]:


df['sentiments_textblob'].value_counts()


# In[30]:


df.to_csv(path_or_buf="../Tweets CSV/labelled_tweets_textblob_new.csv")


# In[31]:


df2 = pd.read_csv("../Tweets CSV/labelled_tweets_vader_final.csv")


# In[32]:


df2 = df2.assign(sentiments_textblob = df['sentiments_textblob'].values)


# In[ ]:


df2.to_csv(path_or_buf="../Tweets CSV/labelled_tweets_compiled.csv")


# In[ ]:




