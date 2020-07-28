# Fail fast
set -e

variablepath="../fonts/Variable"

echo "Adding STAT table to Georama[wdth,wght].ttf ..."
statmake --designspace ./Georama.designspace "../fonts/Variable/Georama[wdth,wght].ttf"

echo "Adding STAT table to Georama-Italic[wdth,wght] ..."
statmake --designspace ./GeoramaItalic.designspace "../fonts/Variable/Georama-Italic[wdth,wght].ttf"

for i in $variablepath/*.ttf; do

	# Hinting
	echo "Hinting $i"
	./tools/ttfautohint-vf --stem-width-mode nnn $i ${i}.hinted
	mv ${i}.hinted $i

	# Add DSIG table
	gftools fix-dsig $i -a -f

	# Add GASP table
	gftools fix-gasp $i --autofix
	# mv ${i}.fix $i

	# Fix PPEM rounding
	echo "Setting $i PPEM rounding ..."
	gftools fix-hinting $i
	mv ${i}.fix $i

	# Remove unwanted fvar instances
	echo "Remove unwanted fvar instances"
	python ./tools/removeUnwantedVFInstances.py $i

done

# Fix name table
echo "Fix name table"
python3 ./tools/fix-name-table-vf.py
