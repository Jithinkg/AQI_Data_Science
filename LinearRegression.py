#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[3]:


df=read_csv.read('Data/Real-Data/Real_Combine.csv')


# In[4]:


df=read_csv.read('Data/Real-Data/Real_Combine.csv')


# In[6]:


df=pd.read_csv('Data/Real-Data/Real_Combine.csv')


# In[7]:


df.isnull()


# In[13]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=True,cmap='viridis')


# In[16]:


X=df.iloc[:,:-1]
y=df.iloc[:,-1]


# In[18]:


X
Y


# In[19]:


y


# In[20]:


y.isnull()


# In[21]:


df.corr()


# In[23]:


import seaborn as sns
sns.distplot(y)


# In[56]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=0)


# In[60]:


from sklearn.linear_model import LinearRegression


# In[58]:


regressor=LinearRegression()
regressor.fit(X_train,y_train)
print("coeff of detr R^2  :{}".format(regressor.score(X_train,y_train)))


# In[51]:


from sklearn.linear_model import LinearRegression


# In[61]:


df.dropna()


# In[62]:


regressor=LinearRegression()
regressor.fit(X_train,y_train)
print("coeff of detr R^2  :{}".format(regressor.score(X_train,y_train)))


# In[ ]:




