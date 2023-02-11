class User:
    def __init__(self,username):
        self .username = username

username = input("enter username: ")
user = User(username)
print("your username is :",user.username)