'''
->Consider the following strings: 
 
     str1 = “Ronald Brown” 
     str2 = “Richard Brown” 
     str3 = “Harry/* Potter% is ^a fictional !! character-&” 
 
• Write a Python function append_Strings() to create a new string, str4 by appending 
str1 and str2 without using in-built Python functions.  
• Write Python code snippet to arrange the characters of str4 so that all lowercase letters should 
come first. Also, find all the occurrences of substring “row” in str4 ignoring the case; without 
using in-built Python functions. 
• Using  an  in-built  Python  function,  write  a  statement  to  remove  all  the  special  symbols  from 
str3. 

->Consider two lists List1 and List2 as shown below.  
List1= [5,10,15,20,25,30,35] 
List2= [10,20,30,40,50,60,70] 
• Write Python code snippet to add a new element 40 after 35 in List1. The modified List1 
should be  
        List1 = [5,10,15,20,25,30,35,40] 
• Write a Python function that appends the elements of List1 into List2 and returns the 
appended list as  
       List2 = [10,20,30,40,50,60,70,5,10,15,20,25,30,35,40] 
• Write a Python function to remove all the duplicate values from the list List2. 
'''

str1 = 'Ronald Brown'
str2 = 'Richard Brown'
str3 = r'Harry/* Potter% is ^a fictional !! character-&'  # raw string



def append_Strings(s1, s2, s3):
    s4 = s1+s2+s3
    return s4


def bubbleSort(s):  # sorting the letters of string in descending order , the lowercase letters will move to the right
    for i in range(0, len(s)):
        for j in range(0, len(s)-i-1):
            if (s[j] < s[j+1]):
                s[j], s[j+1] = s[j+1], s[j]

    return " ".join(s)


def search(subStr, str):
    sample = []
    for i in range(0, len(str)-len(subStr)+1):
        # list of all substrings from the given string that are of same length
        sample.append(str[i:i+len(subStr)])
    return sample.count(subStr)


str4 = append_Strings(str1, str2, str3)
print(str4)
subStr = "row"
print(bubbleSort(list(str4)))
print(search(subStr, str4))
str3 = "".join(e for e in str3 if e.isalnum())
print(str3)

#=======================================================================================================================================

list1 = [5, 10, 15, 20, 25, 30, 35]
list2 = [10, 20, 30, 40, 50, 60, 70]
list1.append(40)


def add(l1, l2):
    l2.extend(l1)


add(list1, list2)


def remDuplicates(l):
    d = {}
    for i in l:  # frequency of each element in the list
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:  # removing duplicate values
        if d[i] > 1:
            while d[i] != 1:
                l.remove(i)
                d[i] -= 1
    return l


print(list1)
print(list2)
print(remDuplicates(list2))
