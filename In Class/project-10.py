def validate_email(email):
    if '@' in email:
        return True
    else:
        return False
    
def validate_password(password):
    if password.isalnum():
        return True
    else:
        return False
    

email_correct = False
password_correct = False
while True:
    if not email_correct:
        email = input('Email girin: ')
        if validate_email(email):
            email_correct = True
    elif not password_correct:
        password = input('Sifre girin: ')
        if validate_password(password):
            password_correct = True
    else:
        print('Siz giris etdiniz!')
        break
    

def register_user():
    email_correct = False
    password_correct = False
    while True:
        if not email_correct:
            email = input('Email girin: ')
            if validate_email(email):
                email_correct = True
        elif not password_correct:
            password = input('Sifre girin: ')
            if validate_password(password):
                password_correct = True
        else:
            print('Siz giris etdiniz!')
            break
    return {'email': email, 'password': password}
