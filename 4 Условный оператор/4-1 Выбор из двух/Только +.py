print('''Только +''')

a = int(input())
b = int(input())
c = int(input())
d = 0
if a < 0:
    d = 0
else:
    d = a
if b < 0:
    d = d
else:
    d = d + b
if c < 0:
    print(d)
else:
    print(d + c)