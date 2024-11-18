# This exercise is designed to understand how to define and manipulate lists, tuples, and dictionaries in Python.

# List
# List are mutable and can be changed
e = [1, 2, "pig", 3.14, True]

# Printing the list
print ("List is composed by:", e)
print ("List element number 2:", e[2]) # carefull with the index, it starts at 0
# Changing the value of the list, and printing it
e[2] = "dog" # changing the value of the list
print ("List element nb.2 after changing value:", e[2])
# Adding a new element to the list, and printing it
e.append(False)# adding a new element to the list
print(e)
print()


# Tuples 
# Tuples are immutable and cannot be changed. If you try to change value to one of the elements, it will raise an error.
f = (1, 2, 'pig', 3.14, True)

# Printing the tuple
print ("Tuple:", f)
print ("Tuple element nb.2:", f[2])
print()

# Dictionary
# Dictionaries are mutable and can be changed
my_dict = {'name': 'Baldassarre', 'age': 33, 'city': 'Monaco'}

# Printing the value of the key 'name'
print ("Dictionary key 'name':", my_dict['name'])

# Changing the value of the key 'name'
my_dict['name'] = 'Baldassarre Martini'
print ("Dictionary key 'name' after changing value:", my_dict['name'])

# Printing the dictionary
print ("Dictionary is composed by:", my_dict)
print("Dictionary keys are:", my_dict.keys())
print("Dictionary values are:", my_dict.values())
print()

# How to trasform a list of tuples into a dictionary
l=[("HDD", 500), ("RAM", 8), ("CPU", "i7")]
print(f"List of tuple: {l},", type(l))
l=dict(l)
print(f"After conversion in dictionary: {l},", type(l))
print()

# Example of use of dictionary
items={'Computer' : 1250.99, 'Keyboard' : 350.99, 'Mouse' : 99.99}
item=input("Price of which item do you want to know? ")
valore=items[item]
print(f'Price of {item} is {valore:.2f}€')