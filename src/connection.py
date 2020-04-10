# importing the requests library 
import requests 

# importing the downloading library
# import urllib (Gives 403 Forbidden Error)
import urllib.request

# importing numpy for array operations
import numpy as np

# importing "heapq" to implement heap queue 
import heapq



# handling JSON and tuples
from pandas.io.json import json_normalize
import json


hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}



# api-endpoint 
BASE_URL = "https://api.thecoronamap.com"
ALL_COUNTRIES = "corona-stats"
ALL_DATES = "get-dates"
      
# api-endpoint (for country flags)
BASE_URL_CF = "https://www.countryflags.io"
# insert COUNTRY_CODE in the middle
PARAMS_CF = "flat/64.png" 


# change or restore defaults of api-endpoints
def changeApis (base_url = "https://api.thecoronamap.com", 
all_countries = "corona-stats", all_dates = "get-dates", 
base_url_cf = "https://www.countryflags.io", params_cf = "flat/64.png" ):
	global BASE_URL
	global ALL_COUNTRIES
	global ALL_DATES
	global BASE_URL_CF
	global PARAMS_CF
	BASE_URL = base_url
	ALL_COUNTRIES = all_countries
	ALL_DATES = all_dates
	BASE_URL_CF = base_url_cf
	PARAMS_CF = base_url
	return True


# sending get request and saving the response as response object 
def getAllDates():
    print("Getting all dates from server...")
    dates_response = requests.get(url = BASE_URL + "/" + ALL_DATES)
	# extracting data in json format
    print("Received all dates from server.")
    return dates_response.json()


def getTopDate(all_dates_data):
	#assuming top date is at end of array
	top_date = all_dates_data[-1]
	return top_date

def getAllCountryData(date):
	print("Getting all country data from server...")
	all_countries_response = requests.get(url = BASE_URL + "/" + ALL_COUNTRIES + "/" + date) 	
	# extracting data in json format 
	print("Received all country data from server.")
	return all_countries_response.json() 

def extractMaxRate(all_countries_data, N = 1):
	max = -1
	name = ""
	print ("---------------- Printing All Country Names ----------------")
	for country in all_countries_data:
		rate = country['dead']/country['confirmed']
		print(country)
		print (country['country_name'], "->", rate)
		if  rate > max:
			max = rate
			name = country['country_name']
	print ("------------------------------------------------------------")

	print ("\n\n")
	print ("Max country: ", name, "=>", max)
	return name, max


def extractMaxAttribute(all_countries_data, attribute, N=1):

	top_N = heapq.nlargest(N, all_countries_data, key=lambda i: i[attribute])
	count = 0
	for i in top_N:
		count += 1
		outp = str(count) + "."
		print (outp, i['country_name'], "=>", i[attribute])

	return top_N



def getCountryFlag(country):
	abbrev = getCountryAbbreviation(country)
	if (abbrev == None):
		return None


	url = BASE_URL_CF + "/" + abbrev + "/" + PARAMS_CF
	print ("Getting data from", url, "...")
	class AppURLopener(urllib.request.FancyURLopener):
		version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"
	urllib._urlopener = AppURLopener()

	# download and save in local file
	resource = urllib._urlopener.retrieve(url, os.path.abspath("../FLAGS/" + abbrev + ".png"))

	# req = urllib2.Request(url, headers=hdr)
	# page = urllib2.urlopen(req)
	# content = page.read()

	# resource = urllib.request.urlopen(url)
	# output = open(os.path.abspath("../FLAGS/" + abbrev + ".png"),"wb")
	# output.write(resource.content)
	# output.close()

def getCountryAbbreviation(country):
	output = open("../Codes.json","r")
	# output = json_normalize(output)
	data = output.read()
	data  = json.loads(data)
	# print (data)
	for i in data:
		# print (i)
		if i['country_name'] == country:
			output.close()
			return i['alpha_2']
	output.close()
	return None


