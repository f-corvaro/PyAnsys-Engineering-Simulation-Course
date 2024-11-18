# Learn the use of numpy library
# Create an venv and install numpy library before executing it

import numpy as np

x=np.array([1,2,3,4,5])
print(f"Array: {x}, {type(x)}")
print("---------------------------------------------------")
y=np.arange(1, 21, 3)
print(y, type(y))
print("---------------------------------------------------")
z=np.eye(4, dtype=int)
print(z, type(z))
print("---------------------------------------------------")
w=np.zeros((2,3))
print(w, type(w))
print("---------------------------------------------------")