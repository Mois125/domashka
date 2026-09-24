import math

ok = True
while True:

    a = input('Введите 1-ое число: ')
    b = input('Введите 2-ое число: ')
    for cif in a:
        if cif not in '0123456789':
            ok = False
            break

    for cif in b:
        if cif not in '0123456789':
            ok = False
            break

    if ok:
        print('Числа приняты.')
        a = int(a)
        b = int(b)

    else:
        print('Вводить только числа!')
        break

    c = input('Введите действие с ними(+-*/): ')

    if c == '+':
        print(a + b)

    elif c == '-':
        print(a - b)

    elif c == '*':
        print(a * b)

    elif c == '/':
        if b != 0:
            print(a / b)
        else:
            print('Нельзя делить на ноль!')

    else:
        print('Выберите команду только из списка!(=-*/)')
        continue

    cont = input('Ещё?: ')
    if cont == 'Нет' or cont == 'нет':
        break

    else:
        continue


