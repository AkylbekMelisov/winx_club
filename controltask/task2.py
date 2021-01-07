list1 = [1,2,3,4,5,2,6,7,78,8,2,2,2,2,2,22,2]
x = 2

def remove_x(x,list1):
    len_list = len(list1)
    i = 0
    while i < len_list:
        if x in list1:
            list1.remove(x)
        i += 1
    print(list1)
remove_x(x,list1)
