# Day 9 - Exercise 4: Dictionary Comprehensions & Filtering

# Original dictionary
grades = {"Alice": 90, "Bob": 82, "Charlie": 95, "Diana": 78}

# Dictionary comprehension: square the grades
squared_grades = {student: grade**2 for student, grade in grades.items()}
print("Squared grades:", squared_grades)

# Filter dictionary: only students with grade >= 85
high_grades = {student: grade for student, grade in grades.items() if grade >= 85}
print("High grades:", high_grades)

# Increment all grades by 5
incremented_grades = {student: grade + 5 for student, grade in grades.items()}
print("Incremented grades:", incremented_grades)
