import math

# 3

class Shape():
    def what_am_i(self):
        print("Я - фигура")
# 1

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * self.length


class Square(Shape):
    def __init__(self, storona):
        self.storona = storona

    def calculate_perimeter(self):
        return self.storona * 4
# 2
    def change_size(self, znach):
        self.storona += znach

rectangle = Rectangle(3, 3)
square = Square(3)

print("Периметр круга:", rectangle.calculate_perimeter(),
      "периметр квадрата:", square.calculate_perimeter())

# 2
square.change_size(2)
print("Сторона квадрата:", square.storona)


# 3

square.what_am_i()
rectangle.what_am_i()

# 4

class Horse():
    def __init__(self, name):
        self.name = name

class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

horse = Horse('Тузик')
rider = Rider('Игнат', horse)

print("Имя всадника:", rider.name, 'имя лошади:', rider.horse.name)