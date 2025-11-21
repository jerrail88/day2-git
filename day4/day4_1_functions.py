# Function that greets a user
def greet(name):
    return f"Hello, {name}!"

# Call the function
user_name = input("Enter your name: ")
message = greet(user_name)
print(message)
