#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# In[3]:


data={'x': [1.0,1.5,3.0,5.0,3.5,4.5,3.5],
     'y':[1.0,2.0,4.0,7.0,5.0,5.0,4.5]}
df = DataFrame(data,columns=['x','y'])
print (df)


# In[13]:


f = DataFrame(data,columns=['x','y'])
  
kmeans = KMeans(n_clusters=4).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=100, alpha=0.8)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)


# In[ ]:




