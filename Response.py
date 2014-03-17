import urllib.request
import urllib.parse
from bs4 import *
import requests
import datetime
'''
Created on Mar 16, 2014

@author: Dan
'''

class Test:
    
    def __init__(self, response):
        self.response = response
    
    def delayTest(self, response, rTime):
        expectedTime = datetime.timedelta(seconds=rTime)
        if response.elapsed > expectedTime:
            rs = "response to " + response.url + " took longer than expected"
            print(rs) #testing
            
            
    def responseTest(self, response):
        if response.status_code != 200:
            rs = "response from" + response.url + " is " + response.checkCode()
            print(rs) #testing
            
            
    def dataTest(self, response, file):
        vectors = [line.strip() for line in open(file)]
        source = response.text
        #compare text to vectors
        for i in vectors:
            j = source.find(i)
            #return warning if anything in vectors detected
            if j >= 0:
                rs = vectors[i] + " found in " + response.url
                print(rs) #testing
        
        
    def sanTest(self, response):
        source = response.text
        #fucking find out how to do this
    
    




