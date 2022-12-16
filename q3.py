#Write a Python function to find the nth term of Fibonacci sequence and its factorial.Return the result as a list.

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


def fib(n):        #calculates the term using the recursive formula of fibonacci series
    if n == 0:
       return 0
    if n==1 or n==2:
        return 1
    return fib(n - 1) + fib(n - 2)

def nthFib(n):

    return [fib(n),fact(fib(n))]

x=int(input("Enter the position of the term to be found:"))
print(fib(x))
l=nthFib(x)
print(x,"th term of the fibonacci series is :",l[0],"\n","Factorial of the required term is :",l[1])

