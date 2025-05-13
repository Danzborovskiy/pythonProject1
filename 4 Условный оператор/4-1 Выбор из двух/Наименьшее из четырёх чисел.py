print('''Напишите программу, которая определяет наименьшее из четырёх чисел.''')

a, b, c, d = int(input()), int(input()), int(input()), int(input())
ab = 0
cd = 0
if a < b:
    ab = a
else:
    ab = b
if c < d:
    cd = c
else:
    cd = d
if ab < cd:
    print(ab)
else:
    print(cd)
