CREATE TABLE ratings (
    user_id VARCHAR(255) REFERENCES users(user_id),
    movie_id VARCHAR(255) REFERENCES movies(movie_id),
    rating DOUBLE PRECISION NOT NULL,
    PRIMARY KEY (user_id, movie_id)
);