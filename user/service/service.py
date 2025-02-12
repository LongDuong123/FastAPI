from repository import repository

class UserService:
    def __init__(self, repo: repository.UserRepository):
        self.repo = repo
        
    def login(self):
        print("...service...login...")
        self.repo.get_user()
        return

    def register(self):
        print("...service...register...")
        user = self.repo.create_user()
        return

    def profile(self):
        print("...service...profile...")
        user = self.repo.update_profile()
        return
