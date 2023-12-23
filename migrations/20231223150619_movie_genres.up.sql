CREATE TABLE movie_genres (
    movie_id VARCHAR(255) NOT NULL,
    genre_id VARCHAR(255) NOT NULL,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);