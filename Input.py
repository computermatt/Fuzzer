from bs4 import BeautifulSoup
from urllib.request import urlopen

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
		split1 = url.split("?")
		retVal = {}
		retVal[split1[0]] = []
		split2 = split1[1].split("&")

		for val in split2:
			retVal[split1[0]].append(val.split("=")[0])

		return retVal

	'''
		Same as parseURL, but with additional "output" key with the value of the url the form is sent to as well as the type of request (post, get, etc.)
	'''
	def discoverForms(self, url):
		inputs = {}
		htmldata = urlopen(url)	
		soup = BeautifulSoup(htmldata)
		for input in soup.findAll("form"):
			inputs[input["action"]] = []
			for nm in input.findAll("input"):
				try:
					inputs[input["action"]].append(nm["name"])
				except:
					pass
		return inputs

if __name__ == '__main__':
	input = Input()
	print(input.parseURL("http://test.com/test.html?thing1=ans&thing2=hello&thing3=theresnothing3"))
	print(input.discoverForms("http://reddit.com"))

