# Day 9 - Exercise 1: Dictionaries

# Create a dictionary
student_grades = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92
}

# Access values
print("Alice's grade:", student_grades["Alice"])

# Loop through keys
for student in student_grades:
    print(student, ":", student_grades[student])

# Loop through items
for student, grade in student_grades.items():
    print(f"{student} has a grade of {grade}")

# Update a value
student_grades["Bob"] = 88
print("Updated grades:", student_grades)

# Add a new entry
student_grades["Diana"] = 95
print("Added new student:", student_grades)

# Delete an entry
del student_grades["Charlie"]
print("After deletion:", student_grades)
