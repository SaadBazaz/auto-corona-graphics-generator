import illustrator_manip as ai
import connection

docRef = ai.app.Application.ActiveDocument

rectRef = docRef.PathItems.Rectangle(1600, 200, 100, 100)
areaTextRef = docRef.TextFrames.AreaText(rectRef)
areaTextRef.Contents = "Hello World!"

testRef = docRef.Layers["Countries"]

lakesRef = docRef.Layers["Lakes"]
lakesRef.Visible = False



layerRef = docRef.Layers["Background"]
ai.setColorOfAllCountries(ai.setPrimaryColor(74, 68, 66, 86), layerRef)

layerRef = docRef.Layers["Countries"]
ai.setColorOfAllCountries(ai.setPrimaryColor(71, 65, 64, 69), layerRef)


countries = ["Germany", "Italy", "Russia", "South Africa"]
for country in countries:
    ai.setColorOfCountry(ai.setPrimaryColor(0, 99, 100, 0), country, layerRef)

layerRef = docRef.Layers["Text"]
ai.setColorOfAllCountries(ai.setPrimaryColor(0, 0, 0, 0), layerRef)

# ExportType = Dispatch("Illustrator.ExportType")
# app.activeDocument.exportFile("results.psd")