def SequentialSearch(list, v):
    location = -1
    for i in range(len(list)):
        if list[i] == v:
            location = i
            return location
    return location
list=[1,3,4,2,7]
print(SequentialSearch(list,8))