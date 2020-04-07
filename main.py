# Classic Hello World example

from win32com.client import Dispatch, GetActiveObject, GetObject
# import illustrator_2020 as ai


# from IPython.utils.generics import complete_object
# import win32com.client

# @complete_object.when_type(win32com.client.DispatchBaseClass)
# def complete_dispatch_base_class(obj, prev_completions):
#     try:
#         ole_props = set(obj._prop_map_get_).union(set(obj._prop_map_put_))
#         return list(ole_props) + prev_completions
#     except AttributeError:
#         pass



# Start up an Illustrator application
app = Dispatch('Illustrator.Application')

# Or get Reference to already running Illustrator application instance
# app = GetActiveObject("Illustrator.Application")
app.Open(r"C:\Users\care\Desktop\PhotoshopScript\AIs\world_map.ai")

docRef = app.Application.ActiveDocument
# docRef = app.Documents.Add()
rectRef = docRef.PathItems.Rectangle(1600, 200, 100, 100)
areaTextRef = docRef.TextFrames.AreaText(rectRef)
areaTextRef.Contents = "Hello World!"

testRef = docRef.Layers["Countries"]
# # print (testRef.)
# subRef = testRef.PathItems["Mali"]
# subRef.Hidden = False


lakesRef = docRef.Layers["Lakes"]
lakesRef.Visible = False

# var newRGBColor = new RGBColor()
# newRGBColor.red = 255
# newRGBColor.green = 255
# newRGBColor.blue = 0
primaryColor = Dispatch("Illustrator.CMYKColor")
secondaryColor = Dispatch("Illustrator.CMYKColor")

#Bright Red
# color.Cyan = 0
# color.Magenta = 99
# color.Yellow = 100
# color.Black = 0


#Charcoal
# color.Cyan = 71
# color.Magenta = 65
# color.Yellow = 64
# color.Black = 69

#Black
# color.Cyan = 74
# color.Magenta = 68
# color.Yellow = 66
# color.Black = 86

#set Primary Color
def setPrimaryColor(cyan, magenta, yellow, black):
    global primaryColor
    primaryColor.Cyan = cyan
    primaryColor.Magenta = magenta
    primaryColor.Yellow = yellow
    primaryColor.Black = black
    return primaryColor

#set Secondary Color
def setSecondaryColor(cyan, magenta, yellow, black):
    global secondaryColor
    secondaryColor.Cyan = cyan
    secondaryColor.Magenta = magenta
    secondaryColor.Yellow = yellow
    secondaryColor.Black = black
    return secondaryColor


#Brute Force Find
def setColorOfCountry (color, countryName, layerRef):
    try:
        country = layerRef.PathItems[countryName]
        country.FillColor = color
    except:
        try:
            scattered_country = layerRef.CompoundPathItems[countryName]
            for territory in scattered_country.PathItems:
                territory.FillColor = color
        except:
            grouped_country = layerRef.GroupItems[countryName]
            for territory in grouped_country.PathItems:
                territory.FillColor = color

##Brute Set All
def setColorOfAllCountries (color, layerRef):
    for country in layerRef.PathItems:
        country.FillColor = color

    for scattered_country in layerRef.CompoundPathItems:
        for territory in scattered_country.PathItems:
            territory.FillColor = color

    for grouped_country in layerRef.GroupItems:
        for territory in grouped_country.PathItems:
            territory.FillColor = color


layerRef = docRef.Layers["Background"]
setColorOfAllCountries(setPrimaryColor(74, 68, 66, 86), layerRef)

layerRef = docRef.Layers["Countries"]
setColorOfAllCountries(setPrimaryColor(71, 65, 64, 69), layerRef)


countries = ["Germany", "Italy", "Russia", "South Africa"]
for country in countries:
    setColorOfCountry(setPrimaryColor(0, 99, 100, 0), country, layerRef)

layerRef = docRef.Layers["Text"]
setColorOfAllCountries(setPrimaryColor(0, 0, 0, 0), layerRef)

# layer_date = docRef.Layers["Countries"]
# text_of_layer_date = layer_date.TextFrames.
# text_of_layer_date.Contents = "Hello beast"