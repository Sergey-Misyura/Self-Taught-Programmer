import math


# 1
class Apple():
    def __init__(self, color, weight, freshness, circle):
        self.color = color
        self.weight = weight
        self.freshness = freshness
        self.circle = circle


# 2
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi


circle = Circle(6)
print("Площадь круга: ", circle.area())


# 3

class Triangle():
    def __init__(self, stor_1, stor_2, ugol):
        """
        :param stor_1: сторона 1
        :param stor_2: сторона 2
        :param ugol: угол между ними d градусах
        """
        self.stor_1 = stor_1
        self.stor_2 = stor_2
        self.ugol = ugol

    def area(self):
        """
        возвращает площадь треугольника
        """
        return 0.5 * (self.stor_1 * self.stor_2 * math.sin(self.ugol * math.pi / 180))


triangle = Triangle(3, 4, 90)
print("Площадь треугольника: ", triangle.area())


# 4
class Hexagon():
    def __init__(self, stor_1, stor_2, stor_3, stor_4, stor_5, stor_6):
        self.stor_1 = stor_1
        self.stor_2 = stor_2
        self.stor_3 = stor_3
        self.stor_4 = stor_4
        self.stor_5 = stor_5
        self.stor_6 = stor_6

    def calculate_perimeter(self):
        return self.stor_1 + self.stor_2 + self.stor_3 + self.stor_4 + self.stor_5 + self.stor_6


hexagon = Hexagon(3, 4, 5, 6, 7, 8)
print("Периметр гексагона: ", hexagon.calculate_perimeter())
