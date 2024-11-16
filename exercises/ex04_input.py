# This program demonstrates how to use the input function in Python to get different types of input from the user.

# Getting a string input from the user
name = input("Enter your name: ")
print("Hello, " + name + "!")
print (type(name))

# Getting an integer input from the user
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")
print (type(age))

# Getting a float input from the user
height = float(input("Enter your height in meters: "))
print("Your height is " + str(height) + " meters.")
print (type(height))

# Getting a boolean input from the user
is_student = input("Are you a student? (yes/no): ").lower() == 'yes'
print("Student status: " + str(is_student))
print (type(is_student))

# Getting a list input from the user
favorite_colors = input("Enter your favorite colors, separated by commas: ").split(',')
print("Your favorite colors are: " + str(favorite_colors))
print(type(favorite_colors))

# Getting a tuple input from the user
coordinates = tuple(map(float, input("Enter your coordinates (x, y), separated by a comma: ").split(',')))
print("Your coordinates are: " + str(coordinates))
print(type(coordinates))

# Getting a dictionary input from the user
user_info = {}
user_info['name'] = input("Enter your name: ")
user_info['age'] = int(input("Enter your age: "))
user_info['city'] = input("Enter your city: ")
print("User information: " + str(user_info))
print(type(user_info))