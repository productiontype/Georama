#!/bin/bash
set -e

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

# Generate fonts
fontmake -m Georama.designspace -o variable
fontmake -m GeoramaItalic.designspace -o variable
fontmake -m Georama-Static.designspace -i -o ttf --expand-features-to-instances
fontmake -m GeoramaItalic-Static.designspace -i -o ttf --expand-features-to-instances

# Post process vf-ttf
cd variable_ttf
sh ../tools/post_generate_vf-ttf.sh

# Post process static ttf
cd ../instance_ttf
sh ../tools/post_generate_ttf.sh

# Generate webfonts
for i in *.ttf; do
	echo "Processing $i to  => woff"
    sfnt2woff-zopfli -m ../webfont_metadata.xml $i
    woff2_compress $i
done

mkdir ../woff2
for i in *.woff2; do
    mv $i ../woff2
done

mkdir ../woff
for i in *.woff; do
    mv $i ../woff
done