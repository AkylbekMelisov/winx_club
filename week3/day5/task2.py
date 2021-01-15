str1 = "xaxxxxa"
if len(str1) // 2 < str1.count('a'):
    print('любимая строка Алисы')
else:
    i = 0
    while len(str1) // 2 >= str1.count('a'):
        if str1[i] != "a":
            str1 = str1.replace(str1[i],'',1)
        if i == len(str1)-1:
            break
        i += 1
    print(str1)



