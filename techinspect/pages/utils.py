from pages.models import *

def login(email, pswd):
    if(user := TIUser.objects.get(username=email)):
        if user.check_password(pswd):
            print("It worked lol")
        else:
            print("Failed")
