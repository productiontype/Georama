set -e

staticpath="../fonts/Static/TTF"

# Fix usWeightClass and postscriptFullName
echo "Fix name table"
python3 ./tools/fix-name-table.py

# Hinting
for i in $staticpath/*.ttf; do
	echo "Hinting $i"
	ttfautohint -i -n -f latn $i $i.hinted
done
for i in $staticpath/*.hinted ; do mv $i ${i//.hinted/} ; done

# Add DSIG table
gftools fix-dsig $staticpath/*.ttf -a -f

# Add GASP table
gftools fix-gasp $staticpath/*.ttf --autofix
for i in $staticpath/*.fix ; do mv $i $staticpath/$(basename -s .fix $i) ; done

# Fix PPEM rounding
for i in $staticpath/*.ttf; do
	echo "Setting $i PPEM rounding ..."
	gftools fix-hinting $i
done
for i in $staticpath/*.fix ; do mv $i $staticpath/$(basename -s .fix $i) ; done
