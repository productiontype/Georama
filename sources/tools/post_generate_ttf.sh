set -e

staticpath="../fonts/Static/TTF"

# Fix name table
echo "Fix name table"
python3 ./tools/fix-name-table-static.py

for i in $staticpath/*.ttf; do

	# Hinting
	echo "Hinting $i"
	ttfautohint -i -n -f latn $i $i.hinted
	mv ${i}.hinted $i

	# Add DSIG table
	gftools fix-dsig $i -a -f

	# Add GASP table
	gftools fix-gasp $i --autofix
	mv ${i}.fix $i

	# Fix PPEM rounding
	echo "Setting $i PPEM rounding ..."
	gftools fix-hinting $i
	mv ${i}.fix $i

done
