#!/usr/bin/env python
# coding: utf-8

# In[94]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from datetime import datetime
import re
df = pd.read_csv('labelled_set8.csv').drop('Unnamed: 0',axis=1)


# In[83]:


cases_phrases = ['spark in cases','fresh cases','cluster of cases','spike in cases','cases rise','cluster detected',
                'cluster of cases','rise in cases','case rise','cases of covid are increasing','increase in cases',
                'increase in corona cases','increase in covid cases','increase in covid-19 cases','cases of coronavirus are increasing']
cases_phrases = ['coronavirus, coronavirus updates, covid-19','coronavirus updates','covid updates','coronavirus tracker','covid tracker'
                'covid-19 tracker']


# In[84]:


indexes = []
for i in range(0,len(df)):
    for phrase in cases_phrases:
        if phrase in df.iloc[i]['full_text']:
            indexes.append(i)
            break
print(len(indexes))


# In[85]:


final_df = pd.read_csv('english_final.csv')


# In[86]:


final_df['sentiments_absa'].value_counts()


# In[87]:


negative_df = final_df[final_df['sentiments_absa'] == -1]
positive_df = final_df[final_df['sentiments_absa'] == 1]
neutral_df = final_df[final_df['sentiments_absa'] == 0]


# In[88]:


fig, ax = plt.subplots(figsize=(16,5), nrows=1, ncols=3)
ax[0].hist(negative_df['retweet_count'])
ax[1].hist(positive_df['retweet_count'])
ax[2].hist(neutral_df['retweet_count'])
plt.show()


# In[89]:


fig, ax = plt.subplots(figsize=(16,5), nrows=1, ncols=3)
ax[0].hist(negative_df['favorite_count'])
ax[1].hist(positive_df['favorite_count'])
ax[2].hist(neutral_df['favorite_count'])
plt.show()


# In[90]:


print(negative_df['user_followers_count'].sum())
print(neutral_df['user_followers_count'].sum())
print(positive_df['user_followers_count'].sum())


# In[91]:


sns.barplot(x='sentiments_absa',y='user_followers_count',data=final_df)


# In[92]:


sns.barplot(x='sentiments_absa',y='favorite_count',data=final_df)


# In[78]:


final_df.iloc[0]['created_at']


# In[93]:


dtime='Tue Mar 02 14:37:15 +0000 2021'
new_datetime = datetime.strftime(datetime.strptime(dtime,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')
print((new_datetime))


# In[95]:


re.findall(re.compile('\d{4}-\d{2}-\d{2}'),'Tue Mar 02 14:37:15 +0000 2021')


# In[ ]:




