# List, Tuples and Dictionary

# List
e = [1, 2, "pig", 3.14, True]

# Printing the list
print()
print ("List:", e)
print()
print ("List element nb.2:", e[2]) # carefull with the index, it starts at 0
print()
# Changing the value of the list, and printing it
e[2] = "dog" # changing the value of the list
print ("List element nb.2 after changing value:", e[2])
print()
e.append('cat')# adding a new element to the list
print(e)
print()

# Tuples 
f = (1, 2, 'pig', 3.14, True)

# Printing the tuple
print ("Tuple:", f)
print()
print ("Tuple element nb.2:", f[2])
print()
# Try to change the value of f[2], it will raise an error, tuples are immutable

# Dictionary
my_dict = {'name': 'Baldassarre', 'age': 33, 'city': 'Monaco'}

# Printing the dictionary
print ("Dictionary:", my_dict)
print()
print("Dictionary keys:", my_dict.keys())
print()
print("Dictionary values:", my_dict.values())
print()

l=[("HDD", 500), ("RAM", 8), ("CPU", "i7")]
print(type(l))
l=dict(l)
print(type(l))
print()

# Printing the value of the key 'name'
print ("Dictionary key 'name':", my_dict['name'])
print()

# Changing the value of the key 'name'
my_dict['name'] = 'Baldassarre Martini'
print ("Dictionary key 'name' after changing value:", my_dict['name'])
print()

items={'Computer' : 1250.99, 'HD 8TB' : 350.99, 'Mouse' : 99.99}
item=input("Price of which item do you want to know? ")
valore=items[item]
print(f'Price of {item} is {valore:.2f}€')