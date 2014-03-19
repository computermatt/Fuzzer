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

                warnings.append("Vector " +i + " found in " + url)
        for j in warnings:
            rs = rs + j + "\n"       
        return rs
        
        
    def sanTest(self, response, url):
        source = response.text
        potential = ["<",">",",",".",'"',"'","(",")","="] #This list doesn't have everything in it, but it should have enough to be able to say if an XSS attack is possible
        content = BeautifulSoup(source)
        for form in content.find_all("form"):
            if any(word in source for word in potential):
                return "Potential XSS attack in " + url
        return "" 

    def vectorTest(self, url, session, form, vectorList, responseTime, testList):
        results = []
        for i in form:
            if (i != "submit") or (i != "Login"): 
                for v in vectorList:
                    payload = {i:v}
                    response = session.post(url, data=payload) 
                    a = self.delayTest(response, responseTime, url)
                    b = self.responseTest(response, url)
                    c = self.dataTest(response, testList, url)
                    d = self.sanTest(response, url)
                    resultString = "For URL: " + url + " , " + a + " , " + b + " , " + c + " , " + d + " , " + "for input: " + i + "\n"
                    results.append(resultString)
        return "\n".join(results)


"""
Returns an array of results. one element per url.
Each element contains the url and the warnings associated with it.


"""
def getResults(urlList,inputs, responseTime, testList, username, password,vectors):    
    if "login.php" not in urlList[0]:
        urlList[0] = urlList[0] + "login.php"
    session = Auth.authenticate("q",urlList[0], username, password)
    results = []
    counter = 0
    for i in urlList:
        print("Checking: " + i)
        response = session.get(urlList[counter])
        test = Test(response)
        a = test.delayTest(response, responseTime, i)
        b = test.responseTest(response, i)
        c = test.dataTest(response, testList, i)
        if i in inputs.keys():
            d = test.vectorTest(i, session, inputs[i], vectors, responseTime, testList)
        else:
            d = ""
        resultString = i + "\n" + a + "\n" + b + "\n" + c + "\n" + d + "\n"
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
