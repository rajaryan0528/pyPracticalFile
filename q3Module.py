'''
When you import a module in Python, all the code in it will be run, and all the variables in that module will be stuck on that module object.
Hence this file which contains only functions
'''


def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


def fib(n):        #calculates the term using the recursive formula of fibonacci series
  if n <= 1:
     return n
  return fib(n - 1) + fib(n - 2)

def nthFib(n):

    return [fib(n),fact(fib(n))]
