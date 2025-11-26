# Day 11 - Exercise 2: Using a Custom Package

from mymath.addition import add
from mymath.subtraction import subtract
from mymath.multiplication import multiply

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Add: {add(a, b)}")
print(f"Subtract: {subtract(a, b)}")
print(f"Multiply: {multiply(a, b)}")
