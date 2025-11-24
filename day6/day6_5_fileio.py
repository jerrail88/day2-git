# day6_5_fileio.py

def write_numbers(filename, n):
    """Write numbers 1 to n to a file."""
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            f.write(f"{i}\n")
    print(f"Wrote numbers 1 to {n} into {filename}")

def read_numbers(filename):
    """Read numbers from a file and print them."""
    print(f"Reading numbers from {filename}:")
    with open(filename, 'r') as f:
        for line in f:
            print(line.strip())

# Get user input
file_name = input("Enter filename: ")
num = int(input("Enter a number: "))

write_numbers(file_name, num)
read_numbers(file_name)
