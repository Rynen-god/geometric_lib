from math import sqrt
def area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise AssertionError("Стороны должны быть положительными")
    if a + b <= c or a + c <= b or b + c <= a:
        raise AssertionError("Треугольник с такими сторонами не существует")
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))
def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise AssertionError("Стороны не могут быть отрицательными")
    return a + b + c
