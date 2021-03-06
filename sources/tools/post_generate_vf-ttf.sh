# Fail fast
set -e

variablepath="../fonts/Variable"

echo "Adding STAT table to Georama[wdth,wght].ttf ..."
statmake --designspace ./Georama.designspace "../fonts/Variable/Georama[wdth,wght].ttf"

echo "Adding STAT table to Georama-Italic[wdth,wght] ..."
statmake --designspace ./GeoramaItalic.designspace "../fonts/Variable/Georama-Italic[wdth,wght].ttf"

for i in $variablepath/*.ttf; do

	# Add DSIG table
	gftools fix-dsig $i -a -f

	# Add GASP table
	gftools fix-gasp $i --autofix

	# Fix PPEM rounding
	echo "Setting $i PPEM rounding ..."
	gftools fix-nonhinting $i $i.fix
	mv $i.fix $i

	# Remove unwanted fvar instances
	echo "Remove unwanted fvar instances"
	python ./tools/removeUnwantedVFInstances.py $i

	# Remove unwanted tables
	echo "Remove unwanted tables"
	gftools fix-unwanted-tables $i

done

# Fix name table
echo "Fix name table"
python ./tools/fix-name-table-vf.py

# Remove unnecessary files
rm $variablepath/*backup*.ttf
