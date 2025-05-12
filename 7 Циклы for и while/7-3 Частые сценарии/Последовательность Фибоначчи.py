total1 = 1
total2 = 0
n = int(input())
for i in range(1, n + 1):
    a = total1
    total1 = a + total2
    total2 = a
    print(a, end = ' ')