# Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна
# определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict, namedtuple

regeestry = defaultdict(int)

num_firm = int(input('Введите число пердприятий:\n'))
total_profit = 0

for num in range(num_firm):
    name = input('Введите название фирмы:\n')
    for quarter in range(4):
        quarter_profit = int(input(f'Введите прибыль за {quarter + 1} квартал:\n'))
        regeestry[name] += quarter_profit
        total_profit += quarter_profit

print(regeestry)

average = total_profit / num_firm



