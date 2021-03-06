import sys
import fontTools.ttLib
from fontbakery.constants import PlatformID, WindowsEncodingID, WindowsLanguageID

file = sys.argv[1]
ttFont = fontTools.ttLib.TTFont(file)

allowed_stylenames = (
    "Thin",
    "ExtraLight",
    "Light",
    "Regular",
    "Medium",
    "SemiBold",
    "Bold",
    "ExtraBold",
    "Black",
    "ExtraBlack",
    "Thin Italic",
    "ExtraLight Italic",
    "Light Italic",
    "Italic",
    "Medium Italic",
    "SemiBold Italic",
    "Bold Italic",
    "ExtraBold Italic",
    "Black Italic",
    "ExtraBlack Italic",
)


def forbidden_instance():
    for instance in ttFont["fvar"].instances:
        name = (
            ttFont["name"]
            .getName(
                instance.subfamilyNameID,
                PlatformID.WINDOWS,
                WindowsEncodingID.UNICODE_BMP,
                WindowsLanguageID.ENGLISH_USA,
            )
            .toUnicode()
        )

        if name not in allowed_stylenames:
            return instance


while forbidden_instance():
    instance = forbidden_instance()
    ttFont["fvar"].instances.remove(instance)
    print("Deleted", instance)

ttFont.save(file)
