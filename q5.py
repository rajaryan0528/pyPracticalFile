#Write a function that finds the sum of the n terms of the following series.Import
#the factorial function created in question4.
# 1–x2/2!+x4/4!–x6/6!+...xn/n!

from q3 import fact
from math import *

def seriesSum(n,x):
   sum=1
   for i in range(2,n+1,2):
     if i%2==0:
        sum-=pow(x,i)/fact(i)
     else:
         sum+=pow(x,i)/fact(i)
   return sum;

n=int (input("Enter the number of terms in the series :"))
x=int (input("Enter a positive integer:"))
print("Sum of the series is :",seriesSum(n,x))