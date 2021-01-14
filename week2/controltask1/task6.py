def bakpack(item_list:list):
    i = 0
    list2 = []
    while i < len(item_list):
        item_count = item_list.count(item_list[i])
        list2.append(item_count)
        i +=  1
    max_list = max(list2)
    result_elem = item_list[list2.index(max_list)]
    j = 0
    while j < max_list-1:
        item_list.remove(result_elem)
        j += 1
    return item_list
print(bakpack(['potato','potato','milk','milk','milk']))
