n = int(input())
total = 0
m = n
sec = 0
while n != 0:
    last_digit = n % 10
    total +=1
    n = n // 10
sec = m % (10 ** (total - 1)) // 10 ** (total - 2)
print(sec)