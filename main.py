from register.account_verification import verification_section
from register.register_section import account_register
from data.data_storage import local_database
from data.user_constructor import user_constructor
from login.verification_login import verification_login
from login.login_section import login_account
from utils.crypted import encryption

verification = verification_section()
account = account_register()
db = local_database()
veriflo = verification_login(db)
login = login_account()
encryptions = encryption()
while True:
    print('1. Login')
    print('2. Register')
    print('3. Admin Config')
    choice = input("Masukkan opsi: ")
    if choice == '1':
        veriflo.login_verification(login.username(),encryptions.vigenere(login.password()))
        if veriflo:
            print("Login...")
        else :
            print("Failed login!")
    elif choice  == '2':
        user = user_constructor(verification.verification_username(account.username()),verification.verification_email(account.email()),encryptions.vigenere(verification.verification_password(account.password())))
        if user:
            db.add_users(user)
            print("Success register account!")
        else:
            print("Failed register account!")
    elif choice == '3':
        db.show_users()