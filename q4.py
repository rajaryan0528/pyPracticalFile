#Write a function that takes a number(>=10) as an input and return the digits of the number as a set

def digits(n):
    s=set()
    while(n>0):
        digit=n%10
        s.add(digit)
        n=n//10

    return s
#Assumed that the repetition is not allowed in the set
x=int(input("Enter the number : "))
s=digits(x)
print("Digits of the number : ",x," as a set is :",s)
