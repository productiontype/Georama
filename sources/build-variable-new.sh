gftools builder sources/builder.yaml

TTF="fonts/variable"
for i in $TTF/*.ttf; do
    python3 sources/afterburner.py $i;
done
