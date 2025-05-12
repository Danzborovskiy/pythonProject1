n = int(input())
last_digit = n % 10
flag = True
while n != 0:
    new_digit = n % 10
    if new_digit != last_digit:
        flag = False
    n = n // 10
if flag == True:
    print('YES')
if flag == False:
    print('NO')