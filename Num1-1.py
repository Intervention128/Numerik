# Serie 1 

import math as m
import matplotlib.pyplot as plt

# plot function
def plot(xpoints, ypoints):
    plt.plot(xpoints,ypoints)
    plt.show()

# Aufgabe 1
def aufgabe1a(max):
    print("u:")
    for n in range(1,max):
        print(n,(0.91/n)*n-0.91)

def aufgabe1b(max):
    print("v:")
    for n in range(1,max):
        print(n,m.sqrt(n)*m.sqrt(n) - n)

# Aufgabe 2
def aufgabe2(x):
    result = 0
    for n in range(21):
        result += x**n / m.factorial(n)
    return result

def aufgabe2Fix(x):
    if(abs(x)>1):
        return aufgabe2Fix(x/abs(x))**abs(x)
    if(x < 0):
        return 1/aufgabe2(-x)
    return aufgabe2(x)

def aufgabe2Plot(x):
    xpoints, ypoints = [], []
    result = 0
    for n in range(21):
        result += x**n / m.factorial(n)
        xpoints.append(n)
        ypoints.append((abs(result-m.exp(x))/m.exp(x)))
    plot(xpoints,ypoints)

#### Aufgabe 1 ####
# aufgabe1a(17) # uncomment to get calculation for 1.(a)
# aufgabe1b(17) # uncomment to get calculation for 1.(b)

#### Aufgabe 2 ####
# for x in [-10,-1,1,10]: # uncomment to calculate exp(x)
    # print("%d: %.15e" % (x, (aufgabe2(x)-m.exp(x)/m.exp(x)))) # uncomment to see normal version
    # print("%d: %.15e" % (x, (aufgabe2Fix(x)-m.exp(x))/m.exp(x))) # uncomment to see fixed version

# aufgabe2Plot(-10) # uncomment to get error plot 
# aufgabe2Plot(-1) # uncomment to get error plot 
# aufgabe2Plot(1) # uncomment to get error plot 
# aufgabe2Plot(10) # uncomment to get error plot 
