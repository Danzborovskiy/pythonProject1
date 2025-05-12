a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i < 2:
        continue
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)
print()
