a = int(input())
b = int(input())

max_sum = 0
best_num = a

for i in range(a, b + 1):
    current_sum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            current_sum += j

    if current_sum > max_sum:
        max_sum = current_sum
        best_num = i
    elif current_sum == max_sum and i > best_num:
        best_num = i

print(best_num, max_sum)
