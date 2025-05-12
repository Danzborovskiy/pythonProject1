from math import pow, sqrt
a = float(input())
b = float(input())
c = float(input())
d = pow(b, 2) - 4 * a * c
if d > 0:
    e = (-b - sqrt(d)) / (2 * a)
    f = (-b + sqrt(d)) / (2 * a)
    print(min(e, f))
    print(max(e, f))
elif d == 0:
    print(-(b / (2 * a)))
else:
    print('Нет корней')