import re

class verification_section:
    def verification_email(self,email):
        if email.count('@') != 1:
            raise ValueError("Failed Email Verification: Email musth have one '@' character! ")
        elif email.startswith('@') or email.endswith("@"):
            raise ValueError("Failed Email Verification: Character '@' cant place in beginning or end position!")
        elif email.endswith('.'):
            raise ValueError("Failed Email Verification: Character '.' cant place in beginning or end position!")    
        elif not re.match(r'[a-zA-Z0-9]+@[a-z]+\.[a-z]+$',email):
            raise ValueError("Failed Email Verification: Email containt a invalid character!")        
        else:
            print('Email has success validated!')
        return email

    def verification_password(self,password):
        uppercase = r'[A-Z]'
        lowercase = r'[a-z]'
        numeric = r'[0-9]'
        symbol = r'\W'

        if len(password) < 8:
            raise ValueError('Failed Password Verification : password character cant less than 8! ')
        elif not re.search(uppercase,password):
            raise ValueError('Failed Password Verification : password must have a uppercase character! ')    
        elif not re.search(lowercase,password):
            raise ValueError('Failed Password Verification : password must have a lowercase character! ')
        elif not re.search(numeric,password):
            raise ValueError('Failed Password Verification : password must have a number character!') 
        elif not re.search(symbol,password):
            raise ValueError('Failed Password Verification : password must have a symbol character!') 
        else:
            print("Password has success validate!")
        return password

    def verification_username(self,username):
        if  re.search(r'\W',username):
            raise ValueError("Failed Username Verification : Username can't containt non-alphanumeric character like ' ' or *$%@!., ")
        else:
            print("Username has success validated!")
        return username