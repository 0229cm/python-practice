#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[4]:


s1 = pd.Series([1, 2, 3])
s1


# In[5]:


s2 = pd.Series(['a', 'b', 'c'])
s2


# In[6]:


s3 = pd.Series(np.arange(200))
s3


# In[7]:


s4 = pd.Series([1, 2, 3], [100, 200, 300])
s4


# In[8]:


s5 = pd.Series([1, 2, 3], ['a', 'm', 'k'])
s5


# In[9]:


s6 = pd.Series(np.arange(5), np.arange(100, 105), dtype=np.int32)
s6


# In[10]:


s6.index


# In[11]:


s6.values


# In[12]:


s6[104]


# In[13]:


s6[104] = 70
s6


# In[14]:


s6[105] = 90
s6[200] = 80
s6


# In[15]:


s7 = pd.Series(np.arange(7), s6.index)
s7


# ## Series 함수 활용하여 데이터분석

# In[31]:


s = pd.Series([1, 1, 2, 1, 2, 2, 2, 1, 1, 3, 3, 4, 5, 5, 7, np.NaN])
s


# In[32]:


len(s)


# In[33]:


s.size


# In[34]:


s.shape


# In[35]:


s.unique()


# In[36]:


s.count()


# In[37]:


a = np.array([2, 2, 2, 2, np.NaN])
a.mean()

b = pd.Series(a)
b.mean()


# In[38]:


s.mean()


# In[39]:


s


# In[40]:


s.value_counts()


# In[47]:


s[[5, 7 ,8, 10]].value_counts()


# In[50]:


s.head(n=7)


# In[49]:


s.tail()


# In[51]:


s1 = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
s2 = pd.Series([6, 3, 2, 1], ['d', 'c', 'b', 'a'])

s1


# In[52]:


s2


# In[53]:


s1 + s2


# In[54]:


s1 ** 2


# In[55]:


s1 ** s2


# In[56]:


4 ** 6


# In[57]:


s1['k'] = 7
s2['e'] = 9


# In[58]:


s2


# In[59]:


s1 + s2


# ## Series boolean selection 활용

# In[60]:


s = pd.Series(np.arange(10), np.arange(10)+1)
s


# In[61]:


s > 5


# In[62]:


s[s>5]


# In[63]:


s [s % 2 == 0]


# In[64]:


s


# In[65]:


s.index > 5


# In[66]:


s[s.index > 5]


# In[70]:


s[(s > 5) & (s < 8)]


# In[71]:


(s >=7).sum()


# In[72]:


(s[s>=7]).sum()


# ## Series 데이터변경, 슬라이싱

# In[74]:


s = pd.Series(np.arange(100, 105), ['a', 'b', 'c', 'd', 'e'])
s


# In[75]:


s['a'] = 200
s


# In[76]:


s['k'] = 300
s


# In[79]:


s.drop('k', inplace=True)


# In[80]:


s


# In[82]:


s[['a', 'b']] = [300, 900]
s


# ## slicing

# In[83]:


s1 = pd.Series(np.arange(100, 105))
s1


# In[84]:


s1[1:3]


# In[87]:


s2 = pd.Series(np.arange(100, 105), ['a', 'c', 'b', 'd', 'e'])
s2


# In[88]:


s2[1:3]


# In[89]:


s2['c':'d']


# In[ ]:




