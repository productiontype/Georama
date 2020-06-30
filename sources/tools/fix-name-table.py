# fix_name_table

"""
If the shortening is applied,
it applies it only to nameID 1 and nameID 4
"""

import os
import re
from fontTools.ttLib import TTFont
import unicodedata

font_file_folder = "../fonts/Static/TTF"
output_folder_path = "../fonts/Static/TTF"


do_shorten = False
add_nameID_16_and_17 = True
add_platformID_1 = False


shortening = {
    "Condensed": "Cd",
    "Extended": "Ext",
    "Extra": "Ex",
    "Semi": "Sm",
    "Bold": "Bd",
    "Light": "Lt",
    "Black": "Blk",
    "Bold": "Bd",
    "Regular": "Rg",
    "Light": "Lt",
    "Medium": "Md",
    "Thin": "Th",
    "Italic": "It",
}


RIBBI_style = [
    "Regular",
    "Italic",
    "Bold",
    "Bold Italic"
]


fsSelection_values = {
    "Regular": 64,
    "Italic": 1,
    "Bold": 32,
    "Bold Italic": 33,
    "Not_RIBBI_italic": 1
}

macStyle_values = {
    "Regular": 0,
    "Italic": 2,
    "Bold": 1,
    "Bold Italic": 3,
    "Not_RIBBI_italic": 2
}


def return_font_file_full_path(folder, filename):
    font_file_full_path = f"{folder}/{filename}"
    return font_file_full_path

def return_filename_no_extension(filename):
    filename_no_extension = filename.split(".")[0]
    return filename_no_extension

def return_familyname(filename):
    name = return_filename_no_extension(filename).split("-")[0]
    parts = []
    i = 0
    for s in name:
        if unicodedata.category(s) == 'Lu':
            part = name[:i]
            if part:
                parts.append(part)
            name = name[i:]
            i = 0
        i += 1
    parts.append(name)

    return ' '.join(parts)

def return_stylename(filename):
    stylename = filename_no_extension.split("-")[1]
    return stylename

def split_name(string):
    splitted_name = re.findall('[A-Z][^A-Z]*', string)
    return splitted_name

def remove_spaces(string):
    string = "".join(string.split(" "))
    return string


def return_nameID_1(familyname, stylename):
    if stylename in RIBBI_style:
        nameID1 = familyname
    else:
        if "Italic" in stylename:
            stylename_without_italic = stylename.replace(" Italic", "")
            nameID1 = f"{familyname} {stylename_without_italic}"
        elif "Regular" in stylename:
            stylename_without_regular = stylename.replace(" Regular", "")
            nameID1 = f"{familyname} {stylename_without_regular}"
        else:
            nameID1 = f"{familyname} {stylename}"
    return nameID1

def return_nameID_2(stylename):
    if stylename in RIBBI_style:
        nameID2 = stylename
    else:
        if "Italic" in stylename:
            nameID2 = "Italic"
        else:
            nameID2 = "Regular"
    return nameID2

def shorten_string(string):
    new_st_as_list = []
    for sub_st in string.split(" "):
        for k, v in shortening.items():
            if k in sub_st:
                sub_st = sub_st.replace(k, shortening[k])
        new_st_as_list.append(sub_st)
    new_st = " ".join(new_st_as_list)
    return new_st


def is_RIBBI(stylename):
    if stylename in RIBBI_style:
        return True
    else:
        return False




