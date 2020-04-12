# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 9
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Стартовый массив: {arr}')

diction = {}  # промежуточный словарь для накопления повторяющихся чисел
max_count = 0  # промежуточная переменная определяющая кол-во повторений
max_num = 0  # индекс по которому определяю самое частое число

for i in range(len(arr)):  # формируем промежуточный словарь в котором
    # храним повторяющееся число и количество повторений
    if arr[i] in diction:
        diction[arr[i]] = diction[arr[i]] + 1
    else:
        diction[arr[i]] = 1

for num, count in diction.items():  # находим максимально повторяющееся число
    if count > max_count:
        max_count = count
        max_num = num

print(
    f'Чаще всего встречается число {max_num} и оно встречается {max_count} '
    f'раза')
