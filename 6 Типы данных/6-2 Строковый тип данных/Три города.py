a, b, c = input(), input(), input()
x = len(a)
y = len(b)
z = len(c)
if min(x, y, z) == len(a):
    print(a)
elif min(x, y, z) == len(b):
    print(b)
elif min(x, y, z) == len(c):
    print(c)
if max(x, y, z) == len(a):
    print(a)
elif max(x, y, z) == len(b):
    print(b)
elif max(x, y, z) == len(c):
    print(c)
