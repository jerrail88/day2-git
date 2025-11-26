students = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 22, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"}
}

for name, info in students.items():
    print(f"Student: {name}")
    print(f"  Age: {info['age']}")
    print(f"  Major: {info['major']}")
    print()
