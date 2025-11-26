# Day 10 - Exercise 5: File Processing Challenge

def process_numbers(filename):
    numbers = []
    
    try:
        with open(filename, "r") as f:
            for line in f:
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    if not numbers:
        print("No valid numbers found in the file.")
        return

    total = sum(numbers)
    avg = total / len(numbers)
    highest = max(numbers)
    lowest = min(numbers)

    # Write results to a new file
    output_file = "results.txt"
    with open(output_file, "w") as f:
        f.write(f"Total: {total}\n")
        f.write(f"Average: {avg:.2f}\n")
        f.write(f"Highest: {highest}\n")
        f.write(f"Lowest: {lowest}\n")

    print(f"Results written to '{output_file}'")


# Ask user for file
filename = input("Enter a filename containing numbers: ")
process_numbers(filename)
