#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
import nltk
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


path = "../Tweets CSV/final_labelled_set.csv"
dataset = pd.read_csv(path)


# In[3]:


dataset.head()


# In[4]:


dataset.shape


# In[5]:


nltk.downloader.download('vader_lexicon')


# In[6]:


from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer 


# In[7]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[8]:


x = dataset.drop(['full_text'], axis=1)
y = dataset['full_text']
y


# In[9]:


# Without Tokenization

scores = []
sia = SentimentIntensityAnalyzer()

for text in y:
    scores.append(sia.polarity_scores(text))
    
scores


# In[10]:


df = pd.DataFrame({'full_text': y, 'sentiment_vader': scores})
df


# In[11]:


# sentiment_vader = []

# for score in scores:
#     if score['compound'] >= 0.05:
#         sentiment_vader.append(1)
#     elif score['compound'] <= -0.05:
#         sentiment_vader.append(-1)
#     else:
#         sentiment_vader.append(0)
        
# sentiment_vader


# In[12]:


# sentiment_vader = []

# for score in scores:
#     if score['pos'] > score['neg'] and score['pos'] > score['neu']:
#         sentiment_vader.append(1)
#     elif score['neg'] > score['pos'] and score['neg'] > score['neu']:
#         sentiment_vader.append(-1)
#     else:
#         sentiment_vader.append(0)
        
# sentiment_vader


# In[13]:


sentiment_vader = []

for score in scores:   
    if score['compound'] >= 0.5:
        sentiment_vader.append(1)
    elif score['compound'] <= -0.5:
        sentiment_vader.append(-1)
    else:
        sentiment_vader.append(0)
        
sentiment_vader


# In[14]:


df['sentiments_vader'] = sentiment_vader


# In[15]:


df[(df['sentiments_vader']>-0.05) & (df['sentiments_vader']<0.05)]


# In[16]:


dataset = dataset.assign(sentiments_vader = df['sentiments_vader'].values)
dataset


# In[17]:


# dataset['sentiments_absa'].value_counts()


# In[19]:


dataset['sentiments_vader'].value_counts()


# In[20]:


dataset['sentiments'].value_counts()


# In[21]:


dataset.to_csv(path_or_buf="../Tweets CSV/labelled_tweets_vader_final.csv")


# In[ ]:




