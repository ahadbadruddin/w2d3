#!/usr/bin/env python3

from mappers import Database 
import json
import requests




class User: 

    def __init__(self,username,password):
        self.username= username
        self.password= password

    def login(self):
        with Database() as d:
            d.cursor.execute(
               '''
                SELECT password  FROM users
                WHERE username = '{self.username}'
                ;''')
        password = d.cursor.fetchone()[0]
        if password:
            if self.password== password:
                return True
            return False


def lookup(company_name):
        api= lookup_api()
        query= api + company_name
        return json.loads(requests.get(query).text)[0]['Symbol']

def quote(symbol):
        api= quote_api()
        query= api + symbol
        return json.loads(requests.get(query).text)['LastPrice']
    
def quote_api():
        endpoint= 'http://dev.markitondemand.com/MODApis/api/v2/Quote/json?symbol='
        return endpoint

def lookup_api():
        endpoint= 'http://dev.markitondemand.com/MODApis/api/v2/Lookup/json?input='
        return endpoint


if __name__=='__main__':
    user = User('ahad','swordfish')
 #   print(user.fetch_username())
#    print(lookup('ford'))
