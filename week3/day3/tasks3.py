str1 = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
a = 'a'

count_a = 0
for alpha in str1:
    if alpha == a:
        count_a += 1
if count_a == len(str1):
    print(True)
else:
    print(False)