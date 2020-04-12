# Задача 1
#
# Написать программу, которая будет складывать, вычитать, умножать или
# делить два числа. Числа и знак операции вводятся пользователем. После
# выполнения вычисления программа не завершается, а запрашивает новые
# данные для вычислений. Завершение программы должно выполняться при вводе
# символа '0' в качестве знака операции. Если пользователь вводит
# неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об
# ошибке и снова запрашивать знак операции. Также она должна сообщать
# пользователю о невозможности деления на ноль, если он ввел его в
# качестве делителя.
#
# https://drive.google.com/file/d/1jRwDeMwz3PMiGdoOO2FsqcNx-sZftJzG/view?usp=sharing


def calc():
    print('Введите операнды и оператор')
    a = int(input('Введите первый операнд: '))
    b = int(input('Введитe второй операнд: '))
    oper = int(input('''Введитe оператор,
     1 для +
     2 для -
     3 для *
     4 для /
     для выхода введите 0: '''))
    if oper == 0:
        return 'конец программы'
    elif oper == 1:
        print(a + b)
        return calc()
    elif oper == 2:
        print(a - b)
        return calc()
    elif oper == 3:
        print(a * b)
        return calc()
    elif oper == 4 and b == 0:
        print('На ноль делить нельзя')
        return calc()
    elif oper == 4:
        print(a / b)
        return calc()
    else:
        print('Ошибочный оператор')
        return calc()

print(calc())