for filename in os.listdir(font_file_folder):
    if filename.endswith(".ttf"):

        font_file_full_path = return_font_file_full_path(font_file_folder, filename)
        output_font_file_full_path = f"{output_folder_path}/{filename}"
        filename_no_extension = return_filename_no_extension(filename)
        familyname = return_familyname(filename)
        temp_stylename = return_stylename(filename)

        if temp_stylename != "Italic":
            stylename = temp_stylename.replace("Italic", " Italic")
        else:
            stylename = temp_stylename

        nameID1  = return_nameID_1(familyname, stylename)
        nameID2  = return_nameID_2(stylename)
        nameID4  = f"{familyname} {stylename}"
        nameID6  = f"{remove_spaces(familyname)}-{remove_spaces(stylename)}"
        nameID16 = familyname
        nameID17 = stylename
        nameID18 = nameID4


        if do_shorten == True:
            nameID1 = shorten_string(nameID1)
            nameID4 = shorten_string(nameID4)


        print(f"Treating {filename_no_extension}")

        ttfont = TTFont(font_file_full_path)

        try:
            ttfont["name"].removeNames(nameID=18)
            ttfont["name"].removeNames(nameID=17)
            ttfont["name"].removeNames(nameID=16)
        except:
            continue

        ttfont["name"].setName( string=nameID1,  nameID=1,  platformID=3, platEncID=1, langID=0x409 )
        ttfont["name"].setName( string=nameID2,  nameID=2,  platformID=3, platEncID=1, langID=0x409 )
        ttfont["name"].setName( string=nameID4,  nameID=4,  platformID=3, platEncID=1, langID=0x409 )
        ttfont["name"].setName( string=nameID6,  nameID=6,  platformID=3, platEncID=1, langID=0x409 )
        ttfont["name"].setName( string=nameID18,  nameID=18,  platformID=3, platEncID=1, langID=0x409 )

        if not is_RIBBI(stylename):
            ttfont["name"].setName( string=nameID16, nameID=16, platformID=3, platEncID=1, langID=0x409 )
            ttfont["name"].setName( string=nameID17, nameID=17, platformID=3, platEncID=1, langID=0x409 )

        if add_platformID_1 == True:
            ttfont["name"].setName( string=nameID1,  nameID=1,  platformID=1, platEncID=0, langID=0x0 )
            ttfont["name"].setName( string=nameID2,  nameID=2,  platformID=1, platEncID=0, langID=0x0 )
            ttfont["name"].setName( string=nameID4,  nameID=4,  platformID=1, platEncID=0, langID=0x0 )
            ttfont["name"].setName( string=nameID6,  nameID=6,  platformID=1, platEncID=0, langID=0x0 )
            if is_RIBBI(stylename):
                ttfont["name"].setName( string=nameID16, nameID=16, platformID=1, platEncID=0, langID=0x0 )
                ttfont["name"].setName( string=nameID17, nameID=17, platformID=1, platEncID=0, langID=0x0 )

            if add_nameID_16_and_17 == True and not is_RIBBI(stylename):
                ttfont["name"].setName( string=nameID16, nameID=16, platformID=1, platEncID=0, langID=0x0 )
                ttfont["name"].setName( string=nameID17, nameID=17, platformID=1, platEncID=0, langID=0x0 )


        # Duplicate existing nameRecord for the ones not modified to the mac platformID 1
        for nameRecord in ttfont["name"].names:
            if nameRecord.nameID not in [1, 2, 4, 6, 16, 17, 18, 21]:
                string = nameRecord.toStr()
                nameID = nameRecord.nameID
                platformID = nameRecord.platformID
                platEncID = nameRecord.platEncID
                langID = nameRecord.langID
                ttfont["name"].setName(string, nameID=nameID, platformID=1, platEncID=0, langID=0x0)



        # Fix fsSelection and macStyle
        nameID_2 = ttfont["name"].getName(nameID=2, platformID=3, platEncID=1).toStr()
        if is_RIBBI(stylename) == True:
            ttfont["OS/2"].fsSelection = fsSelection_values[nameID_2]
            ttfont["head"].macStyle = macStyle_values[nameID_2]
        else:
            if nameID_2 == "Regular":
                ttfont["OS/2"].fsSelection = fsSelection_values["Regular"]
                ttfont["head"].macStyle = macStyle_values["Regular"]
            else:
                ttfont["OS/2"].fsSelection = fsSelection_values["Not_RIBBI_italic"]
                ttfont["head"].macStyle = macStyle_values["Not_RIBBI_italic"]


        ttfont.save(output_font_file_full_path)

print("DONE")



