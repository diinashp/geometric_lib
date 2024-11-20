def area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise AssertionError("error")
    p = (a + b + c) / 2
    return (p*(p-a)*(p-b)*(p-c))**0.5


def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise AssertionError("error")
    return a + b + c
