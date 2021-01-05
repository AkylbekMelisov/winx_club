username = 'maksimka'
password = '123456'

def sign_in():
    tries = 0
    while tries < 3:
        chek_username = input()
        chek_password = input()
        if chek_username == username and chek_password == password:
            print('Вы успешно вошли!')
            break
        else:
            print('Вы ввели неверные данные!')
        tries += 1
sign_in()