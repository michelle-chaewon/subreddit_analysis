#!/usr/bin/env python
# coding: utf-8

# In[11]:


import psraw
import praw
import pandas as pd
import os
import glob
import shutil
import numpy as np


# In[ ]:


#author: Michelle Chaewon Bak


# In[24]:


os.chdir(r"C:\Users\Michelle\Desktop\reddit data")


# In[15]:


# Reddit API Credentials
client_id = "ekZHFlYSzRD8zg"               
client_secret = ""           
user_agent = "reddit_scraper1"               
username = "michelle9820"      
password = ""


# In[18]:


reddit = praw.Reddit(client_id=client_id, 
                     client_secret=client_secret, password=password,
                     user_agent=user_agent, username=username)


# In[19]:


subreddit_list = ['traumatoolbox', 'ptsd', 'PTSDcombat', 'CPTSD', 'CPTSDFightMode', 'CPTSDNextSteps']

for name in subreddit_list:
    os.mkdir(os.path.join(r'C:\Users\Michelle\Desktop\reddit data', name))


# In[20]:


def scraper(subreddit_name, category):
    os.chdir(os.path.join(r'C:\Users\Michelle\Desktop\reddit data', subreddit_name))
    
    posts = []
    subreddit = reddit.subreddit(subreddit_name)
    if category == "hot":
        for post in subreddit.hot(limit=10000):
            if not post.stickied:
                posts.append([post.title, post.selftext])
        posts = pd.DataFrame(posts,columns=['title', 'text'])
        posts.to_csv(subreddit_name + '_' + category + '.csv', index=False)
        
    elif category == "rising":
        for post in subreddit.rising(limit=10000):
            if not post.stickied:
                posts.append([post.title, post.selftext])
        posts = pd.DataFrame(posts,columns=['title', 'text'])
        posts.to_csv(subreddit_name + '_' + category + '.csv', index=False)
        
    elif category == "controversial":
        for post in subreddit.controversial(limit=10000):
            if not post.stickied:
                posts.append([post.title, post.selftext])
        posts = pd.DataFrame(posts,columns=['title', 'text'])
        posts.to_csv(subreddit_name + '_' + category + '.csv', index=False)
        
    elif category == "new":
        for post in subreddit.new(limit=10000):
            if not post.stickied:
                posts.append([post.title, post.selftext])
        posts = pd.DataFrame(posts,columns=['title', 'text'])
        posts.to_csv(subreddit_name + '_' + category + '.csv', index=False)
        
    elif category == "top":
        for post in subreddit.top(limit=10000):
            if not post.stickied:
                posts.append([post.title, post.selftext])
        posts = pd.DataFrame(posts,columns=['title', 'text'])
        posts.to_csv(subreddit_name + '_' + category + '.csv', index=False)


# In[22]:


for name in subreddit_list:
    scraper(name, 'hot')
    scraper(name, 'rising')
    scraper(name, 'controversial')
    scraper(name, 'new')
    scraper(name, 'top')


# In[30]:


file_list = glob.glob("*/*.csv")


# In[34]:


def title_to_text(csv_title):
    df = pd.read_csv(csv_title)
#     df.text.fillna(df.title, inplace=True)
    df.title = df.title.map(str) + '. '
    df.text = df.title.map(str) + df.text.map(str)
    df = df[['text']]
    df.to_csv(csv_title, index = False)
    
for f in file_list:
    file_path = os.path.join(r"C:\Users\Michelle\Desktop\reddit data", f)
    title_to_text(file_path)


# In[35]:


def remove_duplicate_and_non_letter(csv_title): 
    df = pd.read_csv(csv_title)
    df.drop_duplicates(subset="text", inplace=True)
    df = df[df['text'].str.contains('[A-Za-z]')]
    df.to_csv(csv_title, index=False)
    
for f in file_list:
    file_path = os.path.join(r"C:\Users\Michelle\Desktop\reddit data", f)
    remove_duplicate_and_non_letter(f)


# In[43]:


def filter_dream_nightmare(csv_original, words):
    df = pd.read_csv(csv_original)
    df = df[df['text'].str.contains(words)]

    df.to_csv(csv_original, index=False)
    
# filter_dream_nightmare("trauma_filtered.csv", "trauma_filtered.csv", "dream|nightmare")


# In[ ]:





# In[ ]:




