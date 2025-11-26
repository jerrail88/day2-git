# Day 10 - Exercise 4: File Exception Handling

def read_file_safely(filename):
    try:
        with open(filename, "r") as f:
            print("File content:")
            print(f.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for a filename
filename = input("Enter a filename to read: ")

read_file_safely(filename)
