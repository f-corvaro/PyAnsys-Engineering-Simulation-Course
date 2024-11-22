# Description: This is the first workshop of the course. 
# The goal is to get familiar with the tools and libraries that we will use during the course.
# Remember to activate the virtual environment before running the script. `source venv/bin/activate`

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import missingno as msno

import matplotlib
# Set the backend for Matplotlib to 'TkAgg' to enable interactive plotting
matplotlib.use('TkAgg')

# Print the current working directory
print("Current working directory: ", os.getcwd())

# Check if the file exists
file_path = './workshop_1/kpis_race.xlsx'
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file {file_path} does not exist.")

# Load the dataset
data = pd.read_excel(file_path)

# Set pandas option to display all columns in the dataframe
pd.set_option('display.max_columns', None)

# In a script, use print(data.head()) to display the output.
# In a Jupyter notebook, use data.head() to display the output.

# Display the first 5 rows of the dataframe
print(data.head())

# Display the first 10 rows of the dataframe
print(data.head(10))

# Display the last 5 rows of the dataframe
print(data.tail())

# Display the dataframe information
print(data.info())

# Print the column names of the dataframe
print(data.columns)

# Print the shape of the dataframe (number of rows and columns)
print(data.shape)

# Visualize the missing data matrix, white lines represent missing values
msno.matrix(data)
# Display the plot
plt.show()
