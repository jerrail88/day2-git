def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def multiply_numbers(a, b):
    """Return the product of two numbers."""
    return a * b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Sum: {add_numbers(num1, num2)}")
print(f"Product: {multiply_numbers(num1, num2)}")
