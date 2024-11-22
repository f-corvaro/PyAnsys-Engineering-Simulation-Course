<h1 align="center"><a href="https://github.com/f-corvaro/PyAnsys-Engineering-Simulation-Course">
	<img src="https://github.com/f-corvaro/PyAnsys-Engineering-Simulation-Course/blob/main/.extra/python-eng.png" alt="Python_and_pyansys">
</a></h1>

<p align="center">
	<b><i>"Optimize engineering processes with Python and PyAnsys."</i></b><br>
</p>
<p align="center" style="text-decoration: none;">
	<a href="https://it.esssvirtual.com/courses/corso-di-python-e-pyansys-per-ingegneri"><img alt="course" src="https://img.shields.io/badge/course-iESSS-yellow" /></a>
    <a href="https://github.com/f-corvaro/PyAnsys-Engineering-Simulation-Course"><img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/f-corvaro/PyAnsys-Engineering-Simulation-Course?color=blueviolet" /></a>
    <a href="https://github.com/f-corvaro/PyAnsys-Engineering-Simulation-Course"><img alt="Code language count" src="https://img.shields.io/github/languages/count/f-corvaro/PyAnsys-Engineering-Simulation-Course?color=yellow" /></a>
    <a href="https://github.com/f-corvaro/PyAnsys-Engineering-Simulation-Course"><img alt="GitHub top language" src="https://img.shields.io/github/languages/top/f-corvaro/PyAnsys-Engineering-Simulation-Course?color=blueviolet" /></a>
    <a href="https://github.com/f-corvaro/PyAnsys-Engineering-Simulation-Course"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/f-corvaro/PyAnsys-Engineering-Simulation-Course?color=yellow" /></a>
</p>

<h2 align="center">Python and PyAnsys Engineering Simulation Course</h2>

<h3 align="center">Index</h3>
<p align="center">

</p>
<br>

# Status: Coming Soon

Thank you for your interest! I am currently working hard to bring you exciting updates. Stay tuned for more information coming soon!

## Introduction

<p align="justify">

I am grateful for the opportunity provided by iESSS to explore engineering concepts studied during my university courses in 
conjunction with programming concepts, allowing me to understand the connection between these two fields. The Python for Engineers 
course is designed for individuals looking to enhance their programming skills 
and leverage powerful simulation tools. This course covers the fundamentals of Python programming as well as advanced 
techniques in data management, result visualization, and simulation process automation. With the increasing demand for 
efficient and precise engineering solutions, integrating Python with the Ansys platform offers a robust toolset for 
optimizing simulation processes.

This repository contains all the theory and code I developed during this course, including additional code created for fun and to explore 
new or old concepts. I hope this work will be useful to others as well.

</p>
<br>

### Overview 

<p align="justify">

In this course, students will learn how to use the Python language and apply it to simulation techniques in engineering projects. 
The course covers a wide range of topics, including:

- Introduction to Python.
- Algorithms.
- Development environments.
- Code compilation.
- Variables and mathematical operators.
- Conditional commands and structured programming.
- Functions and modular programming.
- Data science and exploratory analysis.
- Data manipulation and visualization.
- Introduction to computer simulation.
- Fluid dynamics analysis (CFD), structural analysis (FEA), and electromagnetic analysis (EMAG).
- Automation of simulation processes with Python.
- Python scripting for Ansys Discovery, PyMAPDL, PyFluent, and PyAEDT.

</p>
<br>

### Useful Tools

<p align="justify">

