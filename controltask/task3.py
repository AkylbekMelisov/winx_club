list1 = [1,2,3,4,5,2,6,7,78,8,2,2,2,2,2,22,2]
x = 33

def tru_false(x):
    if x in list1:
        return ('tru')
    else:
        return ('false')
print(tru_false(x))