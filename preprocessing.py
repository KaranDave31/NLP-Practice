#!/usr/bin/env python
# coding: utf-8

# # TOKENIZATION

# In[45]:


from nltk.tokenize import sent_tokenize


# In[6]:


corpus = """hello there.
general kenobi.
anakin skywalker is no more"""


# In[7]:


print(corpus)


# In[8]:


sent_tokenize(corpus)


# In[9]:


from nltk.tokenize import word_tokenize


# In[10]:


word_tokenize(corpus)


# In[11]:


from nltk.tokenize import wordpunct_tokenize


# In[12]:


wordpunct_tokenize(corpus)


# In[13]:


from nltk.tokenize import TreebankWordTokenizer


# In[14]:


tokenzier = TreebankWordTokenizer()


# In[16]:


tokenzier.tokenize(corpus)


# # STEMMING

# In[19]:


##porterstemmer

from nltk.stem import PorterStemmer


# In[57]:


arr = ["eating","eats","ate","writing","writes","programs"]


# In[28]:


port = PorterStemmer()


# In[31]:


for word in arr :
    print(word + "=" + porter.stem(word))


# In[33]:


##regexpstemmer
from nltk.stem import RegexpStemmer


# In[34]:


regStem = RegexpStemmer('ing$|s$|e$|able$',min=5)


# In[37]:


regStem.stem('flying')


# In[40]:


regStem.stem('eats')


# In[41]:


##snowball stemmer

from nltk.stem import SnowballStemmer


# In[42]:


snowStem = SnowballStemmer('english')


# In[44]:


for word in arr:
    print(word + "=" + snowStem.stem(word))


# # LEMMATIZATION

# In[47]:


##wordnet lemmatizer
from nltk.stem import WordNetLemmatizer


# In[48]:


lemma = WordNetLemmatizer()


# In[54]:


lemma.lemmatize("going",pos='n')


# In[52]:


##nltk.download('wordnet')


# In[55]:


lemma.lemmatize("going",pos='v')


# In[60]:


for word in arr:
    print(word + "=" + lemma.lemmatize(word,pos='n'))


# In[61]:


for word in arr:
    print(word + "=" + lemma.lemmatize(word,pos='v'))


# In[ ]:




