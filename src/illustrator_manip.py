# Classic Hello World example

from win32com.client import Dispatch, GetActiveObject, GetObject
# import illustrator_2020 as ai

import os

# from IPython.utils.generics import complete_object
# import win32com.client

# @complete_object.when_type(win32com.client.DispatchBaseClass)
# def complete_dispatch_base_class(obj, prev_completions):
#     try:
#         ole_props = set(obj._prop_map_get_).union(set(obj._prop_map_put_))
#         return list(ole_props) + prev_completions
#     except AttributeError:
#         pass


# Or get Reference to already running Illustrator application instance
# app = GetActiveObject("Illustrator.Application")

# docRef = app.Documents.Add()

# # print (testRef.)
# subRef = testRef.PathItems["Mali"]
# subRef.Hidden = False

# Start up an Illustrator application
print("Starting Illustrator...")
app = Dispatch('Illustrator.Application')

print("Opening world_map.ai...")
app.Open(os.path.abspath('../AIs/world_map.ai'))


print("Setting up primary and secondary colors (CMYK and RGB)...")
primaryColorCMYK = Dispatch("Illustrator.CMYKColor")
secondaryColorCMYK = Dispatch("Illustrator.CMYKColor")

primaryColorRGB = Dispatch("Illustrator.RGBColor")
secondaryColorRGB = Dispatch("Illustrator.RGBColor")

# var newRGBColor = new RGBColor()
# newRGBColor.red = 255
# newRGBColor.green = 255
# newRGBColor.blue = 0


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

#set Primary Color CMYK
def setPrimaryColorCMYK(cyan, magenta, yellow, black):
    print("Setting PrimaryColorCMYK.")
    global primaryColorCMYK
    primaryColorCMYK.Cyan = cyan
    primaryColorCMYK.Magenta = magenta
    primaryColorCMYK.Yellow = yellow
    primaryColorCMYK.Black = black
    return primaryColorCMYK

#set Secondary Color CMYK
def setSecondaryColorCMYK(cyan, magenta, yellow, black):
    print("Setting SecondaryColorCMYK.")
    global secondaryColorCMYK
    secondaryColorCMYK.Cyan = cyan
    secondaryColorCMYK.Magenta = magenta
    secondaryColorCMYK.Yellow = yellow
    secondaryColorCMYK.Black = black
    return secondaryColorCMYK


#set Primary Color RGB
def setPrimaryColorRGB(red, green, blue):
    print("Setting PrimaryColorRGB.")
    global primaryColorRGB
    primaryColorRGB.Red = red
    primaryColorRGB.Green = green
    primaryColorRGB.Blue = blue
    return primaryColorRGB

#set Primary Color RGB
def setSecondaryColorRGB(red, green, blue):
    print("Setting SecondaryColorRGB.")
    global secondaryColorRGB
    secondaryColorRGB.Red = red
    secondaryColorRGB.Green = green
    secondaryColorRGB.Blue = blue
    return secondaryColorRGB


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
            try:
                grouped_country = layerRef.GroupItems[countryName]
                for territory in grouped_country.PathItems:
                    territory.FillColor = color
            except:
                # try:
                text_country = layerRef.TextFrames[countryName]
                print("TYPENAME IS ", text_country.Typename)
                text_country.TextPath.FillColor = color
                # except:
                #     print("Couldn't find ", countryName, "anywhere!")

##Brute Set All
def setColorOfAllCountries (color, layerRef):
    print("Setting color of all nested layers.")
    for country in layerRef.PathItems:
        country.FillColor = color

    for scattered_country in layerRef.CompoundPathItems:
        for territory in scattered_country.PathItems:
            territory.FillColor = color

    for grouped_country in layerRef.GroupItems:
        for territory in grouped_country.PathItems:
            territory.FillColor = color

    for text_country in layerRef.TextFrames:
        print("TYPENAME IS ", text_country.Typename)
        text_country.TextPath.FillColor = color


##Save File
def saveAI(filename = None):
    print("Starting save process. Please be alert.")
    import win32com.client
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.Run("Illustrator")
    shell.AppActivate("Illustrator")
    import time

    # Thinking time
    time.sleep(3)

    # shell.SendKeys("^a", 0)
    print ("Sending keys...")

    # Change Active Tab manually
    # shell.SendKeys("%{TAB}", 0)
    # time.sleep(1)

    # Sanity test
    shell.SendKeys("{TAB}", 0)
    time.sleep(1)

    # Use the main tool... (Wait for it...)
    shell.SendKeys("^A", 1)
    time.sleep(1)

    # Click Adobe Illustrator to activate the screen (Idk, but okay)
    import pyautogui
    pyautogui.click()
    time.sleep(1)

    # I don't know why it opens the Save As dialog. Oh well...
    shell.SendKeys("^S", 1)
    time.sleep(1)

    if (filename != None):
        shell.SendKeys(filename, 1)
    time.sleep(1)
    shell.SendKeys("~", 1)
    time.sleep(1)
    shell.SendKeys("~", 1)
    time.sleep(1)
    shell.SendKeys("~", 1)
    print ("Keys sent.")


# # layerRef = docRef.Layers["Background"]
# # setColorOfAllCountries(setPrimaryColor(74, 68, 66, 86), layerRef)

# # layerRef = docRef.Layers["Countries"]
# # setColorOfAllCountries(setPrimaryColor(71, 65, 64, 69), layerRef)


# # countries = ["Germany", "Italy", "Russia", "South Africa"]
# # for country in countries:
# #     setColorOfCountry(setPrimaryColor(0, 99, 100, 0), country, layerRef)

# # layerRef = docRef.Layers["Text"]
# # setColorOfAllCountries(setPrimaryColor(0, 0, 0, 0), layerRef)

# # ExportType = Dispatch("Illustrator.ExportType")
# app.activeDocument.exportFile("results.psd")



# layer_date = docRef.Layers["Countries"]
# text_of_layer_date = layer_date.TextFrames.
# text_of_layer_date.Contents = "Hello beast"