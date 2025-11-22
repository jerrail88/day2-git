# Day 5 - Exercise 3: Try/Except Error Handling

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input, please enter a valid number.")
