x = int(input())
a = x // 100
b = (x // 10) % 10
c = x % 10
d = max(a, b, c)
e = min(a, b, c)
if (d - e) == ((a + b + c) - d - e):
    print('Число интересное')
else:
    print('Число неинтересное')