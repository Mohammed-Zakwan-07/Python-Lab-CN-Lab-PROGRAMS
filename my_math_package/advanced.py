import math

def power(base, exp):
    return base ** exp

def square_root(x):
    if x < 0:
        raise ValueError("Square root of negative number")
    return math.sqrt(x)

def factorial(n):
    if n < 0:
        raise ValueError("Factorial of negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
