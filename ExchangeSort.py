def exchange(list):
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list
list = [7,2,4,6,5,3,1,8,9,10]
print('Before: ', list)
print('After: ', exchange(list))