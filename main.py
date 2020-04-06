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
color = Dispatch("Illustrator.CMYKColor")
color.Cyan = 0
color.Magenta = 99
color.Yellow = 100
color.Black = 0




#Brute Force Find
try:
    country = testRef.PathItems["Brazil"]
    country.FillColor = color
except:
    try:
        scattered_country = testRef.CompoundPathItems["Brazil"]
        for territory in scattered_country.PathItems:
            territory.FillColor = color
    except:
        grouped_country = testRef.GroupItems["Brazil"]
        for territory in grouped_country.PathItems:
            territory.FillColor = color


# for country in testRef.PathItems:
#     country.FillColor = color

# for scattered_country in testRef.CompoundPathItems:
#     for territory in scattered_country.PathItems:
#         territory.FillColor = color

# for grouped_country in testRef.GroupItems:
#     for territory in grouped_country.PathItems:
#         territory.FillColor = color



# malay = testRef.CompoundPathItems["Malaysia"]
# for i in malay.PathItems:
#     i.FillColor = color


# layer_date = docRef.Layers["Countries"]
# text_of_layer_date = layer_date.TextFrames.
# text_of_layer_date.Contents = "Hello beast"