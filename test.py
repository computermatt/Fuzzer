'''
Created on Feb 20, 2014

@author: Dan
'''
from crawler import search
from crawler import guess


url1 = "http://www.se.rit.edu"
url2 = "https://www.google.com"
url3 = "http://www.morrisauto.com"

array1 = [url1,url2,url3]

list1 = ["index", "admin", "login", "user", "main", "wiki"]
list2 = [".html", ".php", ".pdf", ""]

a = search(url3)

guess(a, list1, list2)