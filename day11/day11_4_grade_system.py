# Day 11 - Exercise 4: Multi-File Student Grade System

import students
import grades

for name, grade_list in students.students.items():
    avg = grades.calculate_average(grade_list)
    high = grades.highest_grade(grade_list)
    low = grades.lowest_grade(grade_list)

    print(f"\n{name}'s Grades:")
    print("  List:", grade_list)
    print(f"  Average: {avg:.2f}")
    print(f"  Highest: {high}")
    print(f"  Lowest: {low}")
