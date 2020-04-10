import illustrator_manip as ai
import connection as connect

docRef = ai.app.Application.ActiveDocument

rectRef = docRef.PathItems.Rectangle(1600, 200, 100, 100)
areaTextRef = docRef.TextFrames.AreaText(rectRef)
areaTextRef.Contents = "Hello World!"



# lakesRef = docRef.Layers["Lakes"]
# lakesRef.Visible = False



# layerRef = docRef.Layers["Background"]
# ai.setColorOfAllCountries(ai.setPrimaryColor(74, 68, 66, 86), layerRef)

layerRef = docRef.Layers["Countries"]
ai.setColorOfAllCountries(ai.setPrimaryColorCMYK(71, 65, 64, 69), layerRef)

# max_country = connect.extractMaxRate(connect.getAllCountryData(connect.getTopDate(connect.getAllDates())))

# attribute = 'recovered'
# number = 20
# status = "good"
# countries = connect.extractMaxAttribute(connect.getAllCountryData(connect.getTopDate(connect.getAllDates())), attribute, number)


# for country in countries:
#     if status == "danger":
#         percentage = ( country[attribute] / countries[0][attribute] ) * 100
#         ai.setColorOfCountry(ai.setPrimaryColorCMYK(0, percentage, 100, 0), country['country_name'], layerRef)
#     elif status == "good":
#         percentage = ( country[attribute] / countries[0][attribute] ) * 255
#         ai.setColorOfCountry(ai.setPrimaryColorRGB(0, 255, percentage), country['country_name'], layerRef)

# ai.setColorOfCountry(ai.setPrimaryColor(100,99,0,0), max_country[0], layerRef)

# layerRef = docRef.Layers["Text"]
# ai.setColorOfAllCountries(ai.setPrimaryColor(0, 0, 0, 0), layerRef)

# layerRef = docRef.Layers["Text"]
# ai.setColorOfAllCountries(ai.setPrimaryColor(0, 0, 0, 0), layerRef)


## ExportType = Dispatch("Illustrator.ExportType")
## app.activeDocument.exportFile("results.psd")
## IllustratorAPI.ExportForScreensItemToExport()

## import illustrator_2020 as IllustratorAPI

## p = IllustratorAPI.Document()
## p.Export()

## IllustratorAPI.Document.Export()



# Save using SendKeys and Clicking
ai.saveAI("world_map_linked")
