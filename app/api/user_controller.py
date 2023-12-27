class UserController:
    def __init__(self, user_service):
        self.service = user_service

    def get_user_count(self):
        return self.service.get_user_count()

    def get_first_10_user_names(self):
        return self.service.get_first_10_user_names()
