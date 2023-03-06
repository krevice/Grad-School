# plot stress-strain hysteresis loops
import matplotlib.pyplot as plt
import numpy
import numpy as np

# create lists for variables to plot
load = []
displacement = []

# total cross-sectional area of solder bumps (units m^2)
Atotal = (((0.730/2)**2)*numpy.pi/1000000)*8

# stand-off height (units um)
standOffHeight = 150

# open .dat file and read it
# change file path to correct path to .dat file
with open(r'path\to\SS_C3PO_25C.dat', 'r') as f:
    lines = f.readlines()

# create lists for measured variables time, load, displacement as read from the .dat file
for line in lines:
    columns = line.strip().split()
    try:
        loadValues = float(columns[6])
        load.append(loadValues)
        displacementValues = float(columns[3])
        displacement.append(displacementValues)
    except ValueError:
        pass

# calculate stress from load values and total solder area (units MPa)
stress = (np.sqrt(3)*(np.array(load)/Atotal))/1000000

# calculate strain from displacement values and stand-off height (unitless)
strain = (np.array(displacement)/standOffHeight)/np.sqrt(3)

plt.plot(strain, stress)

# add title and label axes
plt.title('Stress-Strain Hysteresis Loop')
plt.xlabel('Strain')
plt.ylabel('Stress (MPa)')

# plot the figures
plt.show()
