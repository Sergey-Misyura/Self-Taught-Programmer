# 1
my_list = list()
with open('text.txt', 'r') as file:
    my_list.append(file.read())
print(my_list)

# 2
a = str(input('Как прошел день?'))
with open('test.txt', 'w') as file:
    file.write(a)

# 3
import csv

movies = [["Звездные войны", "Терминатор", "Искусственный интеллект"], ["Дурак", "Матильда", "Левиафан"],
          ["Люди в черном", "Я - робот", "Эволюция"]]
with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)

