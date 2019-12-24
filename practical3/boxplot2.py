#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df =[4,55,21,33,5,92,33,5,91,33,9,29,99,105,39,45,6,62,65,25,10,73,85,11,79,20,56,45,21,8,65,70,30]
print(df)


# In[3]:


sns.boxplot(data=df)


# In[5]:


print("minimum=",min(df));
print("maximum=",max(df));
n1=len(df);
print(n1);


# In[8]:


q1=(n1+1)*1/4
q2=(n1+1)*2/4
q3=(n1+1)*3/4
print(q1);
print(q2);
print(q3);


# In[11]:



fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(df)


# In[16]:


sns.boxplot(data=df)
ax = sns.swarmplot(data=df,color="red")


# In[ ]:




