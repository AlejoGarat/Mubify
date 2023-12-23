import pandas as pd

csv_file = 'movie.csv'
df = pd.read_csv(csv_file)

sql_file = '20231223153721_new_genres.up.sql'

genre_dict = {}

with open(sql_file, 'w') as f:
    for index, row in df.iterrows():
        genres = row['genres']
        splitted_genres = genres.split('|')
        
        for genre in splitted_genres:
            if genre not in genre_dict:
                genre_dict[genre] = True
                sql_query = f"INSERT INTO genres (genre_id) VALUES ('{genre}');\n"
                f.write(sql_query)

print("Finished")