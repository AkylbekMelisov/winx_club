def phone_number(number):
    if len(number) == 13 and number.startswith('+996'):
        print(number)
    elif len(number) == 10 and number.startswith('0'):
        number = number.replace("0","+996")
        print(number)
    elif len(number) == 9:
        number = '+996' + number
        print(number)
    elif len(number) == 12 and number.startswith('996'):
        number = '+' + number
        print(number)
    else:
        print('не верный номер')
phone_number('996555666555')