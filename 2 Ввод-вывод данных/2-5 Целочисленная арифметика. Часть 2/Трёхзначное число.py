n = int(input())
a = n % 10
b = (n // 10) % 10
c = n // 100
print('Сумма цифр =', (a + b + c))
print('Произведение цифр =', (a * b * c))