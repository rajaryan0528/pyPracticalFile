'''
Write a menu-driven program to accept a list of student names and perform
the following:
a.search an element using linear search and binary search.
b.Sort the elements using bubble sort,insertion sort,selection sort
'''


def linearSearch(l, key):
  for i in range(len(l)):
    if (l[i] == key):
        return i+1
  else:
    return -1


def binarySearch(l, key):
    low = 0
    high = len(l)-1
    while (low <= high):
        mid = (low+high)//2
        if (l[mid] == key):
           return mid+1
        elif (l[mid] < key):
            low = mid+1
        else:
           high = mid-1
    else:
        return -1


def bubbleSort(l):
    for i in range(0, len(l)):
        for j in range(0, len(l)-i-1):
            if (l[j] > l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]

    return l


def selectionSort(l):

    for i in range(len(l)):
        min_index = i

        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l


def insertionSort(l):


    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while(j>=0 and key < l[j]):
            l[j+1]=l[j]
            j-=1
        l[j+1] = key

    return l

def selectionSort(l):
    
    for i in range(len(l)):
        min_index = i
 
        for j in range(i+ 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i],l[min_index] =l[min_index],l[i]
    return l

def menu(): 
    print("0.Exit")
    print("1.Selection Sort")
    print("2.Insertion Sort")
    print("3.Bubble Sort")
    print("4.Linear Search")
    print("5.Binary Search")
    print("-1 - Element not present")


while (True):
    menu()
    i = int(input("Your choice : "))
    if i !=0:
     names = eval(input("Enter the student names :"))
    #valid only  from python 3.10 onwards ,replacement of switch
    match i:
        case 0:
          print("Exiting :)")
          break
        case 1:
            print("The sorted array is :",selectionSort(names))

        case 2:
            print("The sorted array is :", insertionSort(names))

        case 3:
            print("The sorted array is :", bubbleSort(names))

        case 4:
            key = input("Enter the name to be searched for :")
            print("Found at : ",linearSearch(names, key))
        case 5:
            key = input("Enter the name to be searched for :")
            print("Found at : ",binarySearch(names, key))
        case default:
            print("Wrong input :)")
