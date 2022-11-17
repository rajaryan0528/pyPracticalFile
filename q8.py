'''
Write a Python program to perform the following using list:
a)Check if all elements in list are numbers or not.
b)If it is a numeric list,then count number of odd values in it.
c)If list contains all Strings,then display the largest String in the list.
d)Display list in reverse form.
e)Find a specified element in list.
f)Remove the specified element from the list.
g)Sort the list in descending order.
h)accept 2 lists and find the common members in them.
'''


def linearSearch(l, ele):
    for i in l:
        if (i == ele):
            return i
    else:
        return -1
 
def isNumeric(l):
    isNumeric=False
    for i in l:
        if str(i).isdigit() ==False:
            break
    else:
        isNumeric=True
    return isNumeric 


def isString(l):
    isString = True
    for i in l:
        if str(i).isdigit() == True:
            isString=False
            break
    return isString

def oddValuesCount(l):
    count=0
    for i in l:
        if i % 2 != 0:
            count += 1
    return count


def largestString(l):
    return max(l)


def reverseList(l):
    l.reverse()
    return l


def search(l, ele):
    return linearSearch(l, ele)


def removeEle(l, ele):
    l.remove(ele)    # no return value
    return l


def sort(l):
    l.sort(reverse=True)


def commonElements(l, m):
    return [i for i in l if i in m]


def menu():

   print(
    ''' \t0.Exit
        1.Check if all elements in list are numbers or not .
        2.If it is a numeric list, then count number of odd values in it.
        3.If list contains all Strings, then display the largest String in the list.
        4.Display list in reverse form.
        5.Find a specified element in list.
        6.Remove the specified element from the list.
        7.Sort the list in descending order.
        8.accept 2 lists and find the common members in them.''')
   print("-----------------------------------------------------------------")

run = True
while (run):
    menu()
    i = int(input("Enter your choice :"))
    l = eval(input("Enter a list :"))
    match i:
        case 1:
            print(isNumeric(l))

        case 2:
            if (isNumeric(l)):
                print("List is all numeric.")
                print(oddValuesCount(l))
            else:
                print("Please enter a numeric list.")

        case 3:
            if isString(l):
                print(largestString(l))
            else:
                print("Please enter a list of strings.")

        case 4:
            print(reverseList(l))

        case 5:
            ele = print("Enter the element :")
            print(search(l, ele))

        case 6:
            ele = print("Enter the element :")
            print(removeEle(l, ele))

        case 7:
            print(reverseList(l))

        case 8:
            m = eval(input("Enter the second list :"))
            print(commonElements(l, m))

        case default:
            if (i == 0):
                print("Exiting :)")
                run = False
            else:
                print("Wrong Input :(")
