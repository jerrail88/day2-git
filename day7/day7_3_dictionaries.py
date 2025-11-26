# Day 7 - Exercise 3: Dictionaries

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

name = input("Enter a student's name: ")

if name in students:
    print(f"{name}'s grade is {students[name]}")
else:
    print("Student not found.")
