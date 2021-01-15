string1 = "xiaodao"
unique = []
for letter in string1:
    if letter not in unique:
        unique.append(letter)
if len(unique) % 2 == 0:
    print('CHAT WITH HER')
else:
    print('IGNORE HIM!')