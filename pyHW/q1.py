'''
->Write a Python function check_Eligibility(n) which accepts an argument n. It displays a 
message ‘Proceed for Printing’ and returns ‘True’ in case n is a prime number less 
than 29, otherwise it displays ‘Sorry’ and returns ‘False’. 

->Write  another  Python  function  displayPattern(n)  which  accepts  an  argument  n.  It  calls 
check_Eligibility(n).  The function  displayPattern(n)  displays  the  following 
pattern with n rows, only if the function check_Eligibility(n) returns ‘True’, otherwise 
it displays ‘Pattern Not Possible’ and exits from the function. For n=5, the pattern will 
generate 5 rows as given below.  
 
                                                   A  
                                                  B*B  
                                                 C***C  
                                                D*****D  
                                               E*******E

'''


def isPrime(n):  # checksw if a number is prime
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    else:
        return True


def check_Eligibility(n):

    if isPrime(n) == True and n < 29:
        print("Proceed for Printing")
        return True

    else:
        print("Sorry")
        return False


def displayPattern(n):

    if (check_Eligibility(n)):
        k = -1        # number of * to be printed
        c = 65  # ASCII of the first letter
        t = n
        for j in range(n):
            if j == 0:
                print(" "*t, " "+chr(c), "*"*k)
            else:
                print(" "*t, chr(c), "*"*k, chr(c))
            c += 1
            k += 2
            t -= 1
    else:
        print("Pattern Not Possible")
        return


n = int(input("Enter a number:"))
displayPattern(n)
