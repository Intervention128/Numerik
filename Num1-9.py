# Serie 9


import matplotlib.pyplot as plt
import numpy as np

tol = 2.220446049250313e-10
hmin = 2.220446049250313e-3

class adaptiveSimpson: # basically a readable version of the code from the lecture
    def __init__(self, i, f):
        self.a, self.b = i
        self.delta = [i]
        self.f = f
        self.integralValue = 0
        self.points = []
    
    def simpson(self, interval):
        (a,b) = interval
        return (b-a)*(self.f(a)+4*self.f((a+b)/2)+self.f(b))/6

    def error(self, interval):
        a,b = interval
        m = (a+b)/2
        simp0 = self.simpson(interval)
        simp1 = self.simpson((a,m))
        simp2 = self.simpson((m,b))
        return abs(simp0-simp1-simp2), simp1+simp2

    def solve(self):
        while len(self.delta) > 0:
            deltaOld, self.delta = self.delta, []
            for J in deltaOld:
                (aJ,bJ) = J
                (err, compositeSimpson) = self.error(J)
                if err > 10*(bJ-aJ)*tol/(self.b-self.a) and (bJ-aJ) > hmin:
                    m = (aJ+bJ)/2
                    J1 = (aJ,m)
                    J2 = (m,bJ)
                    self.delta.append(J1)
                    self.delta.append(J2)
                else:
                    self.integralValue += compositeSimpson
                    self.points.append(aJ)
                    self.points.append((aJ+bJ)/2)
                    self.points.append(bJ)

    def plot(self):
        print(self.integralValue)
        xvalues = np.arange(self.a, self.b, 1e-6)
        yvalues = self.f(xvalues)
        plt.plot(xvalues, yvalues)
        for point in self.points:
            plt.axvline(x=point)
        plt.show()

def Aufgabe1():
    f = lambda x : np.exp(-10*(x-1)**2)
    fInterval = (-1,1)
    g = lambda x : x**(1/2)
    gInterval = (0,1)
    # simpf = adaptiveSimpson(fInterval, f)
    # simpf.solve()
    # simpf.plot()
    simpg = adaptiveSimpson(gInterval, g)
    simpg.solve()
    simpg.plot()


Aufgabe1()