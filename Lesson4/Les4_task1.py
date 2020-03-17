# Определить, какое число в массиве встречается чаще всего.

import random
import timeit
import cProfile


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



print('вариант 1 loop')
array = arr(10)
print(timeit.timeit('loop(array)', number=100, globals=globals()))  # 0.0008303999999999985
cProfile.run('loop(array)')  # 11    0.000    0.000    0.000    0.000 {built-in method builtins.len}

array = arr(100)
print(timeit.timeit('loop(array)', number=100, globals=globals()))  # 0.06570210000000001
cProfile.run('loop(array)')  # 101    0.000    0.000    0.000    0.000 {built-in method builtins.len}

array = arr(1000)
print(timeit.timeit('loop(array)', number=100, globals=globals()))  # 3.9897042999999996
cProfile.run('loop(array)')  # 1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}

array = arr(10000)
print(timeit.timeit('loop(array)', number=100, globals=globals()))  # 457.0741585
cProfile.run('loop(array)')  # 10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
# Вариант #1 имеет вложенный цикл, следовательно сложность О(n2) квадратичная.
# Граффик функции - парабола, с увеличением входных данных время обработки
# увеличивается с большей интенсивностью. Сложность алгоритма квадратичная
# О(n2)


#вариант 2
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


print('вариант 2 memo')
array = arr(10)
print(timeit.timeit('memo(array)', number=100, globals=globals()))  # 0.0002343999999999992
cProfile.run('memo(array)')  #

array = arr(100)
print(timeit.timeit('memo(array)', number=100, globals=globals()))  # 0.0016479000000000008
cProfile.run('memo(array)')  #

array = arr(1000)
print(timeit.timeit('memo(array)', number=100, globals=globals()))  # 0.019783799999999997
cProfile.run('memo(array)')  #

array = arr(10000)
print(timeit.timeit('memo(array)', number=100, globals=globals()))  # 0.21502010000000002
cProfile.run('memo(array)')  #

array = arr(100000)
print(timeit.timeit('memo(array)', number=100, globals=globals()))  # 2.895196
cProfile.run('memo(array)')  #

array = arr(1000000)
print(timeit.timeit('memo(array)', number=100, globals=globals()))  # 41.213988400000005
cProfile.run('memo(array)')  #
# Граффик функции варианта 2 - прямая, с увеличением входных данных время
# обработки увеличивается прямопропорционально. Сложность алгоритма О(n)

# N = 100
# print('вариант 2 memo')
# while N <= 10000:
#     array = arr(N)
#     print(timeit.timeit('memo(array)', number=100, globals=globals()))
#     N += 100


# вариант 3
def max_fr(array):
    max_ = max(array)
    num = array[0]
    frequency = 1
    for i in range(max_):
        spam = array.count(i)
        if spam > frequency:
            frequency = spam
            num = i
        spam = 0
    return (f'Число {num} встречется {frequency} раз(а)' if frequency > 1 else
            'Все элементы уникальны')
# Вариант 3 представляет параболическую сложность O(n2) Но в отличии от 1
# варианта, более эффективен и замедляется не столь интенсивно.


print('вариант 3 max_fr')
array = arr(10)
print(timeit.timeit('max_fr(array)', number=100, globals=globals()))  # 0.0011170999999999993
cProfile.run('max_fr(array)')  #         5    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}

array = arr(100)
print(timeit.timeit('max_fr(array)', number=100, globals=globals()))  # 0.050612700000000004
cProfile.run('max_fr(array)')  #        66    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}

array = arr(1000)
print(timeit.timeit('max_fr(array)', number=100, globals=globals()))  # 5.0871075
cProfile.run('max_fr(array)')  #       666    0.011    0.000    0.011    0.000 {method 'count' of 'list' objects}

array = arr(10000)
print(timeit.timeit('max_fr(array)', number=100, globals=globals()))  # 565.3294479
cProfile.run('max_fr(array)')  #      6666    1.098    0.000    1.098    0.000 {method 'count' of 'list' objects}

# Вариант 3 имеет линейную сложность O(n)
# N = 100
# print('вариант 3 max_fr')
# while N <= 10000:
#     array = arr(N)
#     print(timeit.timeit('max_fr(array)', number=100, globals=globals()))
#     N += 100


# Из трех вариантов 2 самый эффективный, как по времени относительного
# вычисления, # так и по вреиени в перспективе увеличения входных данных.
# Из выдачи cProfile видно, что большое время затрацивалось на формировагие
# водного массива, в связи с чем, формирование массива был вынесено из функций.