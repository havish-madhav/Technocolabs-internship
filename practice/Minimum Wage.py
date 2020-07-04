#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("C:/users/hp/Desktop/Minimum Wage Data.csv", encoding="latin")


# In[3]:


df.head()


# In[4]:


df.to_csv("C:/users/hp/Desktop/minwage.csv", encoding="utf-8")


# In[5]:


df=pd.read_csv("C:/users/hp/Desktop/minwage.csv")


# In[6]:


df.head()


# In[7]:


#using groupby function to group the unique values and setting the year as index
gb = df.groupby("State")
gb.get_group("Alabama").set_index("Year").head()


# In[8]:


#creating new dataframe and iterating over the group
act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name})
    else:
        act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name}))

act_min_wage.head()


# In[9]:


act_min_wage.describe()


# In[10]:


#checking the correlation
act_min_wage.corr().head()


# In[12]:


#taking seperate dataframe to identify the rows having 0 low.2018 value
issue_df = df[df['Low.2018']==0]
issue_df.head()


# In[13]:


#knowing the unique states 
issue_df['State'].unique()


# In[14]:


#replacing the null values and now checking the corr table
act_min_wage.replace(0, np.NaN).dropna(axis=1).corr().head()


# In[15]:


#saving the dataframe as variable
min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()


# In[16]:


for problem in issue_df['State'].unique():
    if problem in min_wage_corr.columns:
        print("Missing something here....")


# In[17]:


grouped_issues = issue_df.groupby("State")
grouped_issues.get_group("Alabama").head(3)


# In[18]:


grouped_issues.get_group("Alabama")['Low.2018'].sum()


# In[19]:


for state, data in grouped_issues:
    if data['Low.2018'].sum() != 0.0:
        print("Some data found for", state)


# In[21]:


#since its a scraped data we are unable to get over it
#using matplotlib to plot the correlation
plt.matshow(min_wage_corr)
plt.show()


# In[22]:


#customizing the above plot
labels = [c[:2] for c in min_wage_corr.columns]  # get abbv state names.
fig = plt.figure(figsize=(12,12))  # figure so we can add axis
ax = fig.add_subplot(111)  # define axis, so we can modify
ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)  # display the matrix
ax.set_xticks(np.arange(len(labels)))  # show them all!
ax.set_yticks(np.arange(len(labels)))  # show them all!
ax.set_xticklabels(labels)  # set to be the abbv (vs useless #)
ax.set_yticklabels(labels)  # set to be the abbv (vs useless #)

plt.show()


# In[25]:


#importing tables from website using pandas
import requests
web = requests.get("https://www.infoplease.com/state-abbreviations-and-state-postal-codes")
dfs = pd.read_html(web.text)
dfs = pd.read_html("https://www.infoplease.com/state-abbreviations-and-state-postal-codes")


# In[26]:


#printing the abbrivations of states
for df in dfs:
    print(df.head())


# In[28]:


#storing in a variable
state_abbv = dfs[0]
state_abbv.head()


# In[30]:


#saving it to a csv file and reading again
state_abbv.to_csv("C:/users/hp/Desktop/state_abbv.csv")
state_abbv = pd.read_csv("C:/users/hp/Desktop/state_abbv.csv")
state_abbv.head()


# In[32]:


state_abbv[["State/District", "Postal Code"]].to_csv("C:/users/hp/Desktop/state_abbv.csv", index=False)
state_abbv = pd.read_csv("C:/users/hp/Desktop/state_abbv.csv", index_col=0)
state_abbv.head()


# In[34]:


#saving the postal codes to dictonary
abbv_dict = state_abbv.to_dict()
abbv_dict


# In[35]:


abbv_dict = abbv_dict['Postal Code']
abbv_dict


# In[36]:


#now we can change the labels 
labels = [abbv_dict[c] for c in min_wage_corr.columns]  # get abbv state names


# In[37]:


abbv_dict['Federal (FLSA)'] = "FLSA"
labels = [abbv_dict[c] for c in min_wage_corr.columns] 


# In[38]:


abbv_dict['Guam'] = "GU"
abbv_dict['Puerto Rico'] = "PR"
labels = [abbv_dict[c] for c in min_wage_corr.columns]


# In[39]:


#after few replacements to the postal codes now we can plot it 
fig = plt.figure(figsize=(12,12))  # figure so we can add axis
ax = fig.add_subplot(111)  # define axis, so we can modify
ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)  # display the matrix
ax.set_xticks(np.arange(len(labels)))  # show them all!
ax.set_yticks(np.arange(len(labels)))  # show them all!
ax.set_xticklabels(labels)  # set to be the abbv (vs useless #)
ax.set_yticklabels(labels)  # set to be the abbv (vs useless #)

plt.show()


# In[ ]:




