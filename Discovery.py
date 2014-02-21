'''
Created on Feb 19, 2014

@author: Dan
'''
import urllib.request
import urllib.parse
from bs4 import *


class Discovery:

    '''
    @param  | (string)        |  root - the url to be searched
            |                 | 
    @return | (array[string]) |  pages found
    '''
    def search(self,root):
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
    @param  | (array[string]), (array[string]), (array[string])  |  urls - array of urls, wordList - array of common words, extlist - list of common extensions
            |                                                    | 
    @return | (array[string])                                    |  pages found
    '''
    def guess(self, urls, wordList, extList):
        visited = []
        
        for i in wordList:
            for j in extList:
                temp = urls[0] + i + j
                try:
                    urllib.request.urlopen(temp)
                    visited.append(temp)
                except:
                    print( temp + " doesn't exist")
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