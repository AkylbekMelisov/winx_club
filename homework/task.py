# x = 9
list1 = [1,23,43,99,9,9,9]
# i = 0
# count_9 = 0
# while i < len(list1):
#     if list1[i] == x:
#         count_9 +=1
#     i += 1
# print(count_9)

i = 0
result = 0
while i < len(list1):
    result = result + list1[i]
    i += 1
print(result)