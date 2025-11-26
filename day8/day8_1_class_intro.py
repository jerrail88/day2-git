# Day 8 - Exercise 1: Basic Class

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Create object
my_dog = Dog("Buddy", 3)

print(f"Dog's Name: {my_dog.name}")
print(f"Dog's Age: {my_dog.age}")

my_dog.bark()
