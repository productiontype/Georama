#!/usr/bin/env python
import xml.etree.ElementTree as ET

import sys, os
from fontTools.ttLib import TTFont
from fontTools.ttx import makeOutputFileName

inputTTF = sys.argv[1]
font = TTFont(inputTTF)
filename = os.path.splitext(inputTTF)[0]
extension = os.path.splitext(inputTTF)[1]

# WeightClass definitions
wght={
"UltraLite": 100,
"UltraLight": 100,
"ExtraLite": 200,
"ExtraLight": 200,
"Lite": 300, 
"Light": 300,
"Regular":400,
"":400,
"SemiBold":600,
"Bold":700,
"Blak":800, 
"Black":800,
"UltraBlak":900,
"UltraBlack":900
}


familyname = u"Georama"
weightname = filename.replace('Italic','').replace('It','').split("-")[1]
widthname = filename.replace(familyname,'').split("-")[0]
italicname = ""
if filename.endswith("Italic"):
	italicname = "Italic"
elif filename.endswith("It"):
	italicname = "It"

postscriptFullName = u"{0} {1} {2} {3}".format(familyname, widthname, weightname, italicname ).replace('  ', ' ').replace('  ', ' ').rstrip()

# Set postscriptFullName
# print("\t{0}".format(postscriptFullName))
# setName(self, string, nameID, platformID, platEncID, langID):
font['name'].setName(postscriptFullName,4,3,1,1033)

# getName(self, nameID, platformID, platEncID, langID=None)
# print str(font['name'].getName(1,3,1)).replace(chr(0),"")

# for x in font['name'].names:
# 	print x.nameID, x.platformID, x.platEncID, str(x).replace(chr(0),"")


# Set usWeightClass
font['OS/2'].usWeightClass = wght[weightname]
# font['OS/2'].panose.bWeight = wght[weightname][1]


outputTTF = makeOutputFileName(inputTTF, '', extension)
font.save(outputTTF)