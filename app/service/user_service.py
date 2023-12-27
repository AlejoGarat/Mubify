class UserService:
    def __init__(self, user_repo):
        self.repo = user_repo
        pass

    def get_user_count(self):
        return self.repo.get_user_count()

    def get_first_10_user_names(self):
        return self.repo.get_first_10_user_names()