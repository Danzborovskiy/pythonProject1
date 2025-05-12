from math import pow, sqrt
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
n = x1 - x2
m = y1 - y2
z = pow(n, 2) + pow(m, 2)
print(sqrt(z))