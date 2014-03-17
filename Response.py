import urllib.request
import urllib.parse
from bs4 import *
import requests
'''
Created on Mar 16, 2014

@author: Dan
'''
    
def checkCode(request):
    r = request.status_code
    return r

def checkDelay(request):
    r = request.elapsed
    return r

def checkTestData(request):
    pass

def checkSanatization(request):
    pass

a = requests.get("https://www.facebook.com")
print("Response Delay:  ") 
print(checkDelay(a))
print("Response Code:  ") 
print(checkCode(a))