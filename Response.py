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
        else:
            return ""
            
            
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

                warnings.append("Vector " +i + " found in " + response.url)
        for j in warnings:
            rs = rs + j + "\n"       
        return rs
        
        
    def sanTest(self, response):
        source = response.text
        #fucking find out how to do this
        rs = ""
        return rs

"""
Returns an array of results. one element per url.
Each element contains the url and the warnings associated with it.

urllist[0] MUST BE THE AUTHENTICATION URL
"""
def getResults(urlList, responseTime, testList, username, password):    
    session = Auth.authenticate("q",urlList[0], username, password)
    results = []
    counter = 0
    for i in urlList:
        response = session.get(urlList[counter])
        test = Test(response)
        a = test.delayTest(response, responseTime)
        b = test.responseTest(response)
        c = test.dataTest(response, testList)
        d = test.sanTest(response)
        resultString = response.url + "\n" + a + "\n" + b + "\n" + c + "\n" + d + "\n"
        results.append(resultString)
        counter = counter + 1
    return results

#Testing Stuff
'''
a = Auth.authenticate("a","http://127.0.0.1/dvwa/login.php", "admin", "password")
b = a.get("http://127.0.0.1/dvwa/index.php")
c = Test.dataTest("a", b, "testdata.txt")
d = Test.delayTest("a", b, 0.0001)
e = Test.responseTest("a",b)
print(c)
print(d)
print(e)
'''

'''
list1 = ["http://127.0.0.1/dvwa/login.php","http://127.0.0.1/dvwa/index.php","http://127.0.0.1/dvwa/vulnerabilities/sqli/"]
a = getResults(list1,0.001,"testdata.txt","admin","password")
for i in a:
    print(i)
'''