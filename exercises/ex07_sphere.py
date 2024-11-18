# Write a program that computes the volume of a sphere given its radius.
# The volume of a sphere is given by (4/3)πr^3.
# Ask the user for the radius of the sphere.
# Print the volume of the sphere.
import math

# Ask the user for the radius of the sphere
while True:
	# Check if the input is a number
	try:
		r=float(input("Enter the radius of the sphere, in meter: "))
	# If the input is not a number, print an error message
	except ValueError:
		print("Invalid input. Please enter a number.")
		continue
	if (r>0):
		v=(4/3)*math.pi*r**3
		print(f"The volume of the sphere is {v:.3f} cubic meters")
		break
	elif (r==0):
		print("The volume of the sphere is 0 cubic meters")
		break
	# If the input is a negative number, print an error message
	else:
		print("Invalid input. Please enter a positive number.")
		continue
