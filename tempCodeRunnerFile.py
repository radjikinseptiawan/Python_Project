from register.account_verification import verification_section
from register.register_section import account_register
from data.data_storage import local_database
from data.user_constructor import user_constructor

verification = verification_section()
account = account_register()
user = user_constructor(verification.verification_username(account.username()),verification.verification_email(account.email()),verification.verification_password(account.password()))
db = local_database()

db.add_users(user)

db.show_users()