'''
Write a program that makes use of a function to accept a list of n integers
and displays a histogram
'''
import matplotlib.pyplot as plt

x = eval(input("Enter a list on integers :"))
plt.hist(x)
plt.title("Question 12")
plt.show()
