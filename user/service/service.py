from user.repository import repository

def login():
    print("...service...login...")
    repository.get_user()
    return

def register():
    print("...service...register...")
    repository.create_user()
    return

def profile():
    print("...service...profile...")
    repository.update_profile()
    return