#!/bin/bash
set -e

echo "Adding STAT table to Georama-VF.ttf ..."
statmake --designspace ../Georama.designspace Georama-VF.ttf

echo "Adding STAT table to GeoramaItalic-VF.ttf ..."
statmake --designspace ../GeoramaItalic.designspace GeoramaItalic-VF.ttf

# Hinting
for i in *.ttf; do
	../tools/ttfautohint-vf --stem-width-mode nnn $i ${i}.hinted
  echo "Hinting $i ..."
done
for i in *.hinted ; do mv $i ${i//.hinted/} ; done