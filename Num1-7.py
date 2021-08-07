# Serie 7 Numerik

import math as m
import numpy as np
import matplotlib.pyplot as plt

def Aufgabe2():
    x = np.linspace(-1, 1, 1000)
    f = abs(x)
    a = (7+15*(x**2))/16+9/384*(35*(x**4)-30*(x**2)+3)
    b = (2/m.pi)+4/(3*m.pi)*(2*(x**2)-1)-4/(15*m.pi)*(8*(x**4)-8*(x**2)+1)
    # plt.plot(x, f) # uncomment to see original function
    # plt.plot(x, a) # uncomment to see plot of part a
    # plt.plot(x, b) # uncomment to see plot of part b
    # plt.show() # uncomment to see plot

def Aufgabe4():
    # set up plot
    plt1, plt2, plt3 = [], [], []
    plt.yscale('log')
    # calculate things
    f = lambda x : m.exp(x**2)
    fstrich = lambda x : m.exp(x**2)*2*x
    ausdruck1 = lambda x, h, f : (f(x+h)-f(x))/h
    ausdruck2 = lambda x, h, f : (f(x+h)-f(x-h))/(2*h)
    ausdruck3 = lambda x, h, f : (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)
    # print("\\begin{tabular}{|c|c|c|c|} \\hline") # Latex formatting
    # print("k & error1 & error2 & error3\\\\ \\hline") # Latex formatting
    print("k | error1 | error2 | error3")
    for k in range(19):
        h = 5**(-k)
        error1 = abs(ausdruck1(1,h,f)-fstrich(1))
        error2 = abs(ausdruck2(1,h,f)-fstrich(1))
        error3 = abs(ausdruck3(1,h,f)-fstrich(1))
        plt1.append(error1)
        plt2.append(error2)
        plt3.append(error3)
        # tableRow = f'{k} & {error1} & {error2} & {error3}\\\\ \\hline' # Latex formatting
        tableRow = f'{k} | {error1} | {error2} | {error3}'
        print(tableRow)
    # print("\\end{tabular}") # Latex formatting
    # show plot
    # plt.plot(plt1) # uncomment to see plot for first expression
    # plt.plot(plt2) # uncomment to see plot for second expression
    # plt.plot(plt3) # uncomment to see plot for third expression
    # plt.show() # uncomment to see errorplot

# Aufgabe2() # uncomment to show plot for problem 2
# Aufgabe4() # uncomment to start program for problem 4
