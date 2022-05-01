# 1
print('123', 'число', 'любое')

# 2
a = 5
if a > 10:
    print('Одно сообщение')
else:
    print('Другое сообщение')

# 3
a = 30
if a <= 10:
    print('Одно сообщение')
elif a <= 25:
    print('Другое сообщение')
else:
    print('Третье сообщение')

#4
a = 5
b = 3
print('Остаток от деления: ', a % b)

#5
a = int(input('введите одну переменную: '))
b = int(input('введите другую переменную: '))
print('Частное: ', a/b)

#6
age = 13
if isinstance(age, int):
    if age < 0:
        print('Число меньше 0')
    elif age ==0:
        print('Это 0')
    else:
        print('Число больше 0')
else:
    print('Это не целое число')