#!/usr/bin/env python
# coding: utf-8

# # Решение оптимизационных задач в SciPy (Python 3)

# In[1]:


from scipy import optimize


# In[1]:


def f(x):   # The rosenbrock function
    return .5*(1 - x[0])**2 + (x[1] - x[0]**2)**2
    
print(f([1, 1]))


# In[3]:


result = optimize.brute(f, ((-5, 5), (-5, 5)))
print(result)


# In[4]:


print(optimize.differential_evolution(f, ((-5, 5), (-5, 5))))


# In[5]:


import numpy as np

def g(x):
        return np.array((-2*.5*(1 - x[0]) - 4*x[0]*(x[1] - x[0]**2), 2*(x[1] - x[0]**2)))


# In[6]:


print(optimize.check_grad(f, g, [2, 2]))


# In[7]:


print(optimize.fmin_bfgs(f, [2, 2], fprime=g))


# In[8]:


print(optimize.minimize(f, [2, 2]))


# In[9]:


print(optimize.minimize(f, [2, 2], method='BFGS'))


# In[10]:


print(optimize.minimize(f, [2, 2], method='Nelder-Mead'))

