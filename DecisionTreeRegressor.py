#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


df=pd.read_csv('Data/Real-Data/Real_Combine.csv')


# In[10]:


df.head()


# In[11]:


df=df.dropna()


# In[12]:


X=df.iloc[:,:-1] ## independent features
y=df.iloc[:,-1] ## dependent features


# In[13]:


X.isnull()


# In[14]:


sns.pairplot(df)


# In[15]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


# In[16]:


from sklearn.tree import DecisionTreeRegressor


# In[17]:


dtree=DecisionTreeRegressor(criterion='mse')


# In[18]:


dtree.fit(X_train,y_train)


# In[19]:


print("Coefficient of determination R^2 <-- on train set: {}".format(dtree.score(X_train, y_train)))


# In[20]:


print("Coefficient of determination R^2 <-- on test set: {}".format(dtree.score(X_test, y_test)))


# In[21]:


from sklearn.model_selection import cross_val_score
score=cross_val_score(dtree,X,y,cv=5)


# In[22]:


score


# In[ ]:




