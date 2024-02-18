class MovieController:
    def __init__(self, movie_service):
        self.service = movie_service

    def get_movie_info(self, page_size, page_number):
        return self.service.get_movie_info(page_size, page_number)
