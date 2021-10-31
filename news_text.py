#!/usr/bin/env python
# coding: utf-8

# In[2]:


from newspaper import Article


# In[3]:


url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
article = Article(url)


# In[4]:


article.download()
article.parse()


# In[5]:


article.title


# In[8]:


text = article.text


# In[9]:


text


# In[14]:


text.replace("\n\n"," ")

