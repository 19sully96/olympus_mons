# Session 24 Program

The files in this directory are used to solve the Session 24 programming activity.  The files earth.py and mars.py make plots of the equations of motion for a cannonball being fired at 100 m/s at 30 degrees for varying masses.  

## Usage

To run the program and make the plots, run the executable run.sh

```bash
./run.sh
```

This script automatically moves the produced plots to $WINDOWS/Pictures/numphys.  If you want move the plots somewhere else you can change the path in the run.sh file.  If you want the plots to be saved in the same directory as the executable, simply comment out the line

```bash
mv *.png $WINDOWS/Pictures/numphys
```
