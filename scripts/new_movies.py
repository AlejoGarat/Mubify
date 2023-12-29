import pandas as pd

csv_file = 'movie.csv'
df = pd.read_csv(csv_file)

sql_file = '20231223153720_new_movies.up.sql'

with open(sql_file, 'w') as f:
    for index, row in df.iterrows():
        movie_id = row['movieId']
        title = row['title'].replace("'", "''")  # Escapar comillas simples

        sql_query = f"INSERT INTO movies (movie_id, title) VALUES ({movie_id}, '{title}');\n"
        f.write(sql_query)

print(f"Se generaron las consultas SQL en {sql_file}")

