a, b = input(), input()
if a == 'красный' and b == 'красный':
    print('красный')
elif a == 'синий' and b == 'синий':
    print('синий')
elif a == 'желтый' and b == 'желтый':
    print('желтый')
elif a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
    print('фиолетовый')
elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
    print('оранжевый')
elif a == 'желтый' and b == 'синий' or a == 'синий' and b == 'желтый':
    print('зеленый')
else:
    print('ошибка цвета')