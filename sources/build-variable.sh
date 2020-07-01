
# Georama fonts build notes
# --------------------------------------------------------------------------------
#
# Requirements
#
# - afdko/autohint: https://github.com/adobe-type-tools/afdko
# - fontbakery: https://github.com/googlefonts/fontbakery
# - fontmake: https://github.com/googlei18n/fontmake
# - fonttools: https://github.com/fonttools/fonttools
# - sfnt2woff-zopfli: https://github.com/bramstein/sfnt2woff-zopfli
# - statmake: https://github.com/daltonmaag/statmake/
# - ttfautohint: https://www.freetype.org/ttfautohint/
# - woff2_compress: https://github.com/google/woff2
#
# --------------------------------------------------------------------------------

rm "../fonts/Variable/*.ttf"

# Fail fast
set -e

# Generate VF
fontmake -m Georama.designspace -o variable --output-path "../fonts/Variable/Georama[wdth,wght].ttf"
fontmake -m GeoramaItalic.designspace -o variable --output-path "../fonts/Variable/Georama-Italic[wdth,wght].ttf"

# Post process vf-ttf
sh tools/post_generate_vf-ttf.sh
