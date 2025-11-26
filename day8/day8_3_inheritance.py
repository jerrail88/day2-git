# Day 8 - Exercise 3: Inheritance Example

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Create objects
my_cat = Cat("Whiskers")
my_dog = Dog("Buddy")

my_cat.speak()
my_dog.speak()
