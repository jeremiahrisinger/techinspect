from django.core.exceptions import ObjectDoesNotExist

from pages.models import *

def login(email, pswd):
    try:
        user = TIUser.objects.get(username=email)
    except ObjectDoesNotExist:
        return False
    else:
        if user.check_password(pswd):
            return True
