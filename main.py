import illustrator_manip as ai
import connection as connect

docRef = ai.app.Application.ActiveDocument

rectRef = docRef.PathItems.Rectangle(1600, 200, 100, 100)
areaTextRef = docRef.TextFrames.AreaText(rectRef)
areaTextRef.Contents = "Hello World!"



lakesRef = docRef.Layers["Lakes"]
lakesRef.Visible = False



layerRef = docRef.Layers["Background"]
ai.setColorOfAllCountries(ai.setPrimaryColor(74, 68, 66, 86), layerRef)

layerRef = docRef.Layers["Countries"]
ai.setColorOfAllCountries(ai.setPrimaryColor(71, 65, 64, 69), layerRef)


countries = ["Germany", "Italy", "Russia", "South Africa", "United States of America", "Brazil", "China"]
for country in countries:
    ai.setColorOfCountry(ai.setPrimaryColor(0, 99, 100, 0), country, layerRef)

max_country = connect.extractMaxRate(connect.getAllCountryData(connect.getTopDate(connect.getAllDates())))

ai.setColorOfCountry(ai.setPrimaryColor(100,99,0,0), max_country[0], layerRef)

layerRef = docRef.Layers["Text"]
ai.setColorOfAllCountries(ai.setPrimaryColor(0, 0, 0, 0), layerRef)

# ExportType = Dispatch("Illustrator.ExportType")
# app.activeDocument.exportFile("results.psd")