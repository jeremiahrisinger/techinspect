from pages.models import *

def login(email, enc_pswd):
    if(user := User.objects.get(pk=email)):
        if enc_pswd == user.enc_pswd:
            print("It worked lol")
        else:
            print("Failed")
