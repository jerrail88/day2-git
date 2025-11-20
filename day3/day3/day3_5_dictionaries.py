# Create a dictionary of student grades
grades = {
    "Alice": 90,
    "Bob": 82,
    "Charlie": 95
}

# Print all students and their grades
for student, grade in grades.items():
    print(student, "has a grade of", grade)

# Add a new student
grades["Diana"] = 88

print("\nUpdated grades:")
for student, grade in grades.items():
    print(student, "has a grade of", grade)

