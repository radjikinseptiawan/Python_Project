class verification_login:
    def __init__(self,database):
        self.database = database
    def login_verification(self,username,password):
        for user in self.database.users:
            if user.username == username and user.password == password:
                print("Username and password correctly system will direct you to lobby")
                return True
            print("Incorrect username or password or maybe this username can`t find in out database!")
            return False