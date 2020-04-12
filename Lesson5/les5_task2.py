# Написать программу сложения и умножения двух шестнадцатеричных чисел. При
# этом каждое число представляется как коллекция, элементы которой — цифры
# числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
# [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque


def suma_16(num1, num2):
    num1 = deque(num1.upper())
    num2 = deque(num2.upper())
    num3 = deque()
    list_ = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
             'D', 'E', 'F']
    if num1 > num2:
        num1, num2 = num2, num1
    num1.extendleft('0' * (len(num2) - len(num1)))
    over = 0
    while len(num1) != 0:
        sum_num = (list_.index(num1.pop()) + list_.index(num2.pop()))
        num3.appendleft(list_[sum_num % 16 + over])
        over = sum_num // 16
    if over > 0:
        num3.appendleft(over)
    num3 = ''.join(num3)
    return num3


def check():
    print('Test1 is ok' if suma_16('A2', 'C4F') == 'CF1' else 'Test1 is fail')
    print('сумма A2 и C4F = ' + suma_16('A2', 'C4F'))

check()
