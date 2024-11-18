# This program demonstrates how to use the input function in Python to get different types of input from the user.

# Getting a string input from the user
name = input("Enter your name: ")
print(f"Hello, {name}!", "The input	type is:", type(name))

# Getting an integer input from the user
age = int(input("Enter your age: "))
print(f"You are {age} years old.", "The input type is:", type(age))

# Getting a float input from the user
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters.", "The input type is:", type(height))

# Getting a boolean input from the user
is_student = input("Are you a student? (yes/no): ").lower() == 'yes'
print(f"Student status: {is_student}.", "The input type is:", type(is_student))

# Getting a list input from the user
favorite_colors = input("Enter your favorite colors, separated by commas: ").split(',')
print(f"Your favorite colors are: {favorite_colors}.", "The input type is:", type(favorite_colors))

# Getting a tuple input from the user
coordinates = tuple(map(float, input("Enter your coordinates (x, y), separated by a comma: ").split(',')))
print(f"Your coordinates are: {coordinates}.", "The input type is:", type(coordinates))

# Getting a dictionary input from the user
user_info = {}
user_info['name'] = input("Enter your name: ")
user_info['age'] = int(input("Enter your age: "))
user_info['city'] = input("Enter your city: ")
print(f"User information: {user_info}.", "The input type is:", type(user_info))