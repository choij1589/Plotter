# Plotter
---
### Requirements
Plotter use python3-root, please confirm your system can use:
```
python3
import ROOT
exit()
```
---
### Quick Start
Check example.py to see how the plotter works. I have put the test samples in ExampleSamples directory.
```
python3 example.py
```
The code will make example plots in ExamplePlots directory. If you set many inclusive samples in
files\_incl list, than it will also draw the lines and ratios for those.

---
### How to
To make the code more flexible, I haven't automized the codes to get histograms. It is hard to know the directory structure of TFile so user should manage to get the histograms by hands. Also, normalization is not supported in the code side. User should scale the histogram if one wants to. Please see example.py to see how it works.
Basic settings are defined in PlotterBase.py
Extra settings are defined in $CHILDCLASS.py. You can change some settings in $CHILDCLASS.py for your purpose. For the example in Quick Start, it used InclAndStitched.py
To make several observalbles at one time, it is convinient to set the parameters in some place. I defined the parameters in Parameters/$PARAMETER.py. Here I define cvs\_params, hist\_params and info\_params. In the Quick Start, the code used Parameters/examples\_params.py.
