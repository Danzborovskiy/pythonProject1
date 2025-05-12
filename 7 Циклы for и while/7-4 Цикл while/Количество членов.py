text = input()
count = 0
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    count += 1
    text = input()
print(count)