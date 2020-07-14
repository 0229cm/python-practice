#!/usr/bin/env python
# coding: utf-8

# In[130]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


x = np.array([1, 2, 3])
y = np.array([2, 4, 6])

plt.plot(x, y)


# In[8]:


x = np.array([1, 2, 3, 4])
print(x)

y = np.array([[2, 3, 4], [1, 2, 5]])
print(y)

print(type(y))


# In[9]:


np.arange(10)


# In[10]:


np.arange(1, 10)


# In[11]:


np.arange(1, 10, 2)


# In[12]:


np.arange(5, 101, 5)


# In[13]:


np.ones((4, 5))


# In[14]:


np.ones((2, 3, 4))


# In[15]:


np.zeros((2, 3 ,8 ,8))


# In[22]:


np.empty((3, 5))


# In[23]:


np.full((3, 4, 2), 7)


# In[26]:


np.eye(3)


# In[27]:


np.linspace(1, 10, 3)


# In[28]:


np.linspace(1, 10, 4)


# In[29]:


np.linspace(1, 10, 5)


# In[34]:


x = np.arange(1, 16)
print(x)

x.shape

x.reshape(5, 3, 1)


# In[35]:


import numpy as np


# In[40]:


np.random.rand(4, 5, 3)


# In[42]:


np.random.randn(3, 4, 2)


# In[43]:


np.random.randn(5)


# In[44]:


np.random.randint(1, 100, size=(3,5))


# In[56]:


np.random.seed(100)
np.random.randn(3, 4)


# In[57]:


np.random.choice(100, size=(3, 4))


# In[67]:


x = np.array([1, 2, 3, 1.5, 2.6, 4.9])
np.random.choice(x, size=(2, 2), replace=False)


# In[68]:


np.random.uniform(1.0, 3.0, size=(4,5))


# In[72]:


np.random.uniform(size=(3,4))
np.random.randn(3, 4)


# In[3]:


x = np.arange(10)
print(x)


# In[4]:


x[3] = 100
print(x)


# In[6]:


x = np.arange(10).reshape(2, 5)
print(x)


# In[11]:


x[1,2]


# In[12]:


x[0]


# In[13]:


x = np.arange(36).reshape(3, 4, 3)
print(x)


# In[14]:


x[0]


# In[15]:


x[1, 2]


# In[16]:


x[1, 2, 1]


# In[17]:


x = np.arange(10)
print(x)


# In[18]:


x[1:7]


# In[19]:


x = np.arange(10).reshape(2, 5)
print(x)


# In[21]:


x[:,:2]


# In[22]:


x = np.arange(54).reshape(2, 9, 3)
print(x)


# In[24]:


x[:1, :2, :]


# In[26]:


x[0, :2, :]


# ## ndarray

# In[27]:


x = np.arange(15).reshape(3, 5)
print(x)


# In[29]:


np.ravel(x)


# In[28]:


x.ravel()


# In[30]:


temp = x.ravel()
print(temp)


# In[31]:


temp[0] = 100
print(temp)
print(x)


# In[33]:


y = np.arange(15).reshape(3, 5)
print(y)


# In[34]:


t2 = y.flatten()
print(t2)


# In[37]:


t2 = y.flatten(order='F')
print(t2)


# In[35]:


t2[0] = 100
print(t2)
print(y)


# In[38]:


x = np.arange(30).reshape(2, 3, 5)
print(x)


# In[39]:


x.ravel()


# In[42]:


x = np.arange(36)
print(x)
print(x.shape)
print(x.ndim)


# In[43]:


x.reshape(6, 6)


# In[45]:


x.reshape(6, -1)


# In[46]:


y = np.arange(36)
print(y)
print(y.shape)
print(y.ndim)


# In[47]:


y = x.reshape(6, 6)
print(y.shape)
print(y.ndim)


# In[48]:


k = x.reshape(3, 3, 4)
print(k)
print(k.shape)
print(k.ndim)


# ## numpy 기본함수

# In[49]:


x = np.arange(15).reshape(3, 5)
y = np.random.rand(15).reshape(3, 5)
print(x)
print(y)


# In[50]:


np.add(x, y)


# In[51]:


x + y


# In[52]:


print(y)


# In[53]:


np.mean(y)


# In[54]:


y.mean()


# In[55]:


np.max(y)


# In[56]:


np.argmax(y)


# In[57]:


np.var(y), np.median(y), np.std(y)


# In[58]:


np.cumsum(y)


# In[63]:


np.sum(y, axis=None)


# In[65]:


z = np.random.randn(10)
print(z)


# In[66]:


np.any(z > 0)


# In[68]:


z > 0


# In[67]:


