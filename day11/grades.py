# Day 11 - Exercise 4: Grade Calculation Module

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def highest_grade(grades):
    return max(grades) if grades else 0

def lowest_grade(grades):
    return min(grades) if grades else 0
