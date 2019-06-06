#!/usr/bin/env python3

from mappers import Database 

class User: 

    def __init__(self,username,password):
        self.username= username
        self.password= password

    def fetch_username(self):
        with Database() as d:
            d.cursor.execute(
                '''
                SELECT username FROM users;''')
        all_usernames = d.cursor.fetchall()
       
    def fetch_password(self):
        pass


if __name__=='__main__':
    user = User('ahad','swordfish')
    print(user.fetch_username())
