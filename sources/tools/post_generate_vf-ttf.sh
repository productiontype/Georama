set -e

echo "Adding STAT table to Georama-VF.ttf ..."
statmake --designspace ../Georama.designspace "../fonts/Variable/Georama[wdth,wght].ttf"

echo "Adding STAT table to GeoramaItalic-VF.ttf ..."
statmake --designspace ../GeoramaItalic.designspace "../fonts/Variable/Georama-Italic[wdth,wght].ttf"

# Hinting
for i in ../fonts/Variable/*.ttf; do
	./tools/ttfautohint-vf --stem-width-mode nnn $i ${i}.hinted
	echo "Hinting $i ..."
done
for i in ../fonts/Variable/*.hinted ; do mv $i ${i//.hinted/} ; done
