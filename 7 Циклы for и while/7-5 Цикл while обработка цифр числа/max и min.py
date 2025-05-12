n = int(input())
min = 9
max = 0
while n != 0:
    last_digit = n % 10
    if last_digit > max:
        max = last_digit
    if last_digit < min:
        min = last_digit
    else:
        n = min
    n = n // 10
print('Максимальная цифра равна', max)
print('Минимальная цифра равна', min)