#1
author = 'Чехов'
for i in author:
    print(i)
#2
answ_1 = input('Введите первый ответ: ')
answ_2 = input('Введите второй ответ: ')
print(f'Вчера я написал {answ_1}. Вчера я ходил в {answ_2}!')

#3
str_1 = 'олдос Хаксли родился в 1894 году.'
print(str_1.capitalize())

#4
str_2 = 'Где это? Кто это? Когда это?'
list_1 = 'Где это? Кто это? Когда это?'.split("? ")
print(list_1)

#5
list_2 = ['Рыжая', "лиса", "перепрыгнула", "через", "низкий", "забор", "."]
str_3 = ' '.join(list_2[:6]) + '.'
print(str_3)

#6
list_3 = 'Ребенок - зеркало поступков родителей.'
list_4 = list_3.replace('о', '0')
print(list_4)

#7
str_7 = 'Хемингуэй'
print(str_7.index('м'))

#8
str_8 = "'Пятачок,' сказал Винни-Пух, 'по-моему, пчёлы что-то подозревают!'"

#9
str_9 = 'три' + 'три' + 'три'
str_9_1 = 'три' * 3
print(str_9, str_9_1)

#10
str_10 = 'И зачем так орать! Я и в первый раз прекрасно слышал.'
print(str_10[:17])
