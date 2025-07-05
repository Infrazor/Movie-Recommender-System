import streamlit as st
import pickle
import pandas as pd
import requests
import time


@st.cache_data(show_spinner=False)#Benefit: Each unique movie_id is only fetched once — faster, more stable, and no repeated failures.
def fetch_poster_cached(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=bc82971fc51ffa4d274cdd9026188786&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        poster_path = response.json().get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except:
        pass
    return None

def fetch_poster(movie_id):
    poster = fetch_poster_cached(movie_id)
    if poster is None:
        # Retry once without caching
        try:
            response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=bc82971fc51ffa4d274cdd9026188786&language=en-US", timeout=5)
            response.raise_for_status()
            poster_path = response.json().get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
        except:
            return None
    return poster



movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_name = []
    recommended_movie_posters=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_name.append(movies.iloc[i[0]].title)
        # fetch movie poster from api
        recommended_movie_posters.append(fetch_poster(movie_id))
        time.sleep(0.2)  # small delay to avoid overloading the API
    return recommended_movie_name, recommended_movie_posters



st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'Which movie do you want recommendations for?',
    movies['title'].values)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(recommended_movie_names[i])
            if recommended_movie_posters[i]:
                st.image(recommended_movie_posters[i])
            else:
                st.image("https://via.placeholder.com/200x300?text=No+Poster+Available")
                st.text("No poster available")
