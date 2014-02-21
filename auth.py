'''
Created on Feb 19, 2014

@author: Dan
'''
import requests
from requests.auth import HTTPBasicAuth

a = requests.get('https://www.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
print(a)