from bs4 import BeautifulSoup
from urllib.request import * 
import http.cookiejar
import requests

class Input:

	'''
		Input:URL
		Output: {
				baseURL:[
						something,
						anothering
					]
			}
		This is a silly and naive way of doing it, but it works
	'''
	def parseURL(self, url):
		try:
			split1 = url.split("?")
			retVal = [] 
			split2 = split1[1].split("&")

			for val in split2:
				retVal.append(val.split("=")[0])
		except:
			retVal = [] 
		return retVal

	'''
		Same as parseURL
	'''
	def discoverForms(self, soup):
		inputs = [] 
		for input in soup.findAll("form"):
			for nm in input.findAll("input"):
				try:
					inputs.append(nm["name"])
				except:
					pass
		return inputs

	def discoverCookies(self, session):
		return session.cookies 

if __name__ == '__main__':
	input = Input(requests.Session())
	print(input.parseURL("http://yogi.se.rit.edu/~swen-331/01/index.html"))

