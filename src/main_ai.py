import illustrator_manip as ai
import connection as connect

docRef = ai.app.Application.ActiveDocument

# rectRef = docRef.PathItems.Rectangle(1600, 200, 100, 100)
# areaTextRef = docRef.TextFrames.AreaText(rectRef)
# areaTextRef.Contents = "Hello World!"



# lakesRef = docRef.Layers["Lakes"]
# lakesRef.Visible = False



# layerRef = docRef.Layers["Background"]
# ai.setColorOfAllCountries(ai.setPrimaryColorCMYK(74, 68, 66, 86), layerRef)

# layerRef = docRef.Layers["Countries"]
# ai.setColorOfAllCountries(ai.setPrimaryColorCMYK(71, 65, 64, 69), layerRef)


attribute = 'active_cases'
number = 20
status = "neutral"
print ("Getting the stats you need...")
countries = connect.extractMinAttribute(connect.getAllCountryData(connect.getTopDate(connect.getAllDates())), attribute, LessThan=1000)

def findMax (countries):
    max = -1
    for i in countries:
        if (i[attribute] > max):
            max = i[attribute]
    return max

max_of_countries = findMax (countries)

countries.sort(key=lambda i: i[attribute])
print (countries)
count = 0
for i in countries:
    count += 1
    outp = str(count) + "."
    print (outp, i['country_name'], "=>", i[attribute])

# print ("Coloring the countries...")
# for country in countries:
#     print (">> ", country['country_name'])
#     try:
#         if status == "danger":
#             percentage = ( country[attribute] / max_of_countries ) * 100
#             ai.setColorOfCountry(ai.setPrimaryColorCMYK(0, percentage, 100, 0), country['country_name'], layerRef)
#         elif status == "good":
#             percentage = ( country[attribute] / max_of_countries ) * 255
#             ai.setColorOfCountry(ai.setPrimaryColorRGB(0, 255, percentage), country['country_name'], layerRef)
#         elif status == "neutral":
#             percentage = ( country[attribute] / max_of_countries ) * 255
#             ai.setColorOfCountry(ai.setPrimaryColorRGB(percentage, 0, 255), country['country_name'], layerRef)
#     except:
#         print ("!! Couldn't print", country['country_name'])


layerRef = docRef.Layers["Text"]
ai.setColorOfCountry(ai.setPrimaryColorRGB(0,0,0),"Kyrgyzstan", layerRef)
# ai.setColorOfAllCountries(ai.setPrimaryColorCMYK(0, 0, 0, 0), layerRef)

# layerRef = docRef.Layers["Text"]
# ai.setColorOfAllCountries(ai.setPrimaryColor(0, 0, 0, 0), layerRef)




## --------------Stuff which didn't work-------------
## ExportType = Dispatch("Illustrator.ExportType")
## app.activeDocument.exportFile("results.psd")
## IllustratorAPI.ExportForScreensItemToExport()

## import illustrator_2020 as IllustratorAPI

## p = IllustratorAPI.Document()
## p.Export()

## IllustratorAPI.Document.Export()
## --------------Stuff which didn't work-------------




# Save using SendKeys and Clicking
ai.saveAI("world_map_linked")
