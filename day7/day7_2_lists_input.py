# day7_2_lists_input.py

# Start with an empty list
user_numbers = []

# Ask user how many numbers to input
count = int(input("How many numbers do you want to add to the list? "))

# Take input from user and add to the list
for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    user_numbers.append(num)

# Print the list
print(f"Your list: {user_numbers}")

# Remove the first number (if list not empty)
if user_numbers:
    removed = user_numbers.pop(0)
    print(f"Removed the first number: {removed}")

# Print squared values using list comprehension
squares = [x**2 for x in user_numbers]
print(f"Squares of remaining numbers: {squares}")
