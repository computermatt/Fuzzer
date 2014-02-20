'''
Created on Feb 19, 2014

@author: Dan
'''
import urllib.request
import urllib.parse
from bs4 import *

#root = "http://www.google.com"


'''
@param  | (string)        |  root - the url to be searched
        |                 | 
@return | (array[string]) |  pages found
'''
def search(root):
    urls = [root]
    visited = []
    
    while len(urls) > 0:
        try:
            html = urllib.request.urlopen(urls[0])
        except:
            print("Error accessing " + urls[0])
        soup = BeautifulSoup(html)
        urls.pop(0)
        print(len(urls))
        for i in soup.findAll('a', href = True):
            i["href"] = urllib.parse.urljoin(root, i["href"])
            if i["href"] not in visited and root in i["href"]:
                urls.append(i["href"])
                visited.append(i["href"])
    return visited


'''
@param  | (string)        |  root - the url to be searched
        |                 | 
@return | (array[string]) |  pages found
'''
def guess(visited, wordList):
    
    
    return 0


'''
@param  | (array[string]), string  | visited - list of urls, string - desired file name
        |                          | 
@return | nothing                  |  
'''
def output(visited,name):
    file = open(name,'w')
    for i in visited:
        file.write(i + ", ")
    

