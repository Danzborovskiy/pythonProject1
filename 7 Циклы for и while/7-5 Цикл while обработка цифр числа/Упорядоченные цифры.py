n = int(input())
last_digit = 0
flag = True
while n != 0:
    new_digit = n % 10
    if new_digit < last_digit:
        flag = False
    last_digit = new_digit
    n = n // 10
if flag == True:
    print('YES')
if flag == False:
    print('NO')