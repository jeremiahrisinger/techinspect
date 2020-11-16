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
    def __init__(self, username):
        self.login_time = time.time()
        self.username = username
        self.uuid = uuid.uuid4().hex


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
            user_list[user.username] = ActiveUser(user.username)
            #prune the list every time someone logs in.
            prune(user_list)
            return True
    return False

def test_user_list_prune():
    test = ActiveUser('test')
    test.login_time -= SIX_HOURS + 10
    print(user_list)
    print("Adding test user...")
    user_list['test'] = test
    print(user_list)
    prune(user_list)
    print("Pruning...")
    print(user_list)
