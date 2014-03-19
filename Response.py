import urllib.request
import urllib.parse
from bs4 import *
import requests
import datetime
from auth import Auth

class Test:
    
    def __init__(self, response):
        self.response = response
    
    def delayTest(self, response, rTime, url):
        expectedTime = datetime.timedelta(seconds=rTime)
        if response.elapsed > expectedTime:
            rs = "response to " + url + " took longer than expected"
            return rs
        return ""
            
            
    def responseTest(self, response, url):
        if response.status_code != 200:
            rs = "response from " + url + " is " + str(response.status_code)
            return rs
        else:
            return ""
            
            
    def dataTest(self, response, file, url):
        vectors = [line.strip() for line in open(file)]
        source = response.text
        warnings = []
        rs = ""
        #compare text to vectors
        for i in vectors:
            j = source.find(i)
            #return warning if anything in vectors detected
            if j >= 0:

                warnings.append("\tVector " +i + " found in " + url)
        for j in warnings:
            rs = rs + j + "\n"       
        return rs
        
        
    def sanTest(self, response, url):
        source = response.text
        potential = ["<",">",",",".",'"',"'","(",")","="] #This list doesn't have everything in it, but it should have enough to be able to say if an XSS attack is possible
        content = BeautifulSoup(source)
        for form in content.find_all("pre"):
            if any(word in source for word in potential):
                return "Potential XSS attack in " + url
        return "" 

    def vectorTest(self, url, session, form, vectorList, responseTime, testList):
        vectorList = [line.strip() for line in open(vectorList)]
        results = []
        for i in form:
            if (i != "submit") and (i != "Login") and (i != ""): 
                for v in vectorList:
                    payload = {i:v}
                    response = session.post(url, data=payload) 
                    print(response.text)
                    a = self.delayTest(response, responseTime, url)
                    b = self.responseTest(response, url)
                    d = self.sanTest(response, url)
                    if a and b and d:
                        resultString = "For URL: " + url + "\n\t" + a + "\n\t" + b + "\n\t" + d + "\n"
                        results.append(resultString)
        return "\n\n".join(results)


"""
Returns an array of results. one element per url.
Each element contains the url and the warnings associated with it.

urllist[0] MUST BE THE AUTHENTICATION URL
"""
def getResults(session,urlList,inputs, responseTime, testList, username, password,vectors):    
    results = []
    for i in urlList[1:]:
        response = session.get(i)
        test = Test(response)
        a = test.delayTest(response, responseTime, i)
        b = test.responseTest(response, i)
        c = test.dataTest(response, testList, i)
        if i in inputs.keys():
            d = test.vectorTest(i, session, inputs[i], vectors, responseTime, testList)
        else:
            d = ""
        resultString = i + "\n\t" + a + "\n\t" + b + "\n" + c + "\n\t" + d + "\n"
        results.append(resultString)
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
