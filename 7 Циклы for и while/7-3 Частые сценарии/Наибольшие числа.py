total1 = 1
total2 = 1
n = int(input())
for i in range(1, n + 1):
    m = int(input())
    if m > total1:
        total2 = total1
        total1 = m
    elif m > total2:
        total2 = m
print(total1)
print(total2)