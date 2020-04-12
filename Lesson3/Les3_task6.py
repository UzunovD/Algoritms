# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 5

arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный список: {arr}')

min_value = max_value = arr[0]
min_idx = max_idx = 0

for idx, value in enumerate(arr):
    if value < min_value:  # определяем минимальное min_value
        min_value = value
        min_idx = idx
    elif value > max_value:  # определяем максимальное max_value
        max_value = value
        max_idx = idx
# print(f'{min_value=}, {min_idx=}, {max_value=}, {max_idx=}') #
# промежуточные результаты для контроля

# Сумма элементов от мин до максимального:
if min_idx < max_idx:
    arr = arr[min_idx + 1:max_idx]
else:
    arr = arr[min_idx - 1:max_idx:-1]
# print(arr)  # контроль списка
total = 0
_ = 0
for j in arr:
    total = _ + j
    _ = total

print(f'Сумма элементов между {min_value} и {max_value}: {total}')
