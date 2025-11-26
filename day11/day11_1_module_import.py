# Day 11 - Exercise 1: Importing Custom Module

import my_utils

name = input("Enter your name: ")
print(my_utils.greet(name))

number = int(input("Enter a number: "))
print(f"Square: {my_utils.square(number)}")
print(f"Cube: {my_utils.cube(number)}")
