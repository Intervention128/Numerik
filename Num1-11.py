# Serie 11


import math as m
import matplotlib.pyplot as plt

# plot function
def plot(xpoints, ypoints):
    plt.bar(xpoints,ypoints)
    # plt.yscale('log') # uncomment to enable logarithmic scale
    plt.show()

def newtonGedaempft(start, f, derf, tol, kmax, lmin):
    k, l = 0, 1
    damp = [1]
    x = [start]
    while(abs(f(x[k]))>tol and k<kmax):
        s = -(f(x[k]))/(derf(x[k]))
        l = min(1,2*l)
        xnew = x[k]+s*l
        while(abs(f(xnew))>(1-.25*l)*abs(f(x[k]))):
            l = .5*l
            if l<lmin:
                break
            xnew = x[k]+s*l
        k = k+1
        damp.append(l)
        x.append(xnew)
    return x, damp

def aufgabe2(): 
    # start = 1
    start = 10
    # start = 100
    f = lambda x : m.atan(x)
    derf = lambda x : 1/(1+x**2)
    tol = 1e-9
    kmax = 100
    lmin = 1e-6
    result, damp = newtonGedaempft(start, f, derf, tol, kmax, lmin)
    approximation = result[::-1][0]
    xpoints = [i for i in range(len(result))]
    error = [abs(x) for x in result]
    # plot(xpoints, error) # plot error
    # plot(xpoints, damp) # plot damping factor

aufgabe2()