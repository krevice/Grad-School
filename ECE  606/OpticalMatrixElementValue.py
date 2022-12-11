import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def integrand(x, initialState, finalState, L):
    return (
        np.sqrt(2 / L)
        * np.sin(((initialState + 1) * np.pi * (x + (L / 2))) / L)
        * x
        * np.sqrt(2 / L)
        * np.sin((finalState + 1) * np.pi * (x + (L / 2)) / L)
    )


L = 100
initialState = 0
finalState = 2

opticalMatrixElement = quad(
    integrand, -L / 2, L / 2, args=(initialState, finalState, L)
)

print(opticalMatrixElement)
