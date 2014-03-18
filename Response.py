import urllib.request
import urllib.parse
from bs4 import *
import requests
import datetime
from auth import Auth
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
            return rs
            
            
    def responseTest(self, response):
        if response.status_code != 200:
            rs = "response from" + response.url + " is " + response.checkCode()
            return rs
            
            
    def dataTest(self, response, file):
        vectors = [line.strip() for line in open(file)]
        source = response.text
        warnings = []
        rs = ""
        #compare text to vectors
        for i in vectors:
            j = source.find(i)
            #return warning if anything in vectors detected
            if j >= 0:
                warnings.append(vectors[i] + " found in " + response.url)
        for j in warnings:
            rs = rs + j + "\n"       
        return rs
        
        
    def sanTest(self, response):
        source = response.text
        #fucking find out how to do this
        rs = ""
        return rs

"""
"""
def getResults(urlList, responseTime, testList, username, password):    
    session = Auth.authenticate(urlList[0], username, password)
    results = []
    for i in urlList:
        response = session.get(urlList[i])
        test = Test(session.get(response))
        a = test.delayTest(response, responseTime)
        b = test.responseTest(response)
        c = test.dataTest(response, testList)
        d = test.dataTest(response)
        resultString = response.url + "\n" + a + "\n" + b + "\n" + c + "\n" + d + "\n"
        results.append(resultString)
    return results



