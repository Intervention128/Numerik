# Serie 2

import math as m
import numpy as np
import matplotlib.pyplot as plt
import sys
xpoints,ypoints = [], []

# set the maximum recursion limit higher lol
sys.setrecursionlimit(10**6)

# plot function
def plot(xpoints, ypoints):
    plt.plot(xpoints,ypoints)
    plt.show()

# shorthand single precision
s = lambda x : np.float32(x)

# lazy me
def printplot(x,y):
    print("%s: %.20f"%(x,abs(y-m.pi)))
    xpoints.append(x)
    ypoints.append(abs(y-m.pi))

# Aufgabe 1
aufg1 = lambda x : x**10 * 19 * (2**(-24)) / (1-19*(2**(-24)))

# Aufgabe 2a
#### (i) ####
iNormal = lambda x : m.sqrt(x**2 + 1) - x
iFix = lambda x : 1 / (m.sqrt(x**2 + 1) + x)
#### (ii) ####
iiNormal = lambda x,e : np.cos(x+e) - np.cos(x)
iiFix = lambda x,e : -2 * np.sin((2*x+e)/2) * np.sin(e/2)
#### (iii) ####
iiiNormal = lambda x : np.log(2*x) - np.log(2*x + 1)
iiiFix = lambda x : np.log((2*x)/(2*x + 1))

# Aufgabe 2b
#### double precision
def aufgabe2bDouble(n):
    result = (2 * m.sqrt(2)) if n==2 else (2**(n-1)) * m.sqrt(2 * (1-m.sqrt(1-(aufgabe2bDouble(n-1)/(2**(n-1)))**2)))
    printplot(n, result)
    return result

#### single precision
def aufgabe2Single(n):
    result = s(2*s(m.sqrt(2))) if n==2 else s(s(2**(n-1)) * s(m.sqrt(2 * s(1-s(m.sqrt(1-s((aufgabe2Single(n-1)/s(2**(n-1)))**2))))))) # if something looks stupid, but works, it's not stupid.
    printplot(n, result)
    return result

#### double precision fixed
def aufgabe2bFixDouble(n):
    # result = (2 * m.sqrt(2)) if n==2 else (2**(n-1)) * m.sqrt((2 * (aufgabe2bFix(n-1)/(2**(n-1)))**2) / (1 + m.sqrt(1 - (aufgabe2bFix(n-1)/(2**(n-1)))**2)))
    result = 2 * m.sqrt(2)
    for x in range(2,n+1):  # sadly doesnt seem to work recursively :[
        result = (2**x) * m.sqrt((2 * (result/(2**(x)))**2) / (1 + m.sqrt(1 - (result/(2**(x)))**2)))
        printplot(x, result)
    # return result

def aufgabe2bFixSingle(n):
    result = s(2 * m.sqrt(2))
    for x in range(2,n+1):
        result = s((2**x) * s(m.sqrt((2 * s(s(result)/(2**(x)))**2) / s(1 + s(m.sqrt(1 - s(s(result)/(2**(x)))**2)))))) # parentheses, anyone?
        printplot(x, result)

# result = pow(2,x)sqrt((2pow((result/(pow(2,x))),2)/(1+sqrt(1-pow((result/pow(2,x)),2)))));

# print(aufg1(m.pi)) # uncomment to get error for x = pi
# print(aufg1(m.e)) # uncomment to get error for x = e

# print(iNormal(999999)) # uncomment to see normal calculation
# print(iFix(999999)) # uncomment to see fixed calculation
# print(iiNormal(1, 1/100)) # uncomment to see normal calculation
# print(iiFix(1, 1/100)) # uncomment to see fixed calculation
# print(iiiNormal(9999999)) # uncomment to see normal calculation
# print(iiiFix(9999999)) # uncomment to see fixed calculation

# aufgabe2bDouble(30) # uncomment to print double precision
# aufgabe2Single(30) # uncomment to print single precision
# aufgabe2bFixDouble(30) # uncomment to print fixed double Precision
# aufgabe2bFixSingle(30) # uncomment to print fixed single Precision
# plot(xpoints, ypoints) # uncomment this and one of the above to get errorplot