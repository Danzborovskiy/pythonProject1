flag = True
for i in range(1, 11):
    n = int(input())
    if n % 2 != 0:
        flag = False
if flag == True:
    print('YES')
else:
    print('NO')