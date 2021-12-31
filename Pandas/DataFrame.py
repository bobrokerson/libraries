#!/usr/bin/env python
# coding: utf-8

# # Библиотека Pandas

# ## Data Frame

# In[2]:


import pandas as pd


# In[3]:


#создание DataFrame по столбцам с помощью словарей
frame = pd.DataFrame({'numbers':range(10), 'chars':['a']*10})


# In[4]:


frame


# In[5]:


#создание DataFrame с помощью чтения данных из файла
frame = pd.read_csv('dataset.tsv', header=0, sep='\t')


# In[6]:


frame


# In[7]:


frame.columns


# In[8]:


frame.shape


# In[9]:


new_line = {'Name':'Perov', 'Birth':'22.03.1990', 'City':'Penza'}


# In[10]:


#добавление строки в DataFrame
frame.append(new_line, ignore_index=True)


# In[11]:


#добавление строки в DataFrame
frame = frame.append(new_line, ignore_index=True)


# In[12]:


frame


# In[13]:


#добавление столбца в DataFrame
frame['IsStudent'] = [False]*5 + [True]*2


# In[14]:


frame


# In[15]:


#удаление строк DataFrame
frame.drop([5,6], axis=0)


# In[16]:


frame


# In[17]:


#удаление строк DataFrame (inplace)
frame.drop([5,6], axis=0, inplace=True)


# In[18]:


frame


# In[19]:


#удаление столбца DataFrame (inplace)
frame.drop('IsStudent', axis=1, inplace=True)


# In[20]:


frame


# In[21]:


#запись DataFrame в файл
frame.to_csv('updated_dataset.csv', sep=',', header=True, index=False)


# In[22]:


get_ipython().system('cat updated_dataset.csv')


# In[ ]:




