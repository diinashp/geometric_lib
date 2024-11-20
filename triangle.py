def area(a, b, c):
"""принимает числа a, b, c, возвращает (a + b + c)/2"""
    p = (a + b + c) / 2
    return (p*(p-a)*(p-b)*(p-c))**0.5


def perimeter(a, b, c):
"""принимает числа a, b, c, возвращает периметр треугольника со сторонами a, b, c"""
    return a + b + c
