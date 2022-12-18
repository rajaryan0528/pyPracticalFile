'''
Write a Python program that accepts a list Number_List as input. Ensure that user enters numeric values as input in the list. Take an input Num from the user to be searched in Number_List.  
 
• Define  a  Python  function  SortAndSearch()  with  two  arguments  as  Number_List  and Num. Use linear search in SortAndSearch() to search given number Num in Number_List.  Also,  SortAndSearch()  displays  the  position  of  Num  if  it  is  found  in Number_List  otherwise  displays  the message  ‘Number is not found in the list’.  
 
• Use  insertion  sort  in  SortAndSearch()  to  arrange  the  elements  of  Number_List  in ascending  order.  SortAndSearch()should  return  the  sorted  list  along with  the  number  of comparisons  required  for  sorting.    What  changes  are  required  to  arrange  the  elements  of Number_List in descending order?  
 
• Consider Number_List = [2   15   5   4   12] and Num = 4. Show the changes in Number_List after each iteration in SortAndSearch().
'''


def linearSearch(l, ele):
    found = False
    pos = -1
    for i in l:
        if (i == ele):
            found = True
            pos =l.index(i)+1
            break
    return (found, pos)


def SortAndSearch(Number_List, Num):
    data = linearSearch(Number_List, Num)
    if (data[0] == True):
        print("Found at :", data[1])
    else:
        print('Number is not found in the list.')

    for i in range(1, len(Number_List)):
        key = Number_List[i]
        j = i-1
        while (j >= 0 and key < Number_List[j]):  # ascending order
            Number_List[j+1] = Number_List[j]
            j -= 1
            print(Number_List)
        Number_List[j+1] = key

    return Number_List


'''
To  arrange  the  elements  of Number_List in descending order,key < Number_List[j] the < need to be replaced with >.
'''

Number_List = []
n = int(input("Enter number of elements : "))
l = n
try:
    while n > 0:
        ele = int(input())
        Number_List.append(ele)
        n -= 1
except ValueError:
    print("Enter numeric values only.Non-numeric values will be discarded")
    l = l-1  # number of elements in the list will one less than n

Num = int(input("Enter the number to search for:"))
print(SortAndSearch(Number_List, Num))
print(" Maximum Number of Comparisons :", (l*(l-1))/2)  # worst case
