#!/usr/bin/env python
# coding: utf-8

# ## dataframe data

# In[2]:


import pandas as pd


# In[3]:


# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
train_data = pd.read_csv('./train.csv')


# In[5]:


train_data.head(n=3)


# In[8]:


train_data.tail()


# In[9]:


train_data.shape


# In[10]:


train_data.describe()


# In[11]:


train_data.info()


# In[12]:


train_data.index


# In[13]:


data = {'a':100, 'b':200, 'c':300}
pd.DataFrame(data, index=['x','y','z'])


# In[14]:


data = {'a':[1,2,3], 'b':[4,5,6], 'c':[10,11,12]}
pd.DataFrame(data, index=[0,1,2])


# In[18]:


a = pd.Series([100,200,300], ['a','b','d'])
b = pd.Series([101,201,301], ['a','b','k'])
c = pd.Series([110,210,310], ['a','b','c'])

pd.DataFrame([a, b, c], index=[100,101,102])


# ## csv 데이테로부터 dataframe 생성

# In[19]:


train_data = pd.read_csv('./train.csv')
train_data.head()


# In[20]:


train_data = pd.read_csv('./train.csv', index_col='PassengerId', usecols=['PassengerId', 'Survived', 'Pclass', 'Name'])
train_data


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




