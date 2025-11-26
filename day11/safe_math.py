# Day 11 - Exercise 3: Safe Math Module with Exception Handling

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        return "Error: Invalid number."
