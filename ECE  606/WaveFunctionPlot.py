#Create plots of the three different wavefunctions in Problem 1b

import matplotlib.pyplot as plt
import numpy as np

L = 2
initialState = 0
finalState = 2

x = np.linspace(-2 * np.pi, 2 * np.pi, 200)
initialWavefunction = np.sqrt(2 / L) * np.sin(
    ((initialState + 1) * np.pi * (x + (L / 2))) / L
)
finalWavefunction = (
    x * np.sqrt(2 / L) * np.sin((finalState + 1) * np.pi * (x + (L / 2)) / L)
)
wavefunctionProduct = (
    np.sqrt(2 / L)
    * np.sin(((initialState + 1) * np.pi * (x + (L / 2))) / L)
    * x
    * np.sqrt(2 / L)
    * np.sin((finalState + 1) * np.pi * (x + (L / 2)) / L)
)

fig, (ax1, ax2, ax3) = plt.subplots(3)
ax1.plot(x, initialWavefunction)
ax1.set_title("Initial Wave Function, i=0")
ax2.plot(x, finalWavefunction)
ax2.set_title("x*Final Wave Function, f=2")
ax3.plot(x, wavefunctionProduct)
ax3.set_title("Wave Function Product, i=0, f=2")
fig.tight_layout()
plt.show()
