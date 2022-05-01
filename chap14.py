# 1

class Square():
    square_list = []

    def __init__(self, storona):
        self.storona = storona
        self.square_list.append(self)
# 2
    def __repr__(self):
        return f'{self.storona} на {self.storona} на {self.storona} на {self.storona}'

square_1 = Square(1)
square_2 = Square(2)
print("Список квадратов:", Square.square_list)

# 2
print(square_1)

# 3

def compare (a, b):
    if a is b:
        return True
    else:
        return False

print(compare(square_2, square_2))