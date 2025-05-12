a, b, c = input(), input(), input()
x = len(a)
y = len(b)
z = len(c)
if (2 * y - z - x) * (2 * z - y - x) * (2 * x - z - y) == 0:
    if abs(x - y) == abs(y - z) or abs(z - x) == abs(x - y) or abs(x - z) == abs(z - y):
        print('YES')
else:
    print('NO')