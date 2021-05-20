import sys
from fontTools.ttLib import TTFont

path = sys.argv[-1]
ttFont = TTFont(path)

print(f"Afterburner: Setting fvar instance wdth values of {ttFont} to 100")

for instance in ttFont["fvar"].instances:
    instance.coordinates["wdth"] = 100

ttFont.save(path)
