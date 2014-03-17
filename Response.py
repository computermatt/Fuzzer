import urllib.request
import urllib.parse
from bs4 import *
import requests
'''
Created on Mar 16, 2014

@author: Dan
'''
class Response:
    
    def __init__(self, url):
        self.request = requests.get(url)

        
    def checkCode(self):
        return self.request.status_code
    
    def checkDelay(self):
        return self.request.elapsed
    
    def checkTestData(self):
        pass
    
    def checkSanatization(self):
        pass
    
a = Response("https://www.facebook.com")