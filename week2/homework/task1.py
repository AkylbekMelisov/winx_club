def register(username,password,check_password):
    list1 = []
    if len(username) > 8 and password == check_password:
        list1.append(username)
        list1.append(password)
    else:
        print('Пароли не совпадают!')
    return list1

result = register('maksim123','123456','123456')
username = result[0]
password = result[1]

def signin(username,password):
    if username == username and password == password:
        print('Вы вошли в сиситему')
    else:
        print('Не правильное имя пользователя или пароль')
signin('maksim123','123456')

product_list = ['iphone X','iphone Y','samsung galaxy 2','nokia 3','nokia 999',
                'nike boots','adidas boots','dior shirt','raben shirt',
                'adidas shirt', 'channel coat', 'wedding dress','gucci cloak',
                'adidas cloak']

def write_to(filename,product):
    file1 = open(filename,'a')
    file1.write(product + '\n')

for line in product_list:
    write_to('catalogue.txt',line)

file2 = open('catalogue.txt')
product_file = file2.readlines()

def sort():
    for product in product_list:
        if 'iphone' in product or 'samsung' in product or 'nokia' in product:
            write_to('phones.txt',product)
        elif 'boots' in product:
            write_to('boots.txt',product)
        elif 'shirt' and 'coat' and 'dress' in product:
            write_to('clothes.txt',product)
sort()

user_input = input()
if user_input == 'boots':
    file1 = open('boots.txt')
    print(file1.read())
elif user_input == 'phones':
    file1 = open('phones.txt')
    print(file1.read())
elif user_input == 'clothes':
    file1 = open('clothes.txt')
    print(file1.read())
