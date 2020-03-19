# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков. Проанализировать результат и
# определить программы с наиболее эффективным использованием памяти.

# Les3_task4. Определить, какое число в массиве встречается чаще всего.
import collections
import random


def arr(size):
    array = [random.randint(0, size // 1.5) for _ in range(size)]
    return array


# вариант 1
def loop(array):
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]
    return (f'Число {num} встречется {frequency} раз(а)' if frequency > 1 else
            'Все элементы уникальны')


# вариант 2
def memo(array):
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            num = item
    if num is not None:
        return f'Число {num} встречется {frequency} раз(а)'
    else:
        return 'Все элементы уникальны'


# вариант3
def Counter(array):
    num = (collections.Counter(''.join(map(str, array)))).most_common(1)
    return num


# Решение домшки:
import sys

array = arr(10)


def count_mem(obj):
    print(f'type={type(obj)}, size={sys.getsizeof(obj)}, {obj=}')
    size = sys.getsizeof(obj)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items:
                count_mem(key)
                count_mem(value)
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
        elif not isinstance(obj, str):
            for item in obj:
                count_mem(item)
                size += sys.getsizeof(item)
    return size

# Из документации Python:
# "При выполнении функции вводится новая таблица символов, используемая для
# локальных переменных функции. Точнее, все назначения переменных в функции
# сохраняют значение в локальной таблице символов; тогда как ссылки на
# переменные сначала смотрят в локальной таблице символов, затем в локальных
# таблицах символов включающих функций, затем в глобальной таблице символов и,
# наконец, в таблице встроенных имен."
# Мысль:
# скормить рекурсивной функции подсчета подопытную функцию. Функция подсчета
# потрошит подопытную , вытаскивает её таблицу имен и получает переменные.
# Внимание вопрос! Как получить доступ к э той таблице?

# def vairebls(func):
#     list_vair = func.какой-то способ получения ссылок на лок-е переменные функции
#     for vair in list_vair:
#         total_size = count_mem(obj)
#     print(f'Общий ращмер переменных = {total_size}'

