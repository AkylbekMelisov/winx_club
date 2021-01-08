# L = int(input())
# B = int(input())
numbers = list(map(int,input().split()))
a = numbers[0]
b = numbers[1]
count_year = 0
if 1<=a<=b<=10:
    while a <= b:
        a = a * 3
        b = b * 2
        count_year += 1
    print(count_year)
list(int(input()))
