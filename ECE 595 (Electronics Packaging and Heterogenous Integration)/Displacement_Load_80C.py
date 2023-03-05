import matplotlib.pyplot as plt

# create lists for variables to plot
time = []
load = []
displacement = []

# open .dat file and read it
# change file path to correct path to .dat file
with open(r'path\to\SS_C3PO_80C.dat', 'r') as f:
    lines = f.readlines()

# create lists for measured variables time, load, displacement as read from the .dat file
for line in lines:
    columns = line.strip().split()
    try:
        timeValues = float(columns[1])
        time.append(timeValues)
        loadValues = float(columns[6])
        load.append(loadValues)
        displacementValues = float(columns[10])
        displacement.append(displacementValues)
    except ValueError:
        pass

# set subplot so that the x-axis (time) is shared for both load and displacement plots
fig, (ax1, ax2) = plt.subplots(nrows=2,ncols=1,sharex=True)

# set the x-axis (time) and y-axis (displacement) to display only the first 100000 data points
ax1.plot(time[0:100000], displacement[0:100000])
ax1.set_ylabel('Displacement (um)')

# set the x-axis (time) and y-axis (load) to display only the first 100000 data points
ax2.plot(time[0:100000], load[0:100000])
ax2.set_ylabel('Load (N)')

# x-axis (time) label
fig.text(0.5, 0.04, 'Time', ha='center')

# add title to combined plots
fig.suptitle('Experimental Solder, 80C')

#plot the figures
plt.show()
