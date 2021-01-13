list1 = [1,2,2,2,3,3,3,3,4,4,4]
list2 = []

for i in list1:
    list2.append(list1.count(i))
max_count = max(list2)
max_index = list2.index(max_count)
result = list1[max_index]
print(result,max_count)