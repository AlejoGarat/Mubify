CREATE TABLE ratings (
    user_id INTEGER REFERENCES users(user_id),
    movie_id INTEGER REFERENCES movies(movie_id),
    rating DOUBLE PRECISION NOT NULL,
    PRIMARY KEY (user_id, movie_id)
);