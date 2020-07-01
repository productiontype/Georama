# fix_name_table


from fontTools.ttLib import TTFont
import unicodedata

font_path = "../fonts/Variable/Georama[wdth,wght].ttf"
print(f"Treating {font_path}")
ttfont = TTFont(font_path)
ttfont["name"].setName( string='ExtraCondensed Thin', nameID=17, platformID=3, platEncID=1, langID=0x409 )
ttfont.save(font_path)

font_path = "../fonts/Variable/Georama-Italic[wdth,wght].ttf"
print(f"Treating {font_path}")
ttfont = TTFont(font_path)
ttfont["name"].setName( string='ExtraCondensed Thin Italic', nameID=17, platformID=3, platEncID=1, langID=0x409 )
ttfont.save(font_path)
