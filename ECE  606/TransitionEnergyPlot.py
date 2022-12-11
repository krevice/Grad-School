#Calculate all 1,200 transition energies using energy equation from Problem 2b
#Plot all transition energies between 0 and 1 eV (50 in total)

import itertools
import numpy as np
import matplotlib.pyplot as plt

finalStates = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3],
]
combinationFinalStates = list(itertools.product(*finalStates))
initialStates = [[0, 0, 0], [1, 0, 0], [0, 1, 0]]
Nx = []
Ny = []
Nz = []
transitionEnergy = []
filteredTransitionEnergy = []


for x in range(len(combinationFinalStates)):
    X = combinationFinalStates[x][0]
    Nx.append(X)

for x in range(len(combinationFinalStates)):
    Y = combinationFinalStates[x][1]
    Ny.append(Y)

for x in range(len(combinationFinalStates)):
    Z = combinationFinalStates[x][2]
    Nz.append(Z)

for x in range(len(combinationFinalStates)):
    for i in range(len(initialStates)):
        E = (
            (((Nx[x] + 1) ** 2) / 36)
            + (((Ny[x] + 1) ** 2) / 16)
            + ((Nz[x] + 1) ** 2)
            - (((initialStates[i][0] + 1) ** 2) / 36)
            - (((initialStates[i][1] + 1) ** 2) / 16)
            - ((initialStates[i][2] + 1) ** 2)
        )
        transitionEnergy.append(E)
for energy in transitionEnergy:
    if energy >= 0 and energy <= 1:
        filteredTransitionEnergy.append(energy)

print(sorted(filteredTransitionEnergy))
print(len(filteredTransitionEnergy))

xs = [x for x in range(len(filteredTransitionEnergy))]
plt.plot(xs, sorted(filteredTransitionEnergy), '.')
plt.ylabel('Delta E (eV)')
plt.show()
