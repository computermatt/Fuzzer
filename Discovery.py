'''
Created on Feb 19, 2014

@author: Dan
'''
import urllib.request
import urllib.parse
from bs4 import *
import requests

class Discovery:
    def __init__(self, session):
        self.session = session

    '''
    @param  | (string)        |  root - the url to be searched
            |                 | 
    @return | (array[string]) |  pages found
    '''
    def search(self,root):
        urls = [root]
        visited = []
        cache = {}        
        while len(urls) > 0:
            try:
                html = self.session.get(urls[0]).text
            except:
                print("Error accessing " + urls[0])
            soup = BeautifulSoup(html)
            cache[urls[0]] = soup
            urls.pop(0)
            for i in soup.findAll('a', href = True):
                i["href"] = urllib.parse.urljoin(root, i["href"])
                if i["href"] not in visited and root in i["href"]:
                    urls.append(i["href"])
                    visited.append(i["href"])
        return visited,cache
    
    
    '''
    @param  | (array[string]), (array[string]), (array[string])  |  urls - array of urls, wordList - array of common words, extlist - list of common extensions
            |                                                    | 
    @return | (array[string])                                    |  pages found
    '''
    def guess(self, url, wordList, extList):
        visited = []
        
        for i in wordList:
            for j in extList:
                temp = url + i + j
                val = self.session.get(temp)
                if val.status_code != 404:
                    visited.append(temp)
        return visited
    
    '''
    @param  | (array[string]), string  | visited - list of urls, string - desired file name
            |                          | 
    @return | nothing                  |  
    '''
    def output(self, visited,name):
        file = open(name,'w')
        for i in visited:
            file.write(i + ", ")
