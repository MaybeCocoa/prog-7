import math


def f(x):
    return math.sin(x) 

def integrate(a, b, n_iter=10**6):
    result = 0
    h = 1 / n_iter
    while a <= b - h:
        result += (f(a) + f(a + h)) / 2 * h
        a += h
    return result
