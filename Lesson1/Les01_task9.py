# Задача9
# Вводятся три разных числа. Найти, какое из них является средним (больше
# одного, но меньше другого).
# # https://drive.google.com/file/d/1iYbrYgvC8WgpNAFp-7-2gLTAFih9Dpt3/view?usp=sharing

print('Введите три разных числа')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if b < a < c or c < a < b:
    m = a
elif a < b < c or c < b < a:
    m = b
else:
    m = c
print(f'Среднее число = {m}')
