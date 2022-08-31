#Write a function that takes the lengths of three sides:side1,side2 and side3
#of the triangle as the input from the user using input function and return the area and perimeter of the triangle
#as a tuple.Also,assert that sum of the length of any two sides is greater than the third side.
from math import *
def area(a,b,c):
    s=(a+b+c)/2
    area=sqrt(s*(s-a)*(s-b)*(s-c))
    return area,s*2

a=int(input("Enter the length of the side 1 :"))
b=int(input("Enter the length of the side 2 :"))
c=int(input("Enter the length of the side 3 :"))

t=area(a,b,c)
print("Area of the triangle is :",t[0],"\n","Perimeter of the triangle is :",t[1])