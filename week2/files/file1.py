file1 = open('cars.txt', 'r')
list1 = file1.readlines()
list1.append('maksimka')
list1.pop(3)
print(list1)
list1 = ['dsf','sdf',]