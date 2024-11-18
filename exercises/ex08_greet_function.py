# This program is a first example of the powerful of functions

def	greet(name):
	"""
    Returns a greeting message.

    Parameters:
    name (str): The name to greet.

    Returns:
    str: A greeting message.
    """
	return f"Hello, {name}!"

print(greet(input("Enter your name:")))