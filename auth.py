'''
Created on Feb 19, 2014

@author: Dan
'''
import requests
from requests.auth import HTTPBasicAuth

class Auth:

    '''
    authenticates to a web application providing it supports HTTP Basic Auth
    if it doesn't, then we're sol.
    
    @params: web address, username, password
    '''
    def authenticate(self, address, user, password):
        a = requests.get(address, auth=HTTPBasicAuth(user, password))
        return a