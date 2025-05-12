n = int(input())
m = n // 2 + 1
for i in range(1, m + 1):
    for j in range(i):
        print('*', end = '')
    print()
for i in range(m - 1, 0, -1):
    for j in range(i):
        print('*', end = '')
    print()