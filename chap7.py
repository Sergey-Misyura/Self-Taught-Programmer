# 1
list_1 = ['Ходячие мертвецы', "Красавцы", "Клан Сопрано", "Дневники вампира"]
for i in list_1:
    print(i)

# 2
for i in range(25, 51):
    print(i)

# 3
for i, x in enumerate(list_1):
    print(i, x)

# 4
list_4 = [2, 3, 4]
while True:
    num = input('Угадайте число: ')
    if num == 'x':
        break
    elif num in list_4:
        print(num)
    else:
        print('нет такого числа')

# 5
list_5_1 = [8, 19, 148, 4]
list_5_2 = [9, 1, 33, 83]
res = []
for i in list_5_1:
    for n in list_5_2:
        res.append(i * n)
print(res)
