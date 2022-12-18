'''
-->Consider dictionary Dict1 that represents vehicle models and its number available in a company. 
For example, Dict1 is defined as follows:   
Dict1 = {‘BMW’ :5, ‘Mercedes’: 10, ‘Volkswagen’: 10,‘Jaguar’:4, ‘Landrover’:15} 
 
• Write a Python function Model() that accepts Dict1 along with a vehicle model. It returns 
the number of vehicles available for that model. If the model does not exist in Dict1, then it should return a value of -1.      
 
• Write a Python function Change() to accept Dict1 along with a vehicle model ‘VM’.The function should return the updated dictionary Dict1 as follows: 
 
Case 1: if  VM exists in the dictionary and the number of models corresponding to VM  is less than 5, then VM should be removed from the dictionary.  
Case2: if  VM exists in the dictionary and the number of models corresponding to VM is greater than 5, then decrease the number of models by 2.

-->Consider the following tuples: 
Tuple1 = (11,22,33) 
Tuple2 = (99,88,77) 
 
• Write a Python function to swap the values of Tuple1 and Tuple2. The expected output is 
as follows: 
Tuple1 = (99,88,77) 
Tuple2 = (11,22,33) 
 
• Write a Python function Div3and5() that takes a 10-element numeric tuple and returns the 
following:  
 
o sum of elements which are divisible by 3.  
o sum of elements which are divisible by 5. 
o sum of elements which are divisible by 3 and 5.  
 
->Consider the following sets and give Python code snippets for each of the following:  
set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70} 
 
• Display common elements in set1 and set2.  
• Display a new set of elements such that the elements are present in either set1 or set2 but not in both the sets
'''

Dict1 = {}
model = ""
modelCount = 0
n = int(input("Enter the number of models available:"))
for i in range(n):
    model = input("Enter the name of tbhe model: ")
    modelCount = int(input("Enter model Count: "))
    Dict1[model] = modelCount

#Dict1 = {'BMW': 5, 'Mercedes': 10,'Volkswagen': 10, 'Jaguar': 4, 'Landrover': 15}


def Model(Dict1, model):
    if model not in Dict1:
        return -1
    else:
        return Dict1[model]


def change(Dict1, vm):
    if vm in Dict1 and Dict1[vm] < 5:
        del Dict1[vm]
    else:
        Dict1[vm] -= 2


print(Model(Dict1, 'BM'))
change(Dict1, "Volkswagen")
print(Dict1)
print(Model(Dict1, "Volkswagen"))

# ============================================================================================================================
Tuple1 = (11, 22, 33)
Tuple2 = (99, 88, 77)


def Swap(t1, t2):  # swaps the value
    t1, t2 = t2, t1
    return (t1, t2)


Tuple1, Tuple2 = Swap(Tuple1, Tuple2)
print(Tuple1, Tuple2)


def divBy3(n):  # checks divisibility by 3
    if n % 3 == 0:
        return True
    else:
        return False


def divBy5(n):                 # checks divisibility by 5
    if n % 5 == 0:
        return True
    else:
        return False


def divBy3and5(n):           # checks divisibility by 3 and 5
    if n % 3 == 0 and n % 5 == 0:
        return True
    else:
        return False


t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def Div3and5(t):
    sum_Div3 = 0
    sum_Div5 = 0
    sum_Div3and5 = 0

    for i in t:
        if (divBy5(i)):
            sum_Div5 += i
        if (divBy3(i)):
            sum_Div3 += i
        if (divBy3and5(i)):
            sum_Div3and5 += i
    return (sum_Div3, sum_Div5, sum_Div3and5)


print("sum of elements which are divisible by 3: ", Div3and5(t)[0])
print("sum of elements which are divisible by 5: ", Div3and5(t)[1])
print("sum of elements which are divisible by 3 and 5: ", Div3and5(t)[2])

# =======================================================================================================================================

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1 & set2)  # intersection
set3 = set1 ^ set2  # symmetric difference
print(set3)


'''
# union: A | B  
# intersection:A & B  
# difference: A - B)  
# symmetric difference:A ^ B)
'''
