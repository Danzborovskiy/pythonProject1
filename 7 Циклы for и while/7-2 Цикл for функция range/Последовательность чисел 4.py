m = int(input())
n = int(input())
for i in range(m, n + 1):
    if m % 17 == 0 or m % 10 == 9 or m % 15 == 0:
        print(m)
    m = m + 1