# 1
musician = ['Eminem', '50 cent', 'Metallica', 'Disturbed', 'Артур Пирожков', 'Gayazov$ Brother$']

# 2
locations = [(39.435414, 43.359502), (37.36, 55.45), (40.16, 43.17)]

# 3
my_facts = {'рост': '179',
            'вес': '80',
            'цвет': 'пурпурный',
            'актер': 'Джерард Батлер'}

# 4
ans = input('Укажите что хотите получить: рост, вес, цвет, актер- ')
if ans in my_facts:
    result = my_facts[ans]
    print(result)

# 5
songs = ['Lose yourself', 'Candy shop', 'Unforgiven', 'Shout 2000', 'Чика-Вероника', 'Малиновая лада']
my_songs = dict(zip(musician, songs))
print(my_songs)