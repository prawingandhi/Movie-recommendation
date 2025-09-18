#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import ast
import json


# In[2]:


movie_data=pd.read_csv('movieds/tmdb_5000_credits.csv')


# In[3]:


movie_data.head(2)


# In[5]:


movie_data['crew'][0]


# In[4]:


data2=pd.read_csv('movieds/tmdb_5000_movies.csv')


# In[5]:


data2.head(2)


# In[6]:


movie_data=movie_data.merge(data2,on='title')


# In[7]:


movie_data.head(2)


# In[8]:


movie_data.columns


# In[9]:


movie_data=movie_data.drop(['budget','homepage','production_companies','production_countries','release_date', 'revenue', 'runtime', 'status','vote_average', 'vote_count','tagline','original_title' ],axis=1)


# In[10]:


movie_data.head(2)


# In[11]:


movie_data.isnull().sum()


# In[12]:


movie_data.dropna(inplace=True)


# In[13]:


type(movie_data['genres'])


# In[14]:


movie_data['geners']= movie_data['genres'].to_list()


# In[15]:


type(movie_data['genres'])


# In[16]:


type(movie_data['geners'])


# In[17]:


movie_data['genre_names'] = movie_data['geners'].apply(lambda x: [
    d['name'] for d in (json.loads(x) if isinstance(x, str) else x)
])


# In[18]:


movie_data=movie_data.drop(['genres','geners'],axis=1)


# In[19]:


movie_data['keywords'].iloc[0]


# In[20]:


movie_data.head(2)


# In[21]:


movie_data['keywords']=movie_data['keywords'].apply(lambda x: [ d['name']for d in (json.loads(x)if isinstance(x,str)else x)])


# In[22]:


movie_data['spoken_languages'].iloc[0]


# In[23]:


movie_data['spoken_languages']=movie_data['spoken_languages'].apply(lambda x: [d['iso_639_1'] for d in (json.loads(x) if isinstance(x,str)else x)])


# In[24]:


movie_data.head(2)


# In[25]:


movie_data['cast']=movie_data['cast'].apply(lambda x:[ d['name']for d in (json.loads(x) if isinstance(x,str) else x)])


# In[26]:


movie_data.head(2)


# In[27]:


movie_data['cast']=movie_data['cast'].apply(lambda x: x[:3])


# In[28]:


movie_data.head(2)


# In[31]:


def pic_dic(x):
    b=[]
    if isinstance(x,str):
        x=json.loads(x)
        for d in x:
            if d['job']=='Director':

                 b.append(d['name'])

        return b             



# In[32]:


movie_data['director']=movie_data['crew'].apply(pic_dic)


# In[33]:


movie_data=movie_data.drop(['crew'],axis=1)


# In[34]:


movie_data.head()


# In[35]:


movie_data=movie_data.drop((['id','original_language','spoken_languages']),axis=1)


# In[36]:


movie_data.head(2)


# In[37]:


movie_data['overview']=movie_data['overview'].apply(lambda x:x.split())


# In[38]:


movie_data.head(2)


# In[39]:


def remove_space(words):
    l=[]
    for i in words: 
        l.append(i.replace(' ',''))
    return l    


# In[40]:


movie_data['cast']=movie_data['cast'].apply(remove_space)


# In[41]:


movie_data['director']=movie_data['director'].apply(remove_space)


# In[42]:


movie_data['keywords']=movie_data['keywords'].apply(remove_space)


# In[43]:


movie_data['title']=movie_data['title'].apply(lambda x: x.replace(' ',''))


# In[44]:


movie_data.head(2)


# In[45]:


movie_data['tags']=movie_data['overview']+movie_data['cast']+movie_data['director']+movie_data['keywords']+movie_data['genre_names']


# In[46]:


movie_data.head(2)


# In[47]:


movie=movie_data[['movie_id','title','tags']]


# In[48]:


movie.head(2)


# In[49]:


movie['tags']=movie['tags'].apply(lambda x:' '.join(x))


# In[50]:


movie['tags']=movie['tags'].apply(lambda x: x.replace(',',''))


# In[51]:


movie['tags'].iloc[0]


# In[57]:


movie['tags']=movie['tags'].apply(lambda x:x.lower())


# In[58]:


movie['tags'].iloc[0]


# In[59]:


movie.head(2)


# In[61]:


from sklearn.feature_extraction.text import CountVectorizer


# In[62]:


cv=CountVectorizer(max_features=5000,stop_words='english')


# In[67]:


vector=cv.fit_transform(movie['tags']).toarray()


# In[69]:


vector


# In[70]:


vector.shape


# In[71]:


from sklearn.metrics.pairwise import cosine_similarity


# In[72]:


similarity=cosine_similarity(vector)


# In[ ]:


similarity


# In[94]:


def get_recommend(name):
    index=movie[movie['title']==name].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True ,key=lambda x:x[1])
    for i in distance[1:6]:
        print(movie.iloc[i[0]].title)



# In[99]:


get_recommend("PiratesoftheCaribbean:AtWorld'sEnd")


# In[108]:


import os
os.makedirs('movie_doc', exist_ok=True)


# In[109]:


import pickle


# In[110]:


pickle.dump(movie,open('movie_doc/movies_list.pkl','wb'))
pickle.dump(similarity,open('movie_doc/similarity.pkl','wb'))


# In[ ]:




