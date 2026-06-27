import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error"
    return a / b

def modulus(a, b):
    return a % b

def power(a):
    return a ** 2

def square_root(a):
    return math.sqrt(a)

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    return math.tan(math.radians(a))