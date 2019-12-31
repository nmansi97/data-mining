#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random;
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans


# In[7]:


l1=[90,76,23,11,10];
print(l1);


# In[8]:


print("simple random sampling without replacement");
print(random.sample(l1,k=2));


# In[9]:


print("simple random sampling with replacement");
print(random.choices(l1,k=3));


# In[28]:


data = pd.read_csv('exams.csv',usecols = ['mathscore'])
a=data.mathscore.tolist()
print(data)
lst1=[];
lst2=[];
lst3=[];
for mathscore in a:
    if mathscore > 60:
        lst1.append(mathscore);
    elif mathscore > 50 and mathscore <= 60:
        lst2.append(mathscore);
    else:
        lst3.append(mathscore);
print("greater than 60 marks");
print(lst1);
print("greater than 50 marks nad less than or equal 60 marks");
print(lst2);
#ll=[lst1,lst2,lst3];
#print(random.choices(ll));



# In[ ]:





# In[ ]:





# In[ ]:




