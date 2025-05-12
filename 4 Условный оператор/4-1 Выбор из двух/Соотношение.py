a = int(input())
b = a // 1000
c = (a % 1000) // 100
d = (a % 100) // 10
e = a % 10
if (b + e) == (c - d):
    print('ДА')
else:
    print('НЕТ')