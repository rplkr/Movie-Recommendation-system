import pickle
import pandas as pd
import streamlit as st
import requests
import numpy as np


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=bd9d93e4649f8d7b42731beda117f8c6&language=en-US"
    data = requests.get(url).json()

    if 'poster_path' in data and data['poster_path']:
        poster_path = data['poster_path']
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        return full_path
    else:
        return np.NaN


def recommend(movie):
    index = movies[movies['movie_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].id
        poster = fetch_poster(movie_id)

        if not pd.isna(poster):
            recommended_movie_posters.append(poster)
            recommended_movie_names.append(movies.iloc[i[0]].movie_title)

    return recommended_movie_names[:5], recommended_movie_posters[:5]


st.header('Movie Recommender System')
movies = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['movie_title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])




