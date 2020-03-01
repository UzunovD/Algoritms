# В массиве найти максимальный отрицательный элемент. Вывести на экран его
# значение и позицию в массиве. Примечание к задаче: пожалуйста не путайте
# «минимальный» и «максимальный отрицательный». Это два абсолютно разных
# значения.

from random import randint

SIZE = 200
MIN_ITEM = -100
MAX_ITEM = 100

arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Исходный массив:')
print(arr)

max_negative_value = float('-inf')  # начальное отрицательное число

for i in range(len(arr)):
    if arr[i] < 0:
        if arr[i] > max_negative_value:  # определяем макс. отрицательное число
            max_negative_value = arr[i]
            max_negative_idx = i
print(f'''Максимальное отрицательное число: {max_negative_value},
индекс максимального отрицательного числа: {max_negative_idx}''')
