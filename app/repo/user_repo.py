class UserRepository:
    def __init__(self, conn):
        self.conn = conn 

    def get_user_count(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM users")
            count = cur.fetchone()[0]
            return count

    def get_first_10_user_names(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT username FROM users LIMIT 10")
            names = [row[0] for row in cur.fetchall()]
            return names
        
    def get_recommendation_dataset(self):
        with self.conn.cursor() as cur:
            cur.execute(
                """SELECT r.*, m.*, 
                MAX(CASE WHEN mg.genre_id = 'Action' THEN 1 ELSE 0 END) AS Action,
                MAX(CASE WHEN mg.genre_id = 'Adventure' THEN 1 ELSE 0 END) AS Adventure,
                MAX(CASE WHEN mg.genre_id = 'Animation' THEN 1 ELSE 0 END) AS Animation,
                MAX(CASE WHEN mg.genre_id = 'Children' THEN 1 ELSE 0 END) AS Children,
                MAX(CASE WHEN mg.genre_id = 'Comedy' THEN 1 ELSE 0 END) AS Comedy,
                MAX(CASE WHEN mg.genre_id = 'Crime' THEN 1 ELSE 0 END) AS Crime,
                MAX(CASE WHEN mg.genre_id = 'Documentary' THEN 1 ELSE 0 END) AS Documentary,
                MAX(CASE WHEN mg.genre_id = 'Drama' THEN 1 ELSE 0 END) AS Drama,
                MAX(CASE WHEN mg.genre_id = 'Fantasy' THEN 1 ELSE 0 END) AS Fantasy,
                MAX(CASE WHEN mg.genre_id = 'Film-Noir' THEN 1 ELSE 0 END) AS FilmNoir,
                MAX(CASE WHEN mg.genre_id = 'Horror' THEN 1 ELSE 0 END) AS Horror,
                MAX(CASE WHEN mg.genre_id = 'IMAX' THEN 1 ELSE 0 END) AS IMAX,
                MAX(CASE WHEN mg.genre_id = 'Musical' THEN 1 ELSE 0 END) AS Musical,
                MAX(CASE WHEN mg.genre_id = 'Mystery' THEN 1 ELSE 0 END) AS Mystery,
                MAX(CASE WHEN mg.genre_id = 'Other' THEN 1 ELSE 0 END) AS Other,
                MAX(CASE WHEN mg.genre_id = 'Romance' THEN 1 ELSE 0 END) AS Romance,
                MAX(CASE WHEN mg.genre_id = 'Sci-Fi' THEN 1 ELSE 0 END) AS SciFi,
                MAX(CASE WHEN mg.genre_id = 'Thriller' THEN 1 ELSE 0 END) AS Thriller,
                MAX(CASE WHEN mg.genre_id = 'War' THEN 1 ELSE 0 END) AS War,
                MAX(CASE WHEN mg.genre_id = 'Western' THEN 1 ELSE 0 END) AS Western
                FROM ratings r
                INNER JOIN movies m ON r.movie_id = m.movie_id
                LEFT JOIN movie_genres mg ON m.movie_id = mg.movie_id
                GROUP BY r.user_id, r.movie_id, m.movie_id;"""
            )
        dataset = cur.fetchall()
        return dataset
