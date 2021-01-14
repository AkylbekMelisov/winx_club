str1 = "Hellsadsadoy world fdssd asdfdsaf ewew dsaf"

if str1[0].isupper() and len(str1) < 10:
    str1 = str1.lower()
    print(str1)
elif str1[0].islower() and len(str1) < 10:
    str1 = str1.upper()
    print(str1)
elif len(str1) > 10:
    str1 = str1.capitalize()
    print(str1)
