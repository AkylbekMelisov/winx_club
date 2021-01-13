# w = int(input())
#
# if 1 <= w <= 100:
#     if w % 2 == 0:
#         print('YES')
#     else:
#         print("NO")

str1 = input()

if len(str1) > 10:
    len_str = len(str1) - 2
    print(str1[0] + str(len_str) + str1[-1])
else:
    print(str1)

