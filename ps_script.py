import win32com.client
import os

# importing the requests library 
import requests 
  
# api-endpoint 
BASE_URL = "https://api.thecoronamap.com"
ALL_COUNTRIES = "corona-stats"
ALL_DATES = "get-dates"
      
# api-endpoint (for country flags)
BASE_URL_CF = "https://www.countryflags.io"
# insert COUNTRY_CODE in the middle
PARAMS_CF = "flat/64.png" 


# sending get request and saving the response as response object 
dates_response = requests.get(url = BASE_URL + "/" + ALL_DATES)

# extracting data in json format
all_dates_data = dates_response.json();
print("\n\n\n\n\n")
print ("---------------- Printing All Dates ----------------")
print (all_dates_data)
print ("----------------------------------------------------")
print("\n\n\n\n\n")
#display top date
top_date = all_dates_data[len(all_dates_data) - 1]
print ("The most recent date is", top_date)





all_countries_response = requests.get(url = BASE_URL + "/" + ALL_COUNTRIES + "/" + top_date) 
  
# extracting data in json format 
all_countries_data = all_countries_response.json() 
print("\n\n\n\n\n")
print ("---------------- Printing All Country Stats for ", top_date, " ----------------")
print(all_countries_data)
print ("-------------------------------------------------------------------------------")
print("\n\n\n\n\n")


max = -1
name = ""
print ("---------------- Printing All Country Names ----------------")
for country in all_countries_data:
	rate = country['dead']/country['confirmed']
	print (country['country_name'], "->", rate)
	if  rate > max:
		max = rate
		name = country['country_name']
print ("------------------------------------------------------------")

print ("\n\n")
print ("Max country: ", name, "=>", max)


psApp = win32com.client.Dispatch("Photoshop.Application")

psApp.Open(r"C:\Users\care\Desktop\PhotoshopScript\image.psd")

doc = psApp.Application.ActiveDocument

layer_date = doc.ArtLayers["Date"]
text_of_layer_date = layer_date.TextItem
text_of_layer_date.contents = str(top_date)

layer_country_name = doc.ArtLayers["Country.Name"]
text_of_layer_country_name = layer_country_name.TextItem
text_of_layer_country_name.contents = str(name)

layer_rate = doc.ArtLayers["Rate"]
text_of_layer_rate = layer_rate.TextItem
text_of_layer_rate.contents = str(rate)