#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
from IPython.display import display

df = pd.read_csv('dataset-sell4all-maroc.csv')

df.head()

df.count()

pd.options.display.max_columns = None

display(df)

df.dtypes

df['Age'].mean()

df['Customer spendings'].mean()


# median MPG for each Company
df.groupby('Country')['Age'].median()


sns.barplot(x=df['Country'].head(3),y=df['Customer spendings'],data=df)


# In[22]:


sns.barplot(x=df['Country'].head(36),y=df['Customer spendings'],data=df)


# In[23]:



df.drop(df[df['Customer spendings'] < 10].index, inplace = True)

df.drop_duplicates()

df.drop(columns=['Email', 'Phone Number','Name','Address','Postal code','Last date of connection','Last time of connection'])


df.to_csv('cleaned_data.csv')


# In[ ]:




