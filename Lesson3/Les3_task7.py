# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и
# различаться.

from random import randint

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 10

arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный список: {arr}')

n = 0
res = []

while n < 2:
    min_idx = 0
    min_value = arr[min_idx]
    for idx, value in enumerate(arr):
        if value < min_value:  # определяем min_value
            min_value = value
            min_idx = idx
    res.append(arr.pop(min_idx))  # вырезаем минимальное значение из списка
    n += 1
print(f'Два наименьших значения: {res[0]}, {res[1]}')
