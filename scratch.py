def isNumeric(l):
    for i in l:
        if i not in [1,2,3,4,5,6,7,8,9,0]:
            print("0")
            break
    else:
        print("1")
    

print(isNumeric([44]))
