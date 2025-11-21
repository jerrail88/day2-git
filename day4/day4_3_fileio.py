# Write some text to a file
with open("example.txt", "w") as f:
    f.write("Hello, this is a file I/O example.\n")
    f.write("We can write multiple lines.\n")

# Read the file and print its contents
with open("example.txt", "r") as f:
    content = f.read()

print("File contents:")
print(content)
