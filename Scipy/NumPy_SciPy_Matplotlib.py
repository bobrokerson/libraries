#!/usr/bin/env python
# coding: utf-8

# # NumPy, SciPy и Matplotlib (Python 3)

# ## Numpy

# In[6]:


import numpy as np


# In[9]:


x = [2, 3, 4, 6]
y = np.array(x)


# In[11]:


print(type(x), x)
print(type(y), y)


# In[9]:


print(x[1:3])


# In[10]:


print(y[1:3])


# ### failing

# In[12]:


print(x[[0, 2]])


# In[13]:


print(y[[0, 2]])


# In[16]:


print(y[y>3])


# In[19]:


print(x * 5)


# In[21]:


print(y * 5)


# In[22]:


print(x ** 2)


# In[23]:


print(y ** 2)


# In[29]:


matrix = [[1, 2, 4], [3, 1, 0]]
nd_array = np.array(matrix)


# In[30]:


print(matrix[1][2])


# In[31]:


print(nd_array[1, 2])


# In[32]:


print(np.random.rand())


# In[33]:


print(np.random.randn())


# In[35]:


print(np.random.randn(4))


# In[36]:


print(np.random.randn(4, 5))


# In[37]:


print(np.arange(0, 8, 0.1))


# In[38]:


print(range(0, 8, 0.1))


# In[39]:


get_ipython().run_line_magic('timeit', 'np.arange(0, 10000)')
get_ipython().run_line_magic('timeit', 'range(0, 10000)')


# ## SciPy

# In[44]:


from scipy import optimize


# In[45]:


def f(x):
    return (x[0] - 3.2) ** 2 + (x[1] - 0.1) ** 2 + 3

print(f([3.2, 0.1]))


# In[46]:


x_min = optimize.minimize(f, [5, 5])
print(x_min)


# In[47]:


print(x_min.x)


# In[48]:


from scipy import linalg


# In[49]:


a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

x = linalg.solve(a, b)
print(x)


# In[50]:


print(np.dot(a, x))


# In[51]:


X = np.random.randn(4, 3)
U, D, V = linalg.svd(X)
print(U.shape, D.shape, V.shape)
print(type(U), type(D), type(V))


# ## Matplotlib

# In[52]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[53]:


from matplotlib import pylab as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()


# In[54]:


x = np.arange(-10, 10, 0.1)
y = x ** 3
plt.plot(x, y)
plt.show()


# ## Все вместе

# In[55]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


# In[56]:


x = np.arange(0, 10, 2)
y = np.exp(-x/3.0) + np.random.randn(len(x)) * 0.05

print(x[:5])
print(y[:5])


# In[57]:


f = interpolate.interp1d(x, y, kind='quadratic')
xnew = np.arange(0, 8, 0.1)
ynew = f(xnew)


# In[58]:


plt.plot(x, y, 'o', xnew, ynew, '-')
plt.show()

