def game_for_child():
    i = 0
    import random
    random_number = random.randint(0, 9)
    while i < 5:
        number = int(input())
        print(random_number)
        if number == random_number:
            print('Вы победили')
            break
        elif number < random_number:
            print('>')
        elif number > random_number:
            print('<')
        else:
            print('Вы проиграли!')
        i += 1
    if i == 5:
        print('loose')
game_for_child()
