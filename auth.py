'''
Created on Feb 19, 2014

@author: Dan
'''
import requests
from requests.auth import HTTPBasicAuth

class Auth:

    '''
    @params: web address, username, password
    '''
    def authenticate(self, address, user, password):
        a = requests.Session()
        a.post(address, data={"username":user,"password":password, "Login":"Login"}, allow_redirects=True)
        return a
