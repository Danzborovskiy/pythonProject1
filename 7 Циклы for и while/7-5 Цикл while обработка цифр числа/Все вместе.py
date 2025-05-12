num = int(input())
sum = 0
total = 0
product = 1
sred = 0
prom = 0
m = num
while num != 0:
    last_digit = num % 10
    sum = sum + last_digit
    total +=1
    product = product * last_digit
    num = num // 10
sred = sum / total
last = m % 10
first = m // 10 ** (total - 1)
prom = last + first
print(sum)
print(total)
print(product)
print(sred)
print(first)
print(prom)