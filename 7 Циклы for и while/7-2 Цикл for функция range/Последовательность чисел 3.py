m = int(input())
n = int(input())
m = m % 2 - 1 + m
n = n - 1
for i in range(m, n, -2):
    print(m)
    m = m - 2
