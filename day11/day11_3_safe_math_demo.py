# Day 11 - Exercise 3: Using Safe Math Module

import safe_math

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert inputs
a = safe_math.safe_convert(num1)
b = safe_math.safe_convert(num2)

print("Converted values:", a, b)

# If either conversion failed, stop
if isinstance(a, str) or isinstance(b, str):
    print("Cannot continue due to invalid input.")
else:
    print("Division result:", safe_math.safe_divide(a, b))
