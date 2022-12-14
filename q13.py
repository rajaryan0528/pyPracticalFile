'''
Write a program that makes use of a function to display sine,cosine,
polynomial and exponential curves'''

import matplotlib.pyplot as plt
import numpy as np


def plotSine(x):
   sine = np.sin(x)
   plt.plot(x,sine)
   plt.show()

def plotCoine(x):
   cosine = np.cos(x)
   plt.plot(x,cosine)
   plt.show()

def plotExpo(x):
      expo=np.exp(x)
      plt.plot(x,expo)
      plt.show()
def plotPolynomial(x):
    print(''' the polynomial will look like this 
         a.x^3 + b.x^2 +c.x^1 +d.x+0
         [[a,3],[b,2],[c,1],[d,0]]
         ''')

    # 3x^2 + x^1 + x^0   ==[[3,2],[1,1],[1,0]]     [coefficient,power]
    sample = eval(input("Enter :"))  # [[3,2],[1,1],[1,0]]
    fx = []
    y = 0
    for i in x:
        for j in range(len(sample)):
            y += sample[j][0] * (i ** sample[j][1])
        fx.append(y)
        y = 0
    plt.plot(x, fx)
    plt.show()

z = np.arange(0,4*np.pi,0.1)   # start,stop,step
x=np.arange(-10,10)

plotPolynomial(x)
plotExpo(x)
plotSine(z)
plotCoine(z)
