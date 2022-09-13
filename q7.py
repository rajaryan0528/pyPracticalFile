'''Write a menu-driven program to perform the following on strings:
a)Find the length of string.
b)Return maximum of three strings.
c)Accept a string and replace all vowels with “#”
d)Find number of words in the given string.
e)Check whether the string is a palindrome or not'''

def menu():

    print('''
    0.Exit
    1.Find the length of string.
    2.Return maximum of three strings.
    3.Accept a string and replace all vowels with “  # ”
    4.Find number of words in the given string.
    5.Check whether the string is a palindrome or not.
    Enter your choice:
    ''')


'''The relational operators compare the Unicode values of the characters of the strings from the zeroth index till the end of the string. 
It then returns a boolean value according to the operator used.'''


'''“Geek” == “Geek” will return True as the Unicode of all the characters are equal
    In case of “Geek” and “geek” as the unicode of G is /u0047 and of g is /u0067
    “Geek” < “geek” will return True and
    “Geek” > “geek” will return False '''

def length(s):
    return len(s)

def max(s1,s2,s3):
     if s1>s2 and s1>s3:
         return s1
     elif (s2>s1 and s2>s3):
         return s2
     else:
         return s3

def replaceVowels(s):
    vowels = "aeiouAEIOU"
    l = list(s)
    for i in range(len(l)):
        if l[i] in vowels:
            l[i] = '#'
    s_p = "".join(l)
    del l
    return (s_p)

def wordCount(s):
    return len(s.split())

def isPalindrome(s):
    t=s[::-1]
    if(t==s):
        del t
        return True
    else:
        del t
        return False

i=1
def main():
    s = input("Enter a string :")
    run=True
    while(run):
      menu()
      i = int(input())
      #valid only  from python 3.10 onwards ,replacement of switch
      match i:
        case 0:
          print("Exiting :)")
          run=False

        case 1:
              print("The length of string is :", length(s))

        case 2:
           print("Resultant string :",replaceVowels(s))

        case 3:
            t=eval(input("Enter three strings as a tuple:"))
            s=max(t[0],t[1],t[2])
            print("Maximum of the entered three strings is :", s)

        case 4:
            print("Number of words in the given string is :",wordCount(s))

        case 5:
            if(isPalindrome(s)):
                print("String is Palindrome")
            else:
                print("Not a Palindrome")

        case default:
            print("Wrong input :)")

if __name__=="__main__":
    main()



