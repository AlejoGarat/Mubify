import streamlit as st
import requests
import pandas as pd
import pickle
from sklearn.neighbors import NearestNeighbors

api_url = "http://127.0.0.1:5000/api/"
current_page = 1

def main():
    st.title('Mubify')
    
    if "current_page" not in st.session_state:
        st.session_state.current_page = 1
    
    if not st.session_state.get("logged_in"):
        login()
    else:
        show_app_content()
        
    
def login():
    st.subheader("Login")
    user_id = st.text_input("User ID")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if validate_login(user_id, password):
            st.session_state.logged_in = True 
            st.session_state.user_id = user_id 
            st.experimental_rerun()
        else:
            st.error("Invalid user ID or password!")
            
def show_app_content():
    user_id_container = st.empty()
    user_id_container.text(f"User ID: {st.session_state.user_id}")
    movies_info = get_movie_info(9, current_page)
    display_movies(movies_info)
    show_pagination(current_page)

def validate_login(user_id, password):
    return True
    
def display_movies(movies_info):
    for i in range(0, len(movies_info), 3):
        col1, col2, col3 = st.columns(3)
        for j, movie in enumerate(movies_info[i:i+3]):
            column = col1 if j == 0 else (col2 if j == 1 else col3)
            with column:
                show_movie(movie, i + j)

def show_movie(movie, index):
    st.image(movie["movie_url"], caption=movie["movie_title"])
    row = index // 3 + 1
    col = index % 3 + 1
    button_key = f"similar_button_{row}_{col}" 
    if st.button("See similar movies", key=button_key):
        show_similar_movies(movie["movie_title"])

def get_movie_info(page_size, page_number):
    response = requests.get(api_url + "movies", params={"page_size": page_size, "page_number": page_number})
    return response.json()

def show_similar_movies(movie_title):
    similar_movies = get_similar_movies(movie_title)
    
    with st.sidebar:
        st.write(f"### Similar Movies for {movie_title}")
        for similar_movie in similar_movies:
            st.image(similar_movie["movie_url"], caption=similar_movie["movie_title"])

def get_similar_movies(movie_title):
    similar_movies = []
    movies_ds = pd.read_csv("similar_movies_ds.csv")
    movie = movies_ds[movies_ds['title'] == movie_title].drop(['title'], axis=1)
    
    with open('notebooks/knn_model.pkl', 'rb') as f:
        loaded_knn_model = pickle.load(f)
    
    distances, indices = loaded_knn_model.kneighbors(movie)

    for i in range(len(distances.flatten())):
        if i != 0:
            movie_info = {
                "movie_title": movies_ds['title'].iloc[indices.flatten()[i]],
                "movie_url": "https://m.media-amazon.com/images/I/71HQiOZsZ6L._AC_UF894,1000_QL80_.jpg"
            }
            similar_movies.append(movie_info)
    
    return similar_movies

if __name__ == "__main__":
    main()

