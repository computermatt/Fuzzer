import urllib.request
import urllib.parse
from bs4 import *
import requests
import datetime
'''
Created on Mar 16, 2014

@author: Dan
'''

#a = Response(requests.get("http://127.0.0.1/dvwa/vulnerabilities/sqli/"))


def test(response):
    
#check delay
    expectedTime = datetime.timedelta(seconds=1)
    if response.elapsed > expectedTime:
        print("response to " + response.url + " took longer than expected")
        
#Check response code
    if response.status_code != 200:
        print("response from" + response.url + " is " + response.checkCode())
        
#Check for test data
    source = response.text
    #compare text to vectors
    #return warning if anything in vectors detected
    
#Check for sanatization of input
    source2 = response.text
    
    




