#Script to calculate corresponding which transition energies have a nonzero optical matrix element

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
Nxf = []
Nyf = []
Nzf = []
Nxi = []
Nyi = []
Nzi = []
transitionEnergy = []
filteredTransitionEnergy = []
opticalEnergy = []
Lx = 10
Ly = 10
Lz = 10
yy = 5
zz = 5
xx = 5

for x in range(len(combinationFinalStates)):
    Xf = combinationFinalStates[x][0]
    Nxf.append(Xf)
for x in range(len(combinationFinalStates)):
    Yf = combinationFinalStates[x][1]
    Nyf.append(Yf)
for x in range(len(combinationFinalStates)):
    Zf = combinationFinalStates[x][2]
    Nzf.append(Zf)
for x in range(len(initialStates)):
    Xi = initialStates[x][0]
    Nxi.append(Xi)
for x in range(len(initialStates)):
    Yi = initialStates[x][1]
    Nyi.append(Yi)
for x in range(len(initialStates)):
    Zi = initialStates[x][2]
    Nzi.append(Zi)
for x in range(len(combinationFinalStates)):
    for i in range(len(initialStates)):
        E1 = (
            (((Nxf[x] + 1) ** 2) / 36)
            + (((Nyf[x] + 1) ** 2) / 16)
            + ((Nzf[x] + 1) ** 2)
            - (((Nxi[i] + 1) ** 2) / 36)
            - (((Nyi[i] + 1) ** 2) / 16)
            - ((Nzi[i] + 1) ** 2)
        )
        transitionEnergy.append(E1)

        E2 = (
            (4 * Ly / ((np.pi ** 2) * Lx * Lz))
            * np.sin((np.pi / Lz) * (Nzi[i] + 1) * (zz + (Lz / 2)))
            * np.sin((np.pi / Lz) * (Nzf[x] + 1) * (zz + (Lz / 2)))
            * np.sin((np.pi / Lx) * (Nxi[i] + 1) * (xx + (Lx/ 2)))
            * np.sin((np.pi / Lx) * (Nxf[i] + 1) * (xx + (Lx / 2)))
            * (
                (
                    (np.cos(np.pi * (Nyi[i] - Nyf[x])) / ((Nyi[i] - Nyf[x]) ** 2))
                    - (
                        np.cos(np.pi * ((Nyi[i] + Nyf[x] + 2) ** 2))
                        / ((Nyf[x] + Nyi[i] + 2) ** 2)
                        - 2
                    )
                )
            )
        )
        if E2 > 0 and E1 > 0 and E1 <= 1:
            opticalEnergy.append(E1)

for energy in transitionEnergy:
    if energy >= 0 and energy <= 1:
        filteredTransitionEnergy.append(energy)

print(sorted(set(opticalEnergy)))
print(len(set(opticalEnergy)))
#print(sorted(filteredTransitionEnergy))
