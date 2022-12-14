def linearSearch(l, ele):
    for i in range(len(l)):
        if (l[i] == ele):
            return i+1
    else:
        return -1


def search(l, ele):
    pos=linearSearch(l, ele)
    return pos
  
l=[1,2,3,4]
print(search(l,2))