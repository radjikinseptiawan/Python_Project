class local_database:
    def __init__(self):
        self.users = []
    
    def add_users(self,account):
        self.users.append(account)
    
    def show_users(self):
        print("User ditampilkan!")
        [print(f'{user.username} ||| {user.email} ||| {user.password}') for user in self.users ]
        