a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a2 < a1:
    x1 = a2
    y1 = b2
    x2 = a1
    y2 = b1
else:
    x1 = a1
    y1 = b1
    x2 = a2
    y2 = b2

if x2 == y1:
    print(x2)
elif x2 > y1:
    print("пустое множество")
elif x2 >= x1 and x2 <= y1:
    if y2 < y1:
        y = y2
    else:
        y = y1
    if x2 == x1:
        x = x1
    else:
        x = x2
    print(x, y)