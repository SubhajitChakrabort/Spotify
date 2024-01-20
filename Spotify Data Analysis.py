#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# In[4]:


spotify = pd.read_csv("C:\\Users\\SUBHAJIT\\Desktop\\My Document\\Study Document\\Projects\\Spotify Data Analysis\\tracks.csv")


# In[5]:


spotify


# In[6]:


spotify.head()


# In[7]:


spotify.tail()


# In[8]:


pd.isnull(spotify)


# In[9]:


pd.isnull(spotify).sum()


# In[11]:


spotify.describe()


# In[12]:


spotify.columns


# In[14]:


sort = spotify.sort_values('popularity', ascending =True)
sort


# In[15]:


sort = spotify.sort_values('popularity', ascending = True).head(10)
sort


# In[16]:


most = spotify.query('popularity>90', inplace = False).sort_values('popularity', ascending = False)
most[:10]


# In[19]:


spotify.columns


# In[20]:


spotify


# In[21]:


spotify.columns


# In[22]:


spotify.describe().transpose()


# In[24]:


spotify[["artists"]].iloc[18]


# In[25]:


spotify["duration"] = spotify["duration_ms"].apply(lambda x: round(x / 100))
spotify.drop("duration_ms", inplace =True, axis =1)


# In[26]:


spotify.duration.head()


# In[33]:


print(spotify.info())
print(spotify.head()) 


# In[46]:


spotify.columns


# In[47]:


spotify = pd.read_csv("C:\\Users\\SUBHAJIT\\Desktop\\My Document\\Study Document\\Projects\\Spotify Data Analysis\\tracks.csv")


# In[48]:


spotify.columns


# In[52]:


file_path = r'C:\Users\SUBHAJIT\Desktop\My Document\Study Document\Projects\Spotify Data Analysis\tracks.csv'
spotify = pd.read_csv(file_path)
print(spotify.info())
numeric_columns = spotify.select_dtypes(include=np.number).columns
corr_df = spotify[numeric_columns].corr(method='pearson')
plt.figure(figsize=(14, 6))
heatmap = sns.heatmap(data=corr_df, annot=True, fmt='.2f', vmin=-1, vmax=1, center=0, cmap='inferno', linewidths=1, linecolor='black')
heatmap.set_title('Correlation Heatmap between variables')
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90)
plt.show()


# In[53]:


spotify.columns


# In[54]:


spotify["duration"] = spotify["duration_ms"].apply(lambda x: round(x / 100))
spotify.drop("duration_ms", inplace =True, axis =1)


# In[55]:


spotify.duration.head()


# In[56]:


print(spotify.info())
print(spotify.head()) 


# In[57]:


sample_df = spotify.sample(int(0.004 * len(spotify)))


# In[58]:


print(len(sample_df))


# In[61]:


file_path = r'C:\Users\SUBHAJIT\Desktop\My Document\Study Document\Projects\Spotify Data Analysis\tracks.csv'
data = pd.read_csv(file_path)
plt.figure(figsize=(10, 6))
sns.regplot(data=data, y="loudness", x="energy", color="c").set(title="Loudness vs Energy correlation")
plt.show()


# In[66]:


file_path = r'C:\Users\SUBHAJIT\Desktop\My Document\Study Document\Projects\Spotify Data Analysis\tracks.csv'
data = pd.read_csv(file_path)
plt.figure(figsize=(10, 6))
sns.regplot(data=data, y="popularity", x="acousticness", color="b").set(title="Popularity vs Acousticness correlation")
plt.show()



# In[75]:


#spotify['dates'] = spotify.index.get_level_values('release_date')
#spotify.dates = pd.to_datetime(spotify.dates)
#years = spotify.dates.dt.year
print(spotify['release_date'].unique())


# In[76]:


spotify['dates'] = pd.to_datetime(spotify['release_date'], errors='coerce')


# In[78]:


spotify['dates'] = pd.to_datetime(spotify['release_date'], format='%Y-%m-%d', errors='coerce')


# In[79]:


spotify['dates']


# In[83]:


years = spotify['dates'].dt.year
sns.displot(years, discrete =True, aspect =2, height =5, kind ="hist").set(title= "Number of songs per year")


# In[84]:


total_dr = spotify.duration
fig_dims =(18, 7)
fig,  ax = plt.subplots(figsize = fig_dims)
fig = sns.barplot(x = years, y = total_dr, ax = ax, errwidth = False).set(title = "Year vs Duration")
plt.xticks(rotation =90)


# In[86]:


total_dr = spotify.duration
sns.set_style(style="whitegrid")
fig_dims =(10, 5)
fig,  ax = plt.subplots(figsize = fig_dims)
fig = sns.lineplot(x = years, y = total_dr, ax = ax).set(title = "Year vs Duration")
plt.xticks(rotation =60)


# In[87]:


spotify1 = pd.read_csv("C:\\Users\\SUBHAJIT\\Desktop\\My Document\\Study Document\\Projects\\Spotify Data Analysis\\SpotifyFeatures.csv")


# In[88]:


spotify1.head()


# In[89]:


plt.title("Duration of the song in defferent Geners")
sns.color_palette('rocket', as_cmap = True)
sns.barplot(y = 'genre', x = 'duration_ms', data = spotify1)
plt.xlabel("Duration in miliseconds")
plt.ylabel("Genres")


# In[90]:


sns.set_style(style ="darkgrid")
plt.figure(figsize =(10, 5))
famous = spotify1.sort_values("popularity", ascending =False).head(10)
sns.barplot(y ='genre', x ='popularity', data =famous).set(title = "Top 5 Generes by popularity")


# In[91]:


spotify1.columns


# In[ ]:




