import streamlit as st
import requests

api_url = "http://127.0.0.1:5000/api/"

def main():
    st.title('Mubify')
    
    movies_info = get_movie_info(9, 1)
    display_movies(movies_info)
    
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
    return [
        {"movie_title": "Similar Movie 1", "movie_url": "https://example.com/similar_image1.jpg"},
        {"movie_title": "Similar Movie 2", "movie_url": "https://example.com/similar_image2.jpg"},
        {"movie_title": "Similar Movie 3", "movie_url": "https://example.com/similar_image3.jpg"},
    ]

if __name__ == "__main__":
    main()
