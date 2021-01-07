list1 = [2,4,5,7,9,8,6,2,3,4,1,5,1,1,1,1]
list2 = []
i = 0
while i < len(list1):
    if list1[i] not in list2:
        list2.append(list1[i])
    i += 1
print(list2)
