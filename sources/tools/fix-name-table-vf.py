# fix_name_table


from fontTools.ttLib import TTFont

font_path = "../fonts/Variable/Georama[wdth,wght].ttf"
print(f"Treating {font_path}")
ttfont = TTFont(font_path)
ttfont["name"].setName(
    string="ExtraCondensed", nameID=16, platformID=3, platEncID=1, langID=0x409
)
ttfont["name"].setName(
    string="Thin", nameID=17, platformID=3, platEncID=1, langID=0x409
)
ttfont["OS/2"].usWeightClass = 100
ttfont.save(font_path)

font_path = "../fonts/Variable/Georama-Italic[wdth,wght].ttf"
print(f"Treating {font_path}")
ttfont = TTFont(font_path)
ttfont["name"].setName(
    string="ExtraCondensed", nameID=16, platformID=3, platEncID=1, langID=0x409
)
ttfont["name"].setName(
    string="Thin Italic", nameID=17, platformID=3, platEncID=1, langID=0x409
)
ttfont["OS/2"].usWeightClass = 100
ttfont.save(font_path)
