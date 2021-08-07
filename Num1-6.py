# Serie 6

import matplotlib.pyplot as plt

class TriDiagMatrix:
    def __init__(self, bot, main, top):
        self.bot = bot
        self.main = main
        self.top = top
        self.n = len(main)
    
    def solve(self, y):
        yTilde, bTilde, x = [], [], []
        yTilde.append(y[0])
        bTilde.append(self.main[0])
        for i in range(1, self.n):
            bTilde.append(self.main[i]-self.top[i-1]*self.bot[i-1]/bTilde[i-1])
            yTilde.append(y[i]-yTilde[i-1]*self.bot[i-1]/bTilde[i-1])
        # print("yTilde="+str(yTilde)) # DEBUG
        # print("yTildeLength="+str(len(yTilde))) # DEBUG
        # print("bTilde="+str(bTilde)) # DEBUG
        # print("bTildeLength="+str(len(bTilde))) # DEBUG
        x.append(yTilde[self.n-1]/bTilde[self.n-1])
        for i in range(self.n-1):
            x.append((yTilde[self.n-3-i]-self.top[self.n-3-i]*x[i-1])/bTilde[self.n-3-i])
        # print("x="+str(x[::-1])) # DEBUG
        return x[::-1]

class SplineCalc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)-1
        self.h, self.p, self.q, self.g, self.a, self.b, self.c = [], [], [], [], [], [], []
        self.spline, self.derSpline, self.derderSpline = lambda : None, lambda : None, lambda : None
        self.xpoints, self.ypoints, self.derypoints, self.derderypoints = [], [], [], []
        for i in range(self.n):
            self.h.append(self.x[i+1]-self.x[i])
        # print("h="+str(self.h)) # DEBUG
        # print("n="+str(self.n)) # DEBUG
        # print("x="+str(self.x)) # DEBUG
        # print("y="+str(self.y)) # DEBUG
        
    def getSpline(self):
        self.step1()
        self.step2()
        self.step3()
        # print("a="+str(self.a)) # DEBUG
        # print("b="+str(self.b)) # DEBUG
        # print("c="+str(self.c)) # DEBUG
        self.step4()
        self.plotSpline()
    
    def step1(self):
        for i in range(self.n-1):
            self.p.append(self.h[i]/(self.h[i]+self.h[i+1]))
            self.q.append(1-self.p[i])
        # print("p="+str(self.p)) # DEBUG
        # print("pLength="+str(len(self.p))) # DEBUG
        # print("q="+str(self.q)) # DEBUG
        # print("qLength="+str(len(self.q))) # DEBUG
        self.p.pop(0)
        self.q.pop(self.n-2)
        for i in range(1,self.n):
            self.g.append((6/(self.h[i-1]+self.h[i]))*((self.y[i+1]-self.y[i])/self.h[i]-(self.y[i]-self.y[i-1])/self.h[i-1]))
        # print("g="+str(self.g)) # DEBUG
        # print("gLength="+str(len(self.g))) # DEBUG

    def step2(self):
        matrix = TriDiagMatrix(self.p, [2]*(self.n-1), self.q)
        self.a = [0]+matrix.solve(self.g)+[0]
    
    def step3(self):
        # print("aLength="+str(len(self.a))) # DEBUG
        for i in range(self.n):
            self.c.append(self.y[i]-self.a[i]*(self.h[i]**2)/6)
            self.b.append(((self.y[i+1]-self.y[i])/self.h[i])-(self.h[i]/6)*(self.a[i+1]-self.a[i]))
    
    def step4(self): # sadlly doesn't work :(
        self.spline = lambda x, i : self.a[i]*(((self.x[i+1]-x)**3)/(6*self.h[i])) + self.a[i+1]*(((x-self.x[i])**3)/(6*self.h[i])) + self.b[i]*(x-self.x[i]) + self.c[i]
        self.derSpline = lambda x, i : -self.a[i]*(((self.x[i+1]-x)**2)/(2*self.h[i])) + self.a[i+1]*(((x-self.x[i])**2)/(2*self.h[i])) + self.b[i]
        self.derderSpline = lambda x, i : self.a[i]*(((self.x[i+1]-x))/(self.h[i])) + self.a[i+1]*(((x-self.x[i]))/(self.h[i]))
    
    def plotSpline(self):
        for i in range(1001):
            self.xpoints.append(self.x[0]+i*((self.x[self.n]-self.x[0])/1000))
        for x in self.xpoints:
            index = self.binSearch(x)
            self.ypoints.append(self.spline(x, index))
            self.derypoints.append(self.derSpline(x, index))
            self.derderypoints.append(self.derderSpline(x, index))
    
    def showSpline(self):
        plt.plot(self.xpoints, self.ypoints)
    
    def showDerSpline(self):
        plt.plot(self.xpoints, self.derypoints)
    
    def showDerDerSpline(self):
        plt.plot(self.xpoints, self.derderypoints)

    def binSearch(self, x):
        min, max = 0, self.n
        # print(x) # DEBUG
        while(max-min != 1):
            j = int((min+max)/2)
            if(x>=self.x[j]):
                min = j
            else:
                max = j
        # print(self.x[min], self.x[min+1], min) # DEBUG
        return min
    
    def plotError(self, function):
        zpoints = []
        funcpoints = []
        for i in range(1001):
            zpoints.append(abs(function(self.xpoints[i])-self.ypoints[i]))
            funcpoints.append(function(self.xpoints[i]))
        plt.plot(self.xpoints, zpoints)
        # plt.plot(self.xpoints, funcpoints) # uncomment to see function plot
        
        
            
# test functions
def test1(): # from Problem 1b
    xVal = [0, 1, 2]
    yVal = [0, 2, 3]
    spline = SplineCalc(xVal, yVal)
    spline.getSpline()
    # spline.showSpline() # uncomment to see spline
    # spline.showDerSpline() # uncomment to see first derivative
    # spline.showDerDerSpline() # uncomment to see second derivative
    plt.show()

def test2(): # runge function
    runge = lambda x : 1 / (1+25*(x**2))
    xVal, yVal = [], []
    for i in range(21):
        xVal.append(-1+i*(1/10))
        yVal.append(runge(xVal[i]))
    spline = SplineCalc(xVal, yVal)
    spline.getSpline()
    # spline.showSpline() # uncomment to see spline
    spline.plotError(runge) # uncomment to see errorplot
    # spline.showDerSpline() # uncomment to see first derivative
    # spline.showDerDerSpline() # uncomment to see second derivative
    plt.show()

def test3(): # Hammock PK 24
    xVal = [-7, -5, -3, -1, 0, 1, 2, 2.5, 3, 3.3]
    yVal = [2.1, 1.8, 1.2, 0.4, 0, 0.6, 1.6, 2.5, 3.5, 4.7]
    spline = SplineCalc(xVal, yVal)
    spline.getSpline()
    spline.showSpline() # uncomment to see Hammock PK 24 Designer Lie
    # spline.showDerSpline()  # uncomment to see first derivative of Hammock PK 24 Designer Lie
    # spline.showDerDerSpline()  # uncomment to see second derivative of Hammock PK 24 Designer Lie
    plt.show()

# test1() # uncomment to see things
# test2() # uncomment to see things
# test3() # uncomment to see things