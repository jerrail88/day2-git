# Day 9 - Exercise 3: Dictionary Methods & Built-in Functions

grades = {"Alice": 90, "Bob": 85, "Charlie": 92}

# Get all keys
print("Keys:", grades.keys())

# Get all values
print("Values:", grades.values())

# Get all items
print("Items:", grades.items())

# Use get() method (safe access)
print("Bob's grade:", grades.get("Bob"))
print("Eve's grade (default):", grades.get("Eve", "Not Found"))

# Check if key exists
if "Alice" in grades:
    print("Alice is in the dictionary")

# Remove a key
removed_grade = grades.pop("Charlie")
print(f"Removed Charlie's grade: {removed_grade}")
print("Updated grades:", grades)

# Clear the dictionary
grades.clear()
print("Cleared dictionary:", grades)
