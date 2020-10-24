from django.core.exceptions import ObjectDoesNotExist

from pages.models import *

def login(email, pswd):
    try:
        user = TIUser.objects.get(username=email)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist
    else:
        if user.check_password(pswd):
            return True
    return False

def add_user(email, password, image):
    return True