np.all(z > 0)


# In[70]:


z = np.random.randn(10)
print(z)


# In[73]:


np.where(z > 0, z, 0)


# ## axis

# In[74]:


x = np.arange(15)
print(x)


# In[76]:


np.sum(x, axis=0)


# In[82]:


y = x.reshape(3, 5)
print(y)

np.sum(y, axis=0)


# In[81]:


y = x.reshape(3, 5)
print(y)

np.sum(y, axis=1)


# In[84]:


z = np.arange(36).reshape(3, 4, 3)
print(z)

np.sum(z, axis=0)


# In[85]:


z = np.arange(36).reshape(3, 4, 3)
print(z)

np.sum(z, axis=1)


# In[86]:


np.sum(z, axis=2)


# In[87]:


np.sum(z, axis=-1)


# In[88]:


print(z)


# In[90]:


np.sum(z, axis=(0, 2))


# ## 브로드캐스팅

# In[91]:


x = np.arange(15).reshape(3, 5)
y = np.random.rand(15).reshape(3, 5)
print(x)
print(y)


# In[92]:


x + y


# In[93]:


x + 2


# In[102]:


a = np.arange(12).reshape(4, 3)
b = np.arange(100, 103)
c = np.arange(1000, 1004)
d = b.reshape(1, 3)

print(a.shape)
print(b.shape)
print(c.shape)
print(d.shape)
print(d)


# In[98]:


a + b


# In[103]:


a + d


# ## Boolean indexing

# In[105]:


x = np.random.randint(1, 100, size = 10)
print(x)


# In[109]:


even_mask = x % 2 == 0
print(even_mask)


# In[108]:


x[even_mask]


# In[111]:


x[x % 2 == 0]


# In[113]:


x[x > 30]


# In[114]:


x % 2 == 0
x < 30

x[x % 2 == 0 & (x < 30)]


# In[116]:


x < 30
x > 50

x[x < 30 | (x > 50)]


# In[117]:


temp = np.array(
        [23.9, 24.4, 24.1, 25.4, 27.6, 29.7,
         26.7, 25.1, 25.0, 22.7, 21.9, 23.6, 
         24.9, 25.9, 23.8, 24.7, 25.6, 26.9, 
         28.6, 28.0, 25.1, 26.7, 28.1, 26.5, 
         26.3, 25.9, 28.4, 26.1, 27.5, 28.1, 25.8])


# In[118]:


len(temp)


# In[119]:


len(temp[temp > 25.0])


# In[120]:


np.sum(temp > 25.0)


# In[122]:


np.mean(temp[temp > 25.0])


# ## linalg

# In[125]:


x = np.random.rand(3, 3)
print(x)

x @ np.linalg.inv(x)


# In[126]:


x = np.random.rand(3, 3)
print(x)

np.matmul(x, np.linalg.inv(x))


# In[129]:


A = np.array([[1, 1], [2, 4]])
B = np.array([25, 64])

x = np.linalg.solve(A, B)
print(x)

np.allclose(A@x, B)


# ## matplotlib

# In[131]:


x = np.linspace(0, 10, 11)
y = x ** 2 + x + 2 + np.random.randn(11)

print(x)
print(y)


# In[132]:


plt.plot(x, y)


# In[133]:


plt.scatter(x, y)


# In[137]:


plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('X-Y relation')
plt.plot(x, y)


# In[138]:


plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('X-Y relation')
plt.grid(True)
plt.plot(x, y)


# In[140]:


plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('X-Y relation')
plt.grid(True)

plt.xlim(0, 20)
plt.ylim(0, 200)

plt.plot(x, y)


# In[143]:


plt.plot(x, y, 'r')


# In[144]:


plt.plot(x, y, '-.')


# In[145]:


plt.plot(x, y, 'g^')


# In[146]:


plt.plot(x, y, 'm:')


# In[148]:


plt.plot(x, y, 'm:', linewidth=9)


# In[149]:


plt.plot(x, y , color='black',
         linestyle='--', marker='^',
        markerfacecolor='blue', markersize=6)


# In[150]:


plt.subplot(2, 2, 1)
plt.plot(x, y, 'r')

plt.subplot(2, 2, 2)
plt.plot(x, y, 'g')

plt.subplot(2, 2, 3)
plt.plot(y, x, 'k')

plt.subplot(2, 2, 4)
plt.plot(x, np.exp(x), 'b')


# ## hist 함수

# In[152]:


data = np.random.randint(1, 100, size = 200)
print(data)


# In[154]:


plt.hist(data, bins = 20, alpha=0.3)
plt.xlabel('값')
plt.ylabel('개수')
plt.grid(True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




