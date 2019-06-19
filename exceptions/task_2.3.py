def polish_notation():
    oper = (input('Введите операцию: '))
    elem = oper.split(' ')
    try:
        if int(elem[1]) >= 0 and int(elem[2]) >= 0:
            for i in elem:
                if i == '+':
                    sum = int(elem[1]) + int(elem[2])
                    print(sum)
                if i == '-':
                    diff = int(elem[1]) - int(elem[2])
                    print(diff)
                if i == '*':
                    mult = int(elem[1]) * int(elem[2])
                    print(mult)
                if i == '/':
                    div = int(elem[1]) / int(elem[2])
                    print(div)
    except ValueError:
        print('Введите числа')
    except ZeroDivisionError:
        print('Деление на ноль невозможно')
    except IndexError:
        print('Не хватает операнда')
polish_notation()

