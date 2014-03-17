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
    
def delayTest(response,rTime):
    expectedTime = datetime.timedelta(seconds=rTime)
    if response.elapsed > expectedTime:
        print("response to " + response.url + " took longer than expected")
        
def responseTest(response):
    if response.status_code != 200:
        print("response from" + response.url + " is " + response.checkCode())
        
def dataTest(response, file):
    vectors = [line.strip() for line in open(file)]
    source = response.text
    #compare text to vectors
    for i in vectors:
        j = source.find(i)
        #return warning if anything in vectors detected
        if j >= 0:
            print(vectors[i] + " found in " + response.url)
    
def sanTest(response):
    source = response.text
    #do this somehow
    
    




