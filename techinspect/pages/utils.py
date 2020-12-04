from django.core.exceptions import ObjectDoesNotExist

from pages.models import *

import time
import uuid

#A login dictionary that will be used to keep a list of active users.

user_list = {}

SIX_HOURS = 60 * 60 * 6

def prune(user_list):
    for key in list(user_list):
        if (time.time() - user_list[key].login_time) > SIX_HOURS:
            del user_list[key]

class ActiveUser():
    def __init__(self, user):
        self.login_time = time.time()
        self.user = user


def login(email, pswd):
    try:
        #attempt to grab user from db
        user = TIUser.objects.get(username=email)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist
    else:
        #if the user exists in the db, check that the password matches
        if user.check_password(pswd):
            #add user to user_list so we know they're logged in within the system
            user_list[uuid.uuid4().hex] = ActiveUser(TIUser.objects.get(username=email))
            print(f"Added user {user.username} to user_list")
            #prune the list every time someone logs in.
            return True
    return False
def is_TI(uuid):
    try:
        return TIUser.objects.get(UUID=uuid).isTI
    except Exception:
        return False

def get_user(uuid):
    return TIUser.objects.get(UUID=uuid)

def find_user_uuid(username):
    return TIUser.objects.get(username=username).UUID

def test_user_list_prune():
    test = ActiveUser(TIUser.objects.get(username='jackmnitti@gmail.com'))
    test.login_time -= SIX_HOURS + 10
    print(user_list)
    print("Adding test user...")
    user_list[uuid.uuid4()] = test
    print(user_list)
    prune(user_list)
    print("Pruning...")
    print(user_list)
