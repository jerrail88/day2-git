# Day 9 - Exercise 5: Combining Dictionaries with Loops

# Two dictionaries of student grades
math_grades = {"Alice": 90, "Bob": 82, "Charlie": 95}
science_grades = {"Alice": 85, "Bob": 88, "Charlie": 92}

# Combine dictionaries into a single dictionary with nested dictionaries
combined_grades = {}
for student in math_grades:
    combined_grades[student] = {
        "Math": math_grades[student],
        "Science": science_grades.get(student, 0)
    }

# Print combined grades
for student, subjects in combined_grades.items():
    print(f"{student}'s grades:")
    for subject, grade in subjects.items():
        print(f"  {subject}: {grade}")

# Calculate average for each student
for student, subjects in combined_grades.items():
    average = sum(subjects.values()) / len(subjects)
    print(f"{student}'s average grade: {average:.2f}")
