#!/usr/bin/env python3

import time
from  models import User


def infinite_loop():
    ### username = view.login_menu()
    username = input('Your application username: ')
    password = input('Your application password: ')
   
#FIXME


    stored_username= User(username, password).fetch_username()
    stored_password= User().fetch_password()
    


    if username == stored_username:
        if  password == store_password:
            return 'successful login'
        return 'catch-all'
    time.sleep(2)
    print('testing...')

if __name__== '__main__':
    print(infinite_loop())
