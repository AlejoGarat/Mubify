import pandas as pd

csv_file = 'movie.csv'
df = pd.read_csv(csv_file)

sql_file = '20231223153722_new_movie_genres.up.sql'

with open(sql_file, 'w') as f:
    for index, row in df.iterrows():
        movie_id = row['movieId']
        genres = row['genres']
        splitted_genres = genres.split('|')
        
        for genre in splitted_genres:
            sql_query = f"INSERT INTO movie_genres (movie_id, genre_id) VALUES ({movie_id}, '{genre}');\n"
            f.write(sql_query)

print("Finished")