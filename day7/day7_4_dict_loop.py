# Day 7 Exercise 4 - Looping through a dictionary

person = {
    "name": "Jerrail",
    "age": 32,
    "city": "Chicago",
    "hobby": "Coding"
}

print("Looping through KEYS:")
for key in person.keys():
    print(key)

print("\nLooping through VALUES:")
for value in person.values():
    print(value)

print("\nLooping through BOTH key + value:")
for key, value in person.items():
    print(f"{key} → {value}")
