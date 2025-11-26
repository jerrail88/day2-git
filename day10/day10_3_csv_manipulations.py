# Day 10 - Exercise 3: CSV Manipulations
import csv

# Read the CSV created in Exercise 2
students = []
with open("students.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert grades to integers
        row["math"] = int(row["math"])
        row["science"] = int(row["science"])
        students.append(row)

# Increase all math grades by 5
for student in students:
    student["math"] += 5

# Write updated CSV
with open("students_updated.csv", "w", newline="") as csvfile:
    fieldnames = ["name", "math", "science"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for student in students:
        writer.writerow(student)

print("Updated CSV 'students_updated.csv' created.")

# Calculate average per student and display
for student in students:
    average = (student["math"] + student["science"]) / 2
    print(f"{student['name']}'s average: {average}")
