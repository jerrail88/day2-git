# Function to read a file and print each line with line numbers
def read_file_with_numbers(filename):
    with open(filename, "r") as f:
        lines = f.readlines()  # Read all lines into a list
        for i, line in enumerate(lines, start=1):
            print(f"Line {i}: {line.strip()}")

# Call the function on the students.txt file from Exercise 4
read_file_with_numbers("students.txt")
