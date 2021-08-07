# Serie 8

import math as m
import numpy as np

class Quadrature:
    def __init__(self, n, i, f):
        self.n = n
        (self.a, self.b) = i # the interval
        self.h = (self.b-self.a)/self.n # step
        self.f = f # the function (as a lambda)
        self.x = [self.a + i*self.h for i in range(n+1)]

    def trapezRegel(self):
        result = 0.0
        for i in range(self.n):
            result += (self.h/2)*(self.f(self.x[i])+self.f(self.x[i+1]))
        return result
    
    def simpsonRegel(self):
        result = 0.0
        for i in range(0, self.n-1, 2):
            result += (self.h/3)*(self.f(self.x[i])+self.f(self.x[i+2]))+(self.h*4/3)*(self.f(self.x[i+1]))
        return result

class Romberg():
    def __init__(self, i, f):
        (self.a, self.b) = i
        self.f = f
        self.T = [[0] * 12 for i in range(12)]
        # self.T = [[0] * 1000 for i in range(1000)] # use this initialisation for the patience test
    
    def solve(self):
        self.T[1][1] = (self.b-self.a)/2*(self.f(self.a)+self.f(self.b))
        i = 2
        # while abs(self.T[i-2][i-2]-self.T[i-1][i-1]) > np.finfo(float).eps: # test your patience! who will last longer, you or the computer?
        while (i < 11):
            h = (self.b-self.a)*(2**(1-i))
            summe = 0.0
            for k in range(1,2**(i-2)+1):
                summe += self.f(self.a+((2*k)-1)*h)
            self.T[1][i] = (1/2)*self.T[1][i-1]+h*summe
            for j in range(1, i):
                self.T[j+1][i] = self.T[j][i] + (self.T[j][i]-self.T[j][i-1])/((4**j)-1)
            # print(f'hello, i\'m still working! ({i})') # good for the patience test.
            i += 1
        return self.T[i-1][i-1]
    
    def printTable(self):
        self.T.pop(0)
        self.T.pop(10)
        for xs in self.T:
            xs.pop(0)
            xs.pop(10)
            # print(xs) # uncomment to see finished array
        return [self.T[i][i] for i in range(10)]

def Aufgabe1a():
    f = lambda x : m.sqrt(x)
    i = (0,1)
    # i = (1,4)
    print("k | Trapezregel | Simpsonregel")
    # print("\\begin{tabular}{|c|c|c|}\\hline") # Latex formatting
    # print("k & Trapezregel & Simpsonregel\\\\ \\hline") # Latex formatting
    for k in range(1, 11):
        quadr = Quadrature((2**k+1), i, f)
        trapez = quadr.trapezRegel() # calculated values
        simpson = quadr.simpsonRegel() # calculated values
        # trapez = abs(quadr.trapezRegel()-(2/3)) # absolute error for i = (0,1)
        # simpson = abs(quadr.simpsonRegel()-(2/3)) # absolute error for i = (0,1)
        # trapez = abs((quadr.trapezRegel()-(2/3))/(2/3)) # relative error for i = (0,1)
        # simpson = abs((quadr.simpsonRegel()-(2/3))/(2/3)) # relative error for i = (0,1)
        # trapez = abs(quadr.trapezRegel()-(14/3)) # absolute error for i = (1,4)
        # simpson = abs(quadr.simpsonRegel()-(14/3)) # absolute error for i = (1,4)
        # trapez = abs((quadr.trapezRegel()-(14/3))/(14/3)) # relative error for i = (1,4)
        # simpson = abs((quadr.simpsonRegel()-(14/3))/(14/3)) # relative error for i = (1,4)
        # row = f'{k} & {trapez} & {simpson} \\\\ \\hline' # Latex formatting
        row = f'{k} | {trapez} | {simpson}'
        print(row)
    # print("\\end{tabular}") # Latex formatting

### NOTICE: reference values are from integral-calculator.com ###

def Aufgabe1b():
    f = lambda x : m.exp(-(x**2)/2)
    i = (0,1)
    quadr = Quadrature(2, i, f)
    value = 0.8556243918921488
    iterator = 1
    while(abs(quadr.trapezRegel()-value)>10**(-3)):
        quadr = Quadrature(2+iterator, i, f)
        iterator += 1
    print(iterator)

def Aufgabe4():
    f1 = lambda x : x**(1/4)
    f2 = lambda x : 1/((x-1.1)*(x+0.1))
    f3 = lambda x : m.exp(-m.pi*x)*m.cos(m.pi*x)
    i = (0,1)
    romberg1 = Romberg(i, f1)
    romberg2 = Romberg(i, f2)
    romberg3 = Romberg(i, f3)
    romberg1.solve()
    romberg2.solve()
    romberg3.solve()
    sol1 = romberg1.printTable()
    sol2 = romberg2.printTable()
    sol3 = romberg3.printTable()
    err1 = [abs(x-0.8) for x in sol1]
    err2 = [abs(x+(5*np.log(11)/3)) for x in sol2]
    err3 = [abs(x-(1/(2*m.pi)*(m.exp(-m.pi)+1))) for x in sol3]
    # print("\\begin{tabular}{|c|c|c|c|}\\hline") # Latex formatting
    # print("k & $f_1$ & $f_2$ & $f_3$\\\\ \\hline") # Latex formatting
    print("k | f1 | f2 | f3")
    for k in range(10):
        # row = f'{k+1} & {err1[k]} & {err2[k]} & {err3[k]}\\\\ \\hline' # Latex formatting
        row = f'{k+1} | {err1[k]} | {err2[k]} | {err3[k]}'
        print(row)
    # print("\\end{tabular}") # Latex formatting

# Aufgabe1a() # uncomment to get results of problem 1a
# Aufgabe1b() # uncomment to get results of problem 1b
# Aufgabe4() # uncomment to get results of problem 4