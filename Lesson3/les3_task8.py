# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.

row = 3
column = 2
a = []

for i in range(row):
    b = []
    sum_row = 0
    for j in range(column):
        b.append(int(input()))
        sum_row += b[j]
    b.append(sum_row)
    a.append(b)
for _ in a:
    print(f'{_}')