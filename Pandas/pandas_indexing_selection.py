#!/usr/bin/env python
# coding: utf-8

# # Библиотека Pandas (Версия для Python 3)

# ## Data Frame

# In[73]:


import pandas as pd
import datetime


# In[51]:


#создание DataFrame с помощью чтения данных из файла
frame = pd.read_csv('data_sample_example.tsv', header=0, sep='\t')


# In[52]:


frame


# In[53]:


frame.dtypes


# In[54]:


#изменение типа столбца с помощью функции apply
frame.Birth = frame.Birth.apply(pd.to_datetime)


# In[55]:


frame


# In[56]:


frame.dtypes


# In[57]:


frame.info()


# In[58]:


#заполнение пропущенных значений с помощью метода fillna
frame.fillna('разнорабочий')


# In[59]:


#заполнение пропущенных значений с помощью метода fillna (inplace)
frame.fillna('разнорабочий', inplace=True)


# In[60]:


frame


# In[61]:


frame.Position


# In[62]:


frame[['Position']]


# In[63]:


frame[['Name', 'Position']]


# In[64]:


frame[:3] #выбираем первые три записи


# In[65]:


frame[-3:] #выбираем три послдение записи


# In[66]:


frame.loc[[0,1,2], ["Name", "City"]] #работает на основе имен


# In[67]:


frame.iloc[[1,3,5], [0,1]] #работает на основе позиций


# In[74]:


#выбираем строки, которые удовлетворяют условию frame.Birth >= pd.datetime(1985,1,1)
frame[frame.Birth >= pd.datetime(1985,1,1)]


# In[75]:


#выбираем строки, удовлетворяющие пересечению условий
frame[(frame.Birth >= pd.datetime(1985,1,1)) &
      (frame.City != 'Москва')]


# In[76]:


#выбираем строки, удовлетворяющие объединению условий
frame[(frame.Birth >= pd.datetime(1985,1,1)) |
      (frame.City == 'Волгоград')]


# In[ ]:




