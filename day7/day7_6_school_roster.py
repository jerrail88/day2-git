# Day 7 Exercise 6 - Combined Data Structures (School Roster)

school = {
    "Grade 1": ["Alice", "Bob", "Charlie"],
    "Grade 2": ["David", "Eva"],
    "Grade 3": ["Frank", "Grace", "Hannah", "Ian"]
}

print("=== School Roster ===")

# Print each grade and the list of students
for grade, students in school.items():
    print(f"\n{grade}:")
    for student in students:
        print(f" - {student}")

# Add a new student
school["Grade 2"].append("Zoe")

print("\nAdded Zoe to Grade 2!")
print("Updated roster:\n")

# Reprint updated school roster
for grade, students in school.items():
    print(f"{grade}: {students}")
