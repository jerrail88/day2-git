# day7_1_lists.py

# Create a list of numbers
numbers = [2, 4, 6, 8, 10]

# Add a number
numbers.append(12)

# Remove a number
numbers.remove(4)

# Iterate through the list and print each number
for num in numbers:
    print(f"Number: {num}")

# List comprehensions: squares
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")
