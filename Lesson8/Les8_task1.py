# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных
# подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9

def count_substr(S):

    temp_set = set()
    for i in range(len(S)):
        for j in range(len(S) - 1 if i == 0 else len(S), i, -1):
            temp_set.add(hash(S[i:j]))
            # print(S[i:j], i, j, hash(S[i:j]))
            # print(temp_set)
    return len(temp_set)


def check_func():
    print('Test1 is ок' if count_substr("papa") == 6 else 'Test1 is failed')
    print('Test2 is ок' if count_substr("sova") == 9 else 'Test2 is failed')
    print('Test3 is ок' if count_substr("a a ") == 6 else 'Test3 is failed')


check_func()
