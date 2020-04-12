# По введенным пользователем координатам двух точек вывести уравнение прямой
# вида y = kx + b, проходящей через эти точки.
# https://drive.google.com/file/d/1iYbrYgvC8WgpNAFp-7-2gLTAFih9Dpt3/view?usp=sharing

print("Введите координаты первой точки")
x1 = float(input('Введите х1: '))
y1 = float(input('Введите y1: '))
print("Введите координаты второй точки")
x2 = float(input('Введите х2: '))
y2 = float(input('Введите y2: '))

if x1 != x2:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k}*x + {b}')
else:
    b = y2
    print(f'y = {b}')
