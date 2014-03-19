import urllib.request
import urllib.parse
from bs4 import *
import requests
import datetime
from auth import Auth

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
        potential = ["<",">",",",".",'"',"'","(",")","="] #This list doesn't have everything in it, but it should have enough to be able to say if an XSS attack is possible
	if any(word in source for word in potential):
		return "Potential XSS attack in " + response.url 
	return False

    def vectorTest(self, url, session, form, vectorList, responseTime, testList):
        results = []
        for i in form:
            if i != "submit": #submit is a button, you can't exploit a button!
                for v in vectorList:
                    payload = {i:v}
                    response = session.post(url, data=payload) 
                    a = delayTest(response, responseTime)
                    b = responseTest(response)
                    c = dataTest(response, testList)
                    d = test.sanTest(response)
                    resultString = response.url + "\n" + a + "\n" + b + "\n" + c + "\n" + d + "\n"
                    results.append(resultString)
        return results


"""
"""
def getResults(urlList, formList, responseTime, testList, username, password, vectorFile):    
    session = Auth.authenticate(urlList[0], username, password)
    results = []
    vectorList = [line.strip() for line in open(vectorFile)]
    for i in urlList:
        if i in formList.keys():
            results.append(test.vectorTest(response, formList[i], vectorList))
        else:   
            response = session.get(urlList[i])
            test = Test(session.get(response))
            a = test.delayTest(response, responseTime)
            b = test.responseTest(response)
            c = test.dataTest(response, testList)
            d = test.sanTest(response)
            resultString = response.url + "\n" + a + "\n" + b + "\n" + c + "\n" + d + "\n"
            results.append(resultString)
    return results



