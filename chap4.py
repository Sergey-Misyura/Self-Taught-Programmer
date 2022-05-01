# 1
def sqr(a: int):
    """функция возведения в квадрат"""
    return a ** 2


print(sqr(12))


# 2
def ret_str(a: str):
    """функция возвращает строку"""
    return a


print(ret_str('1'))


# 3
def func_3(a, b, c, d=4, f=5):
    """функция перемножения"""
    return a * b * c * d * f


print(func_3(1, 2, 3))


# 4
def divis_2(a: int):
    """функция деления на 2"""
    return a / 2


def multi_4(a: int):
    """функция умножения на 4"""
    return a * 4


per = divis_2(4)
print(multi_4(per))


# 5
def str_to_float(a: str):
    """
    функция преобразования строки к
    числу с плавающей точкой
    """
    try:
        return float(a)
    except ValueError:
        return 'этот аргумент не подходит'


print(str_to_float('13'))
