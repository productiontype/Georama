#!/bin/bash
set -e

# Fix usWeightClass and postscriptFullName
echo "Fix name table"
python3 ../tools/fix-name-table.py

# for i in *.ttf; do
#     # python3 ../tools/fix-name-table.py
#     echo "Processing $i ..."
# done
for i in *.ttf ; do mv $i ${i//#1/} ; done

# Hinting
for i in *.ttf; do
	ttfautohint -i -n -f latn $i ${i}.hinted
  echo "Hinting $i ..."
done
for i in *.hinted ; do mv $i ${i//.hinted/} ; done

# Add DSIG table
 /usr/local/bin/gftools fix-dsig *.ttf -a -f

# Add GASP table
 /usr/local/bin/gftools fix-gasp *.ttf --autofix
rm *.ttf
for i in *.fix ; do mv $i $(basename -s .fix $i) ; done

# Fix PPEM rounding
for i in *.ttf; do
	python ../tools/gftools-fix-hinting.py $i
	echo "Setting $i PPEM rounding ..."
done
for i in *.fix ; do mv $i $(basename -s .fix $i) ; done
