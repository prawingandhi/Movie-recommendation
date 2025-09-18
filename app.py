import pickle
import streamlit   as st
import requests
from main import similarity, movie





def fetch_poster(movie_id):
    api_key = '95dee51257c00d9a507f48e718065d9a'
    

    url = "https://api.themoviedb.org/3/movie/{movie_id}/images".format(movie_id=movie_id)

    headers = {
         "accept": "application/json",
         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5NWRlZTUxMjU3YzAwZDlhNTA3ZjQ4ZTcxODA2NWQ5YSIsIm5iZiI6MTc1NjczMzU5My4zOTUsInN1YiI6IjY4YjVhMDk5Mzc4ODliOGM1NzFmMjkxNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lYeXIM6LOH-diJrvWpcEZtfoLLqYvDm4hpP0bAYjgF4"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    posters = data.get('posters', [])

    for poster in posters[:5]:  # Show first 5 posters
        poster_path = poster['file_path']
        full_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    return full_url    

def recommend(movies):
    index=movie[movie['title']==movies].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True ,key=lambda x:x[1])
    recommend_movie=[]
    recommend_movie_posters=[]

    for i in distance[1:6]:
        movie_id=movie.iloc[i[0]].movie_id
        recommend_movie_posters.append(fetch_poster(movie_id))
        recommend_movie.append(movie.iloc[i[0]].title)
    return recommend_movie, recommend_movie_posters  

st.title("Movies Recommended System")
st.header("Welcome to Movie Recommender System")


movies_list=movie['title'].values
selected_movie=st.selectbox(
    'Select the Movie',
    movies_list
)

recommended_movie,recommended_movie_poster=recommend(selected_movie)
col1,col2,col3,col4,col5=st.columns(5)
with col1:
    st.text(recommended_movie[0])
    st.image(recommended_movie_poster[0])
with col2:
    st.text(recommended_movie[1])
    st.image(recommended_movie_poster[1])
with col3:      
    st.text(recommended_movie[2])
    st.image(recommended_movie_poster[2])
with col4:      
    st.text(recommended_movie[3])
    st.image(recommended_movie_poster[3])
with col5:      
    st.text(recommended_movie[4])   
    st.image(recommended_movie_poster[4])

