# math_ops.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def power(base, exp):
    return base ** exp

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of negative number"
    return x ** 0.5
