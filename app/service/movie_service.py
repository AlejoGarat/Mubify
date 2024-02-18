class MovieService:
    def __init__(self, movie_repo):
        self.repo = movie_repo
        pass
    
    def get_movie_info(self, page_size, page_number):
        movies = self.repo.get_movie_info(page_size, page_number)
        return self.add_movies_link(movies)

    # This will be transitory until movie links are stored in the database
    def add_movies_link(self, movies):
        movie_url = "https://m.media-amazon.com/images/M/MV5BMTQ1OTU0ODcxMV5BMl5BanBnXkFtZTcwOTMxNTUwOA@@._V1_.jpg"
        updated_movies = []
        for movie_id, movie_title in movies:
            updated_movie = {
                "movie_id": movie_id,
                "movie_title": movie_title,
                "movie_url": movie_url
            }
            updated_movies.append(updated_movie)
        return updated_movies

