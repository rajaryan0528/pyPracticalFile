'''
Write a program that makes use of a function to display sine,cosine,
polynomial and exponential curves'''

import matplotlib.pyplot as plt
import numpy as np

z = np.arange(0,4*np.pi,0.1)   # start,stop,step
x=np.arange(-10,10)
expo=np.exp(x)
print(''' the polynomial will look like this 
     a.x^3 + b.x^2 +c.x^1 +d.x+0
     [[a,3],[b,2],[c,1],[d,0]]
     ''')

# 3x^2 + x^1 + x^0   ==[[3,2],[1,1],[1,0]]     [coefficient,power]
sample=[[3,2],[1,1],[1,0]]
fx=[]
for i in range(len(x)):
   fx.append(sample[0][0]*x[i]**sample[0][1]+sample[1][0]*x[i]**sample[1][1]+sample[2][0]*x[i]**sample[2][1])
#polynomial=eval(input("Enter :"))


sine = np.sin(z)
cosine = np.cos(z)
plt.plot(z,sine,z,cosine)
plt.show()
plt.plot(x,fx)
plt.show()
plt.plot(x,expo)
plt.show()
