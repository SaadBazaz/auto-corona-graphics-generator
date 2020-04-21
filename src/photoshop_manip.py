import win32com.client
import os

psApp = None
doc = []

def openPSD(path):
	global psApp
	if (psApp == None): 
		psApp = win32com.client.Dispatch("Photoshop.Application")
	psApp.Open(path)
	doc.append(psApp.Application.ActiveDocument)
	ActiveDoc = doc[-1]

def changeText(layername, newtext):
	global psApp
	if (psApp == None):
		return false
	layer_date = psApp.Application.ActiveDocument.ArtLayers[layername]
	text_of_layer_date = layer_date.TextItem
	text_of_layer_date.contents = str(newtext)
	return true