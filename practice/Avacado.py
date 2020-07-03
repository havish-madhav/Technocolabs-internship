#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:/Users/hp/Desktop/avocado.csv")


# In[3]:


#printing the dataframe
df


# In[4]:


df.head()


# In[5]:


df.head(3)


# In[6]:


#first five rows of averageprice column
df['AveragePrice'].head()


# In[7]:


#seperate dataframe for albny region
albany_df = df[df['region']=="Albany"]


# In[8]:


albany_df.head()


# In[9]:


albany_df.index


# In[10]:


#plotting the average price in albany region
plt.title("Average price in albany")
albany_df["AveragePrice"].plot()


# In[99]:


#smoothing the data using rolling average
albany_df["AveragePrice"].rolling(25).mean().plot()


# In[108]:


#sorting the index
albany_df.sort_index(inplace=True)
#creating new column to store the data 
albany_df["price25ma"] = albany_df["AveragePrice"].rolling(25).mean()
albany_df.head()


# In[111]:


#Printing the region values
df['region']


# In[112]:


#converting into array
df['region'].values


# In[113]:


df['region'].values.tolist()
# and then maybe get the uniques with:
print(set(df['region'].values.tolist()))


# In[114]:


#or simply we can use pandas builtin function
df['region'].unique()


# In[116]:


df["Date"] = pd.to_datetime(df["Date"])
df.sort_values(by="Date", ascending=True, inplace=True)
df.head()


# In[2]:


graph_df = pd.DataFrame()

for region in df['region'].unique():
    region_df = df.copy()[df['region']==region]
    region_df.set_index('Date', inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f"{region}_price25ma"]]  # note the double square brackets! (so df rather than series)
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])

graph_df.tail()


# In[1]:


graph_df.plot(figsize=(8,5), legend=False)


# In[ ]:




