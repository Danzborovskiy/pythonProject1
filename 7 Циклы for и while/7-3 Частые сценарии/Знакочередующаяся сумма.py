n = int(input())
total = 0
for i in range(1, n + 1):
    n = (-1) ** (i + 1) * i
    total += n
print(total)