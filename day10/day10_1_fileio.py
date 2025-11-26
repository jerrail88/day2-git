# Day 10 - Exercise 1: Reading & Writing Text Files

# Write to a file
with open("example.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("Welcome to Day 10 Exercise 1.\n")

# Read from the file
with open("example.txt", "r") as f:
    content = f.read()

print("File content:")
print(content)

# Append to the file
with open("example.txt", "a") as f:
    f.write("Appending a new line.\n")

# Read line by line
with open("example.txt", "r") as f:
    print("Reading line by line:")
    for line in f:
        print(line.strip())
