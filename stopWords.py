#!/usr/bin/env python
# coding: utf-8

# In[76]:


para = """
    The greats never sacrifice the important for the urgent. 
    They handle the immediate problem and still make sure to secure the future. 
    You don’t think I understand what the fuck is going on? 
    You are all playing it safe for the quarter so you have a shot of personally being up on the year. 
    You are ALL SELFISH MOTHERFUCKERS looking to mitigate your downsides and protect your bonuses. 
    The only currency that this firm has…that any firm has these days…is it’s winning streak. 
    The kevlar of knowing the answer. You break that, you break the whole thing. 
    Nobody leaves here until you hand me an idea that I can shock the world with in a few days time!
"""


# In[77]:


from nltk.stem import PorterStemmer


# In[78]:


from nltk.corpus import stopwords


# In[79]:


stopwords.words('english')


# In[80]:


stemmer = PorterStemmer()


# In[81]:


import nltk


# In[82]:


sents = nltk.sent_tokenize(para)


# In[83]:


"""
for i in range(len(sents)):
    words = nltk.word_tokenize(sents[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sents[i] = ' '.join(words)
"""


# In[84]:


sents


# In[85]:


from nltk.stem import SnowballStemmer


# In[86]:


snowball = SnowballStemmer('english')


# In[87]:


"""
for i in range(len(sents)):
    words = nltk.word_tokenize(sents[i])
    words = [snowball.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sents[i] = ' '.join(words)
"""


# In[88]:


sents


# In[89]:


from nltk.stem import WordNetLemmatizer


# In[95]:


lemmatizer = WordNetLemmatizer()


# In[98]:


for i in range(len(sents)):
    words = nltk.word_tokenize(sents[i])
    words = [lemmatizer.lemmatize(word,pos='v') for word in words if word not in set(stopwords.words('english'))]
    sents[i] = ' '.join(words)


# In[99]:


sents


# In[ ]:





# In[ ]:




