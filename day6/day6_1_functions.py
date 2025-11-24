# day6_1_functions.py

def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}! Welcome to Day 6."

# Ask user for input
user_name = input("Enter your name: ")
message = greet(user_name)
print(message)
