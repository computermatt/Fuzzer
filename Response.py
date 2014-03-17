import urllib.request
import urllib.parse
from bs4 import *
import requests
'''
Created on Mar 16, 2014

@author: Dan
'''
    
def checkCode( url):
    r = requests.get('https://www.facebook.com').status_code
    return r

def checkDelay( url):
    r = requests.get('https://www.facebook.com').elapsed
    return r

def checkTestData( url):
    pass

def checkSanatization( url):
    pass

print(checkDelay("https://www.facebook.com"))