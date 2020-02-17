# Найти сумму и произведение цифр трехзначного числа, которое вводит
# пользователь.
# https://drive.google.com/file/d/1iYbrYgvC8WgpNAFp-7-2gLTAFih9Dpt3/view?usp=sharing

print('Введите трехзначное целое положительное число')
n = int(input('Введите число:'))

a = n // 100 % 10
b = n // 10 % 10
c = n % 10
s = a + b + c
m = a * b * c

print(f'Сумма: {s}, Произведение: {m}')
