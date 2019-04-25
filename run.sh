#! /bin/bash

# execute python scripts for earth and mars
python earth.py
python mars.py

# move figures to Pictures directory
mv *.png $WINDOWS/Pictures/numphys

echo "Done"
