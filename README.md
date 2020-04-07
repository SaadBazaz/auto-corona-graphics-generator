# auto-corona-graphics-generator
A small editable Python script to automatically get COVID-19 stats and create Photoshop graphics

## Why?
Python is a great and easy tool used increasingly by scientists and artists for scripting, however, Adobe (creator of Photoshop and Illustrator) have yet to support Python scripting.

### Credits: 
- Python Photoshop Scripting: https://martechwithme.com/photoshop-scripting-with-python-on-windows/
- Pythoshop Python Library: https://pytoshop.readthedocs.io/
- Amazing resource, but for Javascript, VBScript and Applescript. **But**, I've found that almost EVERYTHING in the Javascript section applies to Python if you capitalize the first letter. E.g. in js, it is fillColor, but in normal COM/Python, it would be FillColor: 
https://illustrator-scripting-guide.readthedocs.io/
- Great help for general scripting, like KeySending: https://win32com.goermezer.de/microsoft/windows/controlling-applications-via-sendkeys.html

### Sources:
- For authentic COVID-19 stats: https://thecoronamap.com/
- For Country Codes: https://geotargetly.com/geo-data/country-codes
- For flags: https://www.countryflags.io/
- For World Map: http://www.vectorworldmap.com/

### **Requirements**:
- Photoshop 2019 or higher
- Illustrator 2019 or higher
- Python3

I had to tweak the World Map a bit - I manually named all 195 layers with their corresponding country names. This is necessary for any script to recognize a country. So if you require a **World Map with *properly named* layers**, you've come to the right place. You won't find it anywhere else on the internet.

> Am I the only one who names their layers?
  
