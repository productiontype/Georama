
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


# Generate Static Fonts
staticpath="../fonts/Static/TTF"
webfont_metadata="./webfont_metadata.xml"

rm -r $staticpath/*.ttf

# Fail fast
set -e

fontmake -m Georama-Static.designspace -i -o ttf --output-dir $staticpath --expand-features-to-instances
fontmake -m GeoramaItalic-Static.designspace -i -o ttf --output-dir $staticpath --expand-features-to-instances

# Post process static ttf
sh ./tools/post_generate_ttf.sh

# # Generate webfonts
# for i in $staticpath/*.ttf; do
#     file_name=`basename $i`
#     file_name="${file_name%.ttf}"
#     echo "Export "$file_name.woff

#     sfnt2woff -m $webfont_metadata $i
#     woff2_compress $i
# done

# for i in $staticpath/*.woff2; do
#     mv $i $staticpath/../woff2
# done

# for i in $staticpath/*.woff; do
#     mv $i $staticpath/../woff
# done


# Delete instances, we don't need them. If you need to look at instances, comment-out this line and repeat
rm -r instances
