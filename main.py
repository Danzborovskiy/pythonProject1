n = int(input())
counter = 0
while n > 0:
    counter += 1
    n //= 10
print(counter)