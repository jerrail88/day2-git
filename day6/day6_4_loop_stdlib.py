# day6_4_loop_stdlib.py

import random

def roll_dice():
    """Simulate rolling a six-sided dice."""
    return random.randint(1, 6)

def play_game(rounds):
    """Roll the dice multiple times and print results."""
    for i in range(1, rounds + 1):
        result = roll_dice()
        print(f"Roll {i}: {result}")

# Ask user for number of rolls
num_rolls = int(input("How many times do you want to roll the dice? "))
play_game(num_rolls)
