import math


def area(r):
    if(r < 0):
        raise AssertionError("error")
    return math.pi * r * r


def perimeter(r):
    if(r < 0):
        raise AssertionError("error")
    return 2 * math.pi * r
