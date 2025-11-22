# Day 5 - Exercise 2: Looping Through Lists

numbers = [3, 7, 12, 5, 9]

print("Numbers in the list:")
for num in numbers:
    print(num)

# Calculate the sum manually (without using sum())
total = 0
for num in numbers:
    total += num

print("Total:", total)

# Print only numbers greater than 6
print("Numbers greater than 6:")
for num in numbers:
    if num > 6:
        print(num)