To complete the proposed exercises, it is recommended to use the free educational license of the Ansys package 
(Ansys Student). It can be downloaded and installed at any time directly from the Ansys website: [Ansys Student](https://www.ansys.com/academic/students).

During the course, you will be required to use [Google Colab](https://colab.research.google.com/). Google Colaboratory, or Colab, is a free, 
cloud-based Jupyter notebook environment that allows you to write and execute Python code in your browser. 

The course requires the use of several Python libraries. Below is a list of these libraries along with their descriptions and links to their 
respective pages:

- [numpy](https://numpy.org/): NumPy is an open-source library for numerical computing in Python. It provides support for arrays, matrices, 
  and many mathematical functions to operate on these data structures. [GitHub page](https://github.com/numpy/numpy?tab=readme-ov-file).
- [pandas](https://pandas.pydata.org/): Pandas is an open-source data manipulation and analysis library. It offers data structures like 
  DataFrames and Series, which are essential for handling structured data. [GitHub page](https://github.com/pandas-dev/pandas).
- [matplotlib](https://matplotlib.org/): Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations 
  in Python. It is widely used for plotting graphs and charts. [GitHub page](https://github.com/matplotlib/matplotlib).
- [seaborn](https://seaborn.pydata.org/): Seaborn is a statistical data visualization library based on Matplotlib. It provides a high-level 
  interface for drawing attractive and informative statistical graphics. [GitHub page](https://github.com/mwaskom/seaborn).

The use of these libraries will be explained in the theory section of this README.

</p>
<br>

## Folder Structure

<p align="justify">

```
```

<p>

## Theorical Knowledge

<details>
  <summary><strong>Basic Concept of Programming</strong></summary>
  <p align="justify">
  
  A **programming language** is a set of rules used to write programs that can be executed by a computer. High-level languages, such as Python, are written by programmers and then compiled or interpreted into low-level machine code that can be executed by the computer's microprocessor. 

  An **algorithm** is a finite sequence of well-defined instructions used to solve a specific problem. In computer science, algorithms are implemented using programming languages and must be designed to achieve a particular goal. Effective problem-solving involves breaking down complex problems into smaller, manageable parts and solving them step by step. Clear and unambiguous communication is essential for writing efficient and maintainable code.

  A **compiler** is a program that converts source code written in a programming language into executable code that can be read and executed by the computer. “Hello World” is a simple example of a program that is used to test a development environment.

  **Variables** are spaces in computer memory used to store values. 

  The **development environment** is the space where you write the instructions that will be executed by the program. You need to import files and libraries for proper operation. To see results, you have to compile the program and analyze it line by line to check the logic and any errors (breakpoints). Essentially, it is a programmer's note sheet where they will write their algorithm in a programming language. 

  An **Integrated Development Environment (IDE)** is software that provides development tools for coding, testing, and debugging programs. There are many IDEs for various programming languages, such as PyCharm, Visual Studio Code, Sublime Text, and IDLE.

  **Offline IDEs**:
  - **PyCharm**: A powerful IDE for Python with features like code completion, debugging, and version control integration.
  - **Visual Studio Code**: A lightweight but powerful source code editor with support for Python and many other languages, extensions, and debugging tools. (My favorite one).
  - **Sublime Text**: A sophisticated text editor for code, markup, and prose with a focus on speed and simplicity.
  - **IDLE**: The default Python IDE that comes with the Python installation, suitable for beginners.

  **Online IDEs**:
  - **Google Colaboratory**: An interactive way of sharing documents with code, graphs, results, text, and other features. It allows the execution of a block of code, and codes can be edited and executed at any time. It is particularly useful for data science and machine learning projects as it provides free access to GPU and TPU resources. *(This IDE will be used for the course)*.
  
  ### Differences between Online and Offline IDEs

  **Offline IDEs**:
  - **Pros**:
    - Full control over the development environment and tools.
    - Better performance and responsiveness.
    - Access to local files and resources.
    - More customization options and extensions.
  - **Cons**:
    - Requires installation and setup on your local machine.
    - Limited to the resources available on your local machine.

  **Online IDEs**:
  - **Pros**:
    - Accessible from any device with an internet connection.
    - No installation or setup required.
    - Easy collaboration and sharing of code.
    - Access to powerful cloud resources (e.g., GPUs in Google Colab).
  - **Cons**:
    - Dependent on internet connectivity.
    - Potentially slower performance compared to local IDEs.
    - Limited access to local files and resources.

  </p>
</details>

<details>
  <summary><strong>Introduction to Python</strong></summary>
  <p align="justify">

  **Python** is a high-level, interpreted programming language developed by Guido van Rossum and first released in 1991. 
  Known for its readability and simplicity, Python has become one of the most popular programming languages in the world. 
  It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python's 
  extensive standard library and active community contribute to its versatility and widespread use in various fields such 
  as web development, data science, artificial intelligence, and scientific computing.

  In Python, an **interpreter** is used instead of a compiler. An interpreter executes the code line by line, translating it into machine code at runtime. This is different from a compiler, which translates the entire source code into machine code before execution.

  ### High-Level and Low-Level Languages

  Machine language consists of binary code (0s and 1s) that is directly executed by a computer's CPU. Assembly language is more readable than machine language and uses mnemonic codes to represent machine-level instructions. High-level languages, such as Python, are closer to human languages and abstract away the complexities of the hardware, making them easier to read, write, and maintain.

  ### Compilers vs. Interpreters

  **Compiler:**
  - **Definition:** A compiler is a program that converts source code written in a programming language into executable code that can be read and executed by the computer.
  - **Pros:**
    - Faster execution time since the code is already translated into machine code.
    - Better optimization of the code during the compilation process.
  - **Cons:**
    - Compilation can be time-consuming, especially for large programs.
    - Debugging can be more difficult since errors are reported after the entire code is compiled.

  **Interpreter:**
  - **Definition:** An interpreter translates and executes code line by line at runtime.
  - **Pros:**
    - Easier to debug since errors are reported immediately after the line is executed.
    - No need for a separate compilation step, making development faster and more interactive.
  - **Cons:**
    - Slower execution time due to on-the-fly code translation.
    - Less optimization compared to compiled code.

  Python files have the `.py` extension, and you need to have a Python interpreter installed to run them. Unlike C, Python does not compile to `.o` (object) files. Instead, Python code is interpreted at runtime. When you run a Python script, the Python interpreter compiles the code to bytecode, which is then executed by the Python Virtual Machine (PVM). This process is transparent to the user and does not produce `.o` files.

  ### Comments
  In Python, comments are written with the `#` symbol. Comments are used to explain the code and make it more readable for humans. The computer ignores comments during execution.
  
  Example:
  ```python
  # This is a single-line comment
  print("Hello, World!")  # This comment explains the print statement
  ```

  ### Variables Types

  Python has several types of variables, including integers (`int`), floating-point numbers (`float`), sequences of characters (`string`), booleans (`bool`), lists (`list`), tuples (`tuple`), and dictionaries (`dict`). These variables can be used in a program to store values and perform calculations.

  - **Integers (`int`)**: Whole numbers, e.g., `5`, `-3`.
  - **Floating-point numbers (`float`)**: Numbers with a decimal point, e.g., `3.14`, `-0.001`.
  - **Strings (`str`)**: Sequences of characters, e.g., `"Hello, World!"`.
  - **Booleans (`bool`)**: Logical values, `True` or `False`.

  **Formatted String Literals (f-strings)**: In Python, formatted string literals, also known as f-strings, provide a way to embed expressions 
  inside string literals using curly braces `{}`. This allows you to include the value of variables directly within a string.

  Example:
  ```python
  a = 10
  print(f"The value of a is {a}")
  ```
  In this example, the `f` before the string indicates that it is an f-string, and `{a}` is replaced with the value of the variable 
  a when the string is printed.

  **Lists:** A list is an ordered collection of items which can be of different types. Lists are mutable, meaning their elements 
  can be changed.

  Example:
  ```python
  my_list = [1, 2, 3, "apple", 4.5]
  print(my_list[3])  # Output: apple
  ```
  **Tuples:** A tuple is similar to a list, but it is immutable, meaning its elements cannot be changed after creation.

  Example:
  ```python
  my_tuple = (1, 2, 3, "apple", 4.5)
  print(my_tuple[3])  # Output: apple
  ```

  **Dictionaries:** A dictionary is an unordered collection of key-value pairs. Each key is unique and is used to access its 
  corresponding value.

  Example:
  ```python
  my_dict = {"name": "Alice", "age": 25, "city": "New York"}
  print(my_dict["name"])  # Output: Alice
  ```

  ### Mathematical Operators

  Python has standard mathematical operators: addition `+`, subtraction `-`, multiplication `*`, division `/`, remainder of division `%`, power `**`, and integer division `//`. Python performs operations in a specific order of priority: parentheses, powers, multiplication, division, addition, and subtraction.

  ### Conditional Statements
  Conditional statements in Python allow you to execute code based on a condition. The most common structures are `if`, `else`, and `elif`. The `if` statement allows you to execute a block of code only if a certain condition is met. The `else` statement allows you to execute alternative code if the condition is not met. The `elif` statement, short for "else if," allows you to check multiple conditions sequentially.

  Conditional statements in Python rely on comparison operators, which allow you to compare values and variables. Some examples of comparison operators are:
  - `==` (equality)
  - `!=` (inequality)
  - `<` (less than)
  - `>` (greater than)
  - `<=` (less than or equal to)
  - `>=` (greater than or equal to)

  The code that should be executed if a certain condition is met must be indented.

  ### Loops
  Loops in Python allow you to execute a block of code multiple times by iterating over a sequence of values. 
  This concept is used when you need to repeat a specific action for a certain number of times or while a condition is `true`. 
  Using loops can significantly reduce the amount of code you need to write, thereby reducing the computational cost of the algorithm.

  - `For` Loops: The for loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence. This is useful when you know in advance how many times you need to execute the block of code.
  Example:
  ```python
  for i in range(5):
    print("Iteration:", i)
  ```
  - `While` Loops: The while loop is used to execute a block of code as long as a certain condition is `true`. 
  The programmer must ensure that the condition eventually becomes `false`; otherwise, the loop will run indefinitely, resulting in an infinite loop.
  Example:
  ```python
  count = 0
  while count < 5:
    print("Count:", count)
    count += 1  # Update the variable to avoid an infinite loop
  ```

  ### Logical Operators

  <img src="https://github.com/f-corvaro/PyAnsys-Engineering-Simulation-Course/blob/main/.extra/logical.png" alt="Logical Operators">

  Logical operators in Python are used to combine conditional statements. They include `and`, `or`, `not`, `nand`, and `nor`. The `and` operator returns `True` if both operands are true, while the `or` operator returns `True` if at least one operand is true. The `not` operator inverts the truth value of the operand. The `nand` operator returns `True` if at least one operand is false (it is the negation of `and`). The `nor` operator returns `True` if both operands are false (it is the negation of `or`). These operators are essential for constructing complex logical expressions and controlling the flow of a program.

  Examples:
  ```python
  x = True
  y = False

  # and operator
  print(x and y)  # Output: False

  # or operator
  print(x or y)  # Output: True

  # not operator
  print(not x)  # Output: False

  # nand operator (negation of and)
  print(not (x and y))  # Output: True

  # nor operator (negation of or)
  print(not (x or y))  # Output: False
  ```

  ### Try/Except

  The `try/except` block in Python is used for handling exceptions and errors that may occur during the execution of a program. 
  By wrapping code that might raise an exception within a `try` block, you can catch and handle specific exceptions using one or more 
  `except` blocks. This prevents the program from crashing and allows you to provide meaningful error messages or alternative actions. 
  For example, you can handle file I/O errors, divide-by-zero errors, or any other runtime errors gracefully. Additionally, you can use 
  the `else` block to execute code if no exceptions were raised and the `finally` block to execute code that should run regardless of 
  whether an exception occurred or not, such as closing a file or releasing resources.

  </p>
</details>

<details>
  <summary><strong>Advanced Python Concepts</strong></summary>
  <p align="justify">

  ### Functions

  Functions are blocks of code that perform a specific task and can be called at various points in your code. They are useful for encapsulating logic and avoiding repetition. The code inside a function must be indented, and functions are defined using the `def` keyword. The advantage of using functions is that if you need to make changes to the code, you only need to do it once in the function body, rather than every time the function is called. You define a function with `def function_name(parameter_1, parameter_2, ..., parameter_n):`. A function can have one or more parameters, or none at all. Functions are essential for modular programming, allowing you to reuse code by creating libraries, thus avoiding the need to redefine functions repeatedly.

  Functions can also return values using the `return` statement, which allows you to capture the output of the function and use it elsewhere in your code. Additionally, functions can have default parameters, which provide default values if no arguments are passed.

  Example:
  ```python
  def greet(name):
      return f"Hello, {name}!"

  print(greet("Alice"))  # Output: Hello, Alice!
  ```

  In this example, the greet function takes a single parameter name and returns a greeting message. Functions help in organizing code, making it more readable and maintainable. They also facilitate debugging and testing by isolating specific tasks within the code. 

  It's also a good practice to include a **docstring** at the beginning of a function to describe its purpose, parameters, and return values. This helps in documenting the code and making it easier to understand for others.

  Example:
  ```python
  def greet(name="World"):
    """
    Returns a greeting message.

    Parameters:
    name (str): The name to greet. Default is "World".

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"
  ```


  ### Libraries

  Python libraries are collections of modules that provide additional functionality to your code. For example, the `math` library offers 
  advanced mathematical functions, while the `numpy` library provides tools for working with matrices and arrays. Once you import a library, 
  you can access its functions and features. Other examples of popular libraries include `warnings` for managing warning messages, 
  `pandas` for data manipulation and analysis, `matplotlib.pyplot` for data visualization, and `seaborn` for statistical data visualization. 
  When importing these libraries, it is common to use **aliases** to simplify their usage in the code. For instance, `import numpy as np`, `import pandas as pd`, `import matplotlib.pyplot as plt`, and `import seaborn as sns`. These aliases make the code more concise and readable.
  Other popular libraries include `requests` for making HTTP requests, `scikit-learn` for machine learning, and `tensorflow` for deep learning. 
  Libraries greatly enhance the capabilities of Python and allow you to perform complex tasks with minimal code.

  To use a library, you often need to install it first using a package manager like `pip3`. For example, you can install `numpy` by running `pip3 install numpy` in your terminal. 

  It's important to keep your libraries up to date to benefit from the latest features and security updates. You can check if a library is up to date and update it using `pip3`. 
  For example, to check for updates and update `numpy`, you can run:
  ```sh
  pip3 install --upgrade numpy
  ```

  For more information about a library, including usage examples and detailed documentation, you should refer to the official documentation. Official documentation is usually available on the library's website or its repository on platforms like GitHub. This is the best source for accurate and comprehensive information about the library's features and usage.

  To manage your project dependencies effectively, it is recommended to use a **virtual environment (venv)**. A virtual environment is an isolated environment that allows you to manage dependencies for your Python projects separately. Here are the steps to create and use a virtual environment:

  1. Create a Virtual Environment:
    ```sh
    python3 -m venv venv
    ```
  2. Activate the venv:
    Linux: 
      ```sh
      source venv/bin/activate
      ```
    Windows: 
      ```sh
      .\venv\Scripts\activate
      ```
  3. Install Packages In The venv:
    ```sh
    pip3 install numpy
    ```
  4. **Deactivate the Virtual Environment** when you have finished working:
   ```sh
   deactivate
   ```

  **In my virtual environment (VENV), I have already installed all the required libraries for the course.**
 
  ### Object-Oriented Programming (OOP)

  Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which combine data and related functionality into a single structure. A class is a general definition of an object, while an object is a specific instance of a class. For example, a `Car` class might define the common characteristics of all cars (model, year, make, and value), whereas `my_car` would be a specific instance of that class. 

  Example:
```python
class Car:
    def __init__(self, model, year, make, value):
        self.model = model
        self.year = year
        self.make = make
        self.value = value

    def description(self):
        return f"{self.year} {self.make} {self.model} valued at {self.value}"
```

  The `self` keyword is used in class methods to refer to the instance of the class. 
  The `__init__` method in Python is a special method that is called when an **instance** (object) of a class is created. 
  It is known as the **constructor method**. The purpose of the `__init__` method is to initialize the object's attributes with the values provided when the object is instantiated. An istance for this example could be:

  ```python
  # Creating an instance of the Car class
  my_car = Car("Corolla", 2020, "Toyota", 20000)
  print(my_car.description())  # Output: 2020 Toyota Corolla valued at 20000
  ```

  Another example of a class is Person, where we have attributes like name and age, and a method called introduce that prints a message with the person's name and age. Finally, we create an object of the Person class called `person1` with specific name and age values.

  Example:
  ```python
  class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

  person1 = Person("Alex", 30)
  print(person1.introduce())  # Output: My name is Alex and I am 30 years old.
  ```

  The advantages of this type of programming include modularity, code reuse, and easier maintenance. By encapsulating data and functionality within objects, OOP allows for more organized and manageable code, making it easier to develop and maintain complex software systems.
 
  </p>
</details>

<details>
  <summary><strong>Exercises in Python</strong></summary>
  <p align="justify">

  In the `./exercises/` folder, you will find numerous exercises and examples that illustrate the theoretical concepts discussed.

  </p>
</details>

<details>
  <summary><strong>Data Science</strong></summary>
  <p align="justify">

  **Data science** is a means to solve problems and find solutions. The process analysis involves:
  - Identifying the problem that needs to be solved.
  - Defining the goal of the solution.
  - Determining where to obtain the necessary data for analysis.
  - Collecting the required data.
  
  After this initial analysis, action must be taken. Over time, companies have evolved from: "I do it this way because it's always been done this way" to "I collect data but don't use it" to "I analyze this data" to "I collect, store data efficiently, and analyze it to implement a strategy" (now AI is also used to analyze processes).
  
  The process flow diagram of a data science project involves an iterative flow, which may require multiple cycles to refine a strategy. Therefore, the steps include defining the problem, finding a way to collect and process data (requiring a format to analyze large amounts of data), analyzing it from an exploratory and bivariate perspective, verifying that the initial hypotheses are correct, conducting a critical analysis, and making a decision. 
  
  **Exploratory Data Analysis (EDA)** is the first crucial phase in analyzing a dataset. The goal is to gain a general understanding of the data, identify patterns, anomalies, and key characteristics that could influence subsequent analyses. EDA is performed using:
  - ***Visualization:*** Graphs and charts are used to visualize the distribution of variables, relationships between them, and to identify any outliers.
  - ***Descriptive statistics:*** Means, standard deviations and other statistics are calculated to describe the main characteristics of the dataset.
  - ***Identification of missing values:*** Missing values are identified and decisions are made on how to handle them (removal, imputation, etc.).
  - ***Data quality check:*** Errors or inconsistencies in the data are verified.

  **Bivariate analysis**, on the other hand, is a specific type of exploratory analysis that focuses on studying the relationship between two variables. The goal is to understand if there is a connection between these two variables and, if so, what type it is (linear, non-linear, positive, negative).

  ### Difference Between Data-Driven and Data Science

  Data-driven refers to a decision-making process that relies heavily on data analysis and interpretation. In a data-driven approach, decisions are made based on data insights rather than intuition or personal experience. This approach ensures that strategies and actions are backed by empirical evidence, leading to more accurate and effective outcomes.

  Data science, on the other hand, is a multidisciplinary field that involves extracting knowledge and insights from structured and unstructured data using scientific methods, processes, algorithms, and systems. It encompasses various techniques such as machine learning, statistical analysis, and data mining to analyze and interpret complex data sets. Data science aims to uncover patterns, make predictions, and provide actionable insights to solve real-world problems.

  In summary, while data-driven focuses on making decisions based on data, data science provides the tools and methodologies to analyze and interpret the data that informs those decisions.

  ###  Data Types

  Nowadays, any interaction with technology or machines generates data, such as mouse positions, clicks, and images. Data can be generated by people through surveys (representing the responses provided) or by machines (data generated by systems and devices). Data can also be categorized as public (freely available and non-profit) or private (requiring authorization and often paid). 

  The nature of the data can vary widely:
  - **Structured Data**: Organized in a predefined manner, often in tabular format (e.g., databases, spreadsheets).
  - **Unstructured Data**: Lacks a specific format or structure (e.g., text documents, images, videos).
  - **Semi-structured Data**: Contains elements of both structured and unstructured data (e.g., JSON, XML).

  Examples of private data include medical records, financial information, and personal identifiers, which require strict handling and protection due to privacy concerns.

### Data Collection

  Data collection can be either manual or automatic. Manual data collection involves methods such as paper surveys, which require subsequent digitization. Automatic data collection utilizes sensors and devices for measurement, including video data from security cameras.

  There are various techniques for extracting data from websites, such as web scraping, which involves gathering data from social networks, e-commerce sites, and news websites.

  Another method of data collection is through APIs (Application Programming Interfaces). APIs provide a set of protocols and tools that allow different applications and systems to communicate and share data. This method enables developers to access and extract data from other applications and systems efficiently.

  In some cases, geographic information can also be crucial, requiring the collection of location-based data through GPS devices or geographic information systems (GIS).

  ### Ensuring Data Quality

  Having a large amount of data is beneficial, but to use it effectively in the data science process, we must ensure its reliability and quality. Key questions to consider include:
  - Are the sensors positioned correctly?
  - Have the sensors been calibrated?
  - Is the external data source reliable?
  - Do the data have any biases?
  - Is the sampling frequency adequate?

  To address the issue of sampling frequency, we can refer to the **Nyquist Theorem**. 
  
  ***The theorem states that the sampling frequency must be at least twice the highest frequency component present in the measured signal to accurately reconstruct the original signal.*** For example, if the highest frequency in the signal is 1 kHz, the sampling frequency should be at least 2 kHz.

  Additionally, data quality can be assessed through:
  - **Data Completeness**: Ensuring that all necessary data points are collected and no critical information is missing.
  - **Data Consistency**: Verifying that data is consistent across different sources and systems.
  - **Data Accuracy**: Ensuring that the data correctly represents the real-world values it is supposed to measure.
  - **Data Timeliness**: Ensuring that the data is up-to-date and relevant to the current analysis.

  By addressing these aspects, we can ensure that the collected data is of high quality and suitable for accurate and reliable analysis in data science projects. High-quality data leads to more reliable insights, better decision-making, and more effective outcomes.

  ### Understanding Bias and Correlation

  Bias in data can be caused by selective sampling, sampling issues, prejudices, or algorithms programmed with errors. It is crucial to identify and mitigate bias to ensure the accuracy and fairness of data analysis.

  Correlation occurs when the variations over time of two variables resemble each other. However, it is important to distinguish between correlation and causation. Correlation implies a relationship between two variables, but it does not necessarily mean that one variable causes the other. 

  Spurious correlation occurs when two variables appear to have a significant relationship, but in reality, there is no causal connection between them. This can lead to incorrect conclusions if not properly identified.

  Statistical analysis is used to help identify relationships between variables and determine whether they are causal or merely correlated. However, statistics alone cannot prove causality. To establish causation, additional methods such as controlled experiments, longitudinal studies, or domain-specific knowledge are required.

  </p>
</details>

<details>
  <summary><strong>Dataframe and Exploratory Data Analysis</strong></summary>
  <p align="justify">

  A **dataframe** is a tabular data structure composed of rows and columns. 
  Each column has a header, and each row has an index. It can be compared to a matrix, with the difference that 
  the first row contains headers and the first column contains indices. In Python, the pandas library provides structures 
  for data manipulation, including the dataframe. A dataframe in pandas can be created from various data sources, 
  such as lists, dictionaries, CSV files, and Excel files. During the creation of a dataframe, it is possible to specify 
  the column names and data types for each column. Additionally, pandas offers many functions for data manipulation within 
  a dataframe, such as filtering, selection, sorting, and aggregation. Dataframes can be combined using `concat()` or 
  merged using `merge()`.

  Beyond data manipulation, pandas also provides functions for data visualization, such as line plots, scatter plots, 
  and bar charts (functions based on the `matplotlib` library). Visualizations are essential for data analysis. 
  The `read_excel()` function in pandas allows reading data from an Excel file. You can specify the file path, 
  the sheet name, and other configuration options for reading the file. Once the file is loaded into a dataframe, 
  you can use pandas functions to manipulate and analyze the data. Additionally, you can export dataframe data to an Excel 
  file using `to_excel()`, with various configuration options available.

  ### Basic Operations - Exploratory Data Analysis

  To understand a dataframe, it is important to first visualize it in its entirety. Pandas provides functions such as:
  - `head()` to view the first 5 rows of the dataframe (or a specified number of rows).
  - `tail()` to view the last 5 rows of the dataframe (or a specified number of rows).
  - `sample()` to view random samples from the dataframe.
  - `describe()` to obtain basic statistics of the dataframe (count, mean, standard deviation, min, and max for each numeric column).
  - `info()` to get information about the dataframe (number of rows and columns, data types, and presence of null values).

  Exploratory Data Analysis (EDA) is a crucial step in the data analysis process. It involves summarizing the main characteristics 
  of the data, often using visual methods. EDA helps in understanding the data distribution, identifying patterns, spotting anomalies, 
  and checking assumptions. It is an iterative process that includes data cleaning, transformation, and visualization. By performing EDA, 
  analysts can make informed decisions about the next steps in their analysis or modeling process.

  ### Additional Useful Functions for Dataframes

  - `isnull()` and `notnull()` to detect missing values.
  - `fillna()` to fill missing values with a specified value.
  - `dropna()` to remove missing values.
  - `pivot_table()` to create a spreadsheet-style pivot table as a dataframe.
  - `groupby()` to group data and perform aggregate operations.
  - `apply()` to apply a function along an axis of the dataframe.
  - `astype()` to cast a pandas object to a specified data type.

  These functions and methods make pandas a powerful tool for data analysis and manipulation, enabling analysts to efficiently 
  handle and explore large datasets.

  ### Types of Variables

  In the context of dataframes, variables are the columns that hold data. 
  Each column in a dataframe represents a variable, and each row represents an observation 
  or record. Variables in dataframes can be classified into several types:

  - Numerical Variables: 
    
    - Discrete Variables: These are countable and have distinct values. Examples include the number of students in a class, the number of cars in a parking lot, or the number of books on a shelf.
    
    - Continuous Variables: These can take any value within a range and are often measured. Examples include height, weight, temperature, and time.
  
  - Time Series Variables: These variables represent data points collected or recorded at specific time intervals. They are used to analyze trends, patterns, and seasonal effects over time. Examples include daily stock prices, monthly sales figures, and annual rainfall measurements.

  - Categorical Variables:
    
    - Nominal Variables: These represent categories with no inherent order. Examples include types of fruits (apple, banana, orange), colors (red, blue, green), and gender (male, female).
    
    - Ordinal Variables: These represent categories with a natural order. Examples include education levels (high school, bachelor's, master's, PhD), customer satisfaction ratings (poor, fair, good, excellent), and class ranks (freshman, sophomore, junior, senior).

  These variables are used in Dataframes for:
  - Data Manipulation: Variables can be manipulated using various pandas functions such as filtering, selection, sorting, and aggregation.
  - Data Analysis: Variables are analyzed to extract meaningful insights. This includes calculating statistics, identifying patterns, and detecting anomalies.
  - Data Visualization: Variables are visualized using plots and charts to better understand the data distribution and relationships between variables.
  - Data Cleaning: Variables are cleaned to handle missing values, correct data types, and remove inconsistencies.
  
  Understanding the types of variables in a dataframe is crucial for selecting appropriate statistical methods and accurately interpreting data in various analyses.

  </p>
</details>

## Developed Skills

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python" alt="Python" />
    <a href="https://www.ansys.com/"><img src="https://github.com/f-corvaro/PyAnsys-Engineering-Simulation-Course/blob/main/.extra/ANSYS_logo.png" alt="Ansys" height="48" />
    <a href="https://colab.google/"><img src="https://github.com/f-corvaro/PyAnsys-Engineering-Simulation-Course/blob/main/.extra/gcolaboratory_logo.png" alt="Google Colaboratory" height="48" />
  </a>
</p><br>

## References

## References

- [Python Official Documentation](https://docs.python.org/3/)
- [Ansys Student](https://www.ansys.com/academic/students)


## Support and Contributions

<p align="center">
If you find this repository helpful, please consider starring it to show your support. Your support is greatly appreciated!</p>

<p align="center">
<a href="https://ko-fi.com/fcorvaro"><img width="180" img align="center" src="https://github.com/f-corvaro/42.common_core/blob/main/.extra/support-me-ko-fi.svg"><alt=""></a>
<a href="https://github.com/sponsors/f-corvaro"><img width="180" img align="center" src="https://github.com/f-corvaro/42.common_core/blob/main/.extra/support-me-github.svg"><alt=""></a>

<br>

## Author

<p align="center"><a href="https://profile.intra.42.fr/users/fcorvaro"><img style="height:auto;" src="https://avatars.githubusercontent.com/u/102758065?v=4" width="100" height="100"alt=""></a>
<p align="center">
<a href="mailto:fcorvaro@student.42roma.it"><kbd>Email</kbd><alt=""></a>
<a href="https://github.com/f-corvaro"><kbd>Github</kbd><alt=""></a>
<a href="https://www.linkedin.com/in/f-corvaro/"><kbd>Linkedin</kbd><alt=""></a>
<a href="https://42born2code.slack.com/team/U050L8XAFLK"><kbd>Slack</kbd><alt=""></a>

<hr/>