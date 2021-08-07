# Serie 3

import math as m
import numpy as np
import matplotlib.pyplot as plt
xpoints, ypoints = [], []

# Aufgabe 3
def aufgabe3():
    x = np.linspace(0.5, 8, 1000)
    f = (2*x)**(1/2)
    interpol_newton = 1 + (x-0.5)*( 2/3 + (x-2)*( -1/15 + (x-4.5)*(2/(35*15))))
    interpol_lagrange = ((x-2) * (x-4.5) * (x-8) / -45) + 2*((x-.5) * (x-4.5) * (x-8) / 22.5) + 3*((x-.5) * (x-2) * (x-8) / -35) + 4*((x-.5) * (x-4.5) * (x-2) / 157.5)
    interpol_bary = (-45/(x-0.5)+45/(x-2)-105/(x-4.5) +630/(x-8))/(-45/(x-0.5)+22.5/(x-2) -35/(x-4.5) +157.5/(x-8))
    # plt.plot(x, interpol_newton, "b") # uncomment these to see respective plots
    # plt.plot(x, interpol_lagrange, "y") # uncomment these to see respective plots
    # plt.plot(x, interpol_bary, "g") # uncomment these to see respective plots
    # plt.plot(x, f, "r") # uncomment these to see respective plots
    plt.show()

# aufgabe3() # uncomment to do anything lol
