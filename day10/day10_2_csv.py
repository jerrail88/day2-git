# Day 10 - Exercise 2: Working with CSV Files
import csv

# Sample data
students = [
    {"name": "Alice", "math": 90, "science": 85},
    {"name": "Bob", "math": 82, "science": 88},
    {"name": "Charlie", "math": 95, "science": 92}
]

# Write CSV
with open("students.csv", "w", newline="") as csvfile:
    fieldnames = ["name", "math", "science"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for student in students:
        writer.writerow(student)

print("CSV file 'students.csv' created.")

# Read CSV
with open("students.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    print("Reading CSV content:")
    for row in reader:
        print(row)
