'''
Created on Feb 19, 2014

@author: Dan
'''
import requests
from requests.auth import HTTPBasicAuth

class Auth:

    def authenticate(self, address, user, password):
        a = requests.get(address, auth=HTTPBasicAuth(user, password))