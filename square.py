
def area(a):
    if a < 0:
        raise AssertionError("error")
    return a * a


def perimeter(a):
    if a < 0:
        raise AssertionError("error")
    return 4 * a
