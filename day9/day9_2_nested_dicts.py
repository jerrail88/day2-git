# Day 9 - Exercise 2: Nested Dictionaries

# Nested dictionary: students with subjects and grades
students = {
    "Alice": {"Math": 90, "Science": 85},
    "Bob": {"Math": 78, "Science": 88},
    "Charlie": {"Math": 95, "Science": 92}
}

# Access a nested value
print("Alice's Science grade:", students["Alice"]["Science"])

# Loop through students
for student, subjects in students.items():
    print(f"\n{student}'s grades:")
    for subject, grade in subjects.items():
        print(f"  {subject}: {grade}")

# Update a grade
students["Bob"]["Math"] = 82
print("\nUpdated Bob's Math grade:", students["Bob"]["Math"])

# Add a new subject for a student
students["Charlie"]["English"] = 88
print("\nAdded English for Charlie:", students["Charlie"])

# Delete a subject
del students["Alice"]["Math"]
print("\nDeleted Alice's Math grade:", students["Alice"])
