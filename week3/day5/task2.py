str1 = input()
if len(str1) // 2 < str1.count('a'):
    print(len(str1))
else:
    i = 0
    while len(str1) // 2 >= str1.count('a'):
        if str1[i] != "a":
            str1 = str1.replace(str1[i],'',2)
        if i == len(str1)-1:
            break
        i += 1
    print(len(str1))
