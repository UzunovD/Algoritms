# Задача2
#
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2
# нечетные (3 и 5).

print('Введите целое положительное число')
num = input()
even = 0
uneven = 0
for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        uneven += 1
print(f'четных чисел: {even}, нечетных: {uneven}')


