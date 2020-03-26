# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный
# массив, заданный случайными числами на промежутке [-100; 100). Выведите на
# экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход
# массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться
# сортировка пузырьком. Улучшенные версии сортировки, например, расчёской,
# шейкерная и другие в зачёт не идут.
import random


def bubble_sort(array):
    n = 1

    while n < len(array):
        is_sorted = True
        for i in range(len(array) - n):  # n для естественного поведения
            if array[i] < array[i + 1]:  # если левый меньше правого
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        if is_sorted:
            break

        n += 1
        print(array)


SIZE = 10
LIMIT = 100
arr = [random.randrange(-LIMIT, LIMIT) for _ in range(SIZE)]
print(arr)
bubble_sort(arr)
print(arr)
