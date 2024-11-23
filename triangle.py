def area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise AssertionError("error")
    if not (a + b > c and a + c > b and b + c > a):
        if a == 0 and b == 0 and c == 0:
            return 0
        raise AssertionError("error")
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise AssertionError("error")
    if not (a + b > c and a + c > b and b + c > a):
        if a == 0 and b == 0 and c == 0:
            return 0
        raise AssertionError("error")
    return a + b + c
