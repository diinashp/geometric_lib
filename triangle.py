def area(a, b, c):
    p = (a + b + c) / 2
    if a < 0 or b < 0 or c < 0:
        raise AssertionError("error")
    if a + b <= c or a + c <= b or b + c <= a:
        raise AssertionError("error")      
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise AssertionError("error")
    if a + b <= c or a + c <= b or b + c <= a:  
        raise AssertionError("error")
    return a + b + c
