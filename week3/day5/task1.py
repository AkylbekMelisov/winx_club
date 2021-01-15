# list2 = []
# n = int(input())
# for i in range(n):
#     name = input()
#     list2.append(name)
# list2.sort()
# print(list2)

stones = ['purple','green','blue','orange','red','yellow']
list1 = []
n = int(input())
for i in range(n):
    my_stone = input()
    list1.append(my_stone)

print(len(stones) - n)
for stone in stones:
    if stone not in list1:
        print(stone)
