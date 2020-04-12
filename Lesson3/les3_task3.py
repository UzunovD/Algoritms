# В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив:       {arr}')

min_value = max_value = arr[0]
min_idx = max_idx = 0

for i in range(len(arr)):
    if arr[i] < min_value:  # определяем минимальное min_value
        min_value = arr[i]
        min_idx = i
    elif arr[i] > max_value:  # определяем максимальное max_value
        max_value = arr[i]
        max_idx = i
# перестановка
arr[min_idx] = max_value
arr[max_idx] = min_value

print(f'Результирующий массив: {arr}')
