# Function to write a list of names to a file
def write_names(filename, names):
    with open(filename, "w") as f:
        for name in names:
            f.write(name + "\n")

# List of names
students = ["Alice", "Bob", "Charlie", "Diana"]

# Call the function
write_names("students.txt", students)

print("Names written to students.txt successfully.")
