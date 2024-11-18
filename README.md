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

I am grateful for the opportunity provided by iESSS to explore both new and established concepts in programming and 
engineering. The Python for Engineers course is designed for individuals looking to enhance their programming skills 
and leverage powerful simulation tools. This course covers the fundamentals of Python programming as well as advanced 
techniques in data management, result visualization, and simulation process automation. With the increasing demand for 
efficient and precise engineering solutions, integrating Python with the Ansys platform offers a robust toolset for 
optimizing simulation processes.

This repository contains the materials and projects I will study and complete throughout this course. I hope this 
work will be useful to others as well.

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

During the course, you will be required to use [Google Colab](https://colab.research.google.com/).

Google Colaboratory, or Colab, is a free, cloud-based Jupyter notebook environment that allows you to write and execute Python code in your browser. To get started with Google Colab, you can create a new notebook, write your code, and execute it directly in the browser. 

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
  
  The **development environment** is the space where you write the instructions that will be executed by the program. You need to import files and libraries for proper operation. To see results, you have to compile the program and analyze it line by line to check the logic and any errors (breakpoints). Essentially, it is a programmer's note sheet where they will write their algorithm in a programming language. An **Integrated Development Environment (IDE)** is software that provides development tools for coding, testing, and debugging programs. There are many IDEs for various programming languages, such as PyCharm, Visual Studio Code, Sublime Text, and IDLE.

  ### Online vs. Offline IDEs

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
  
  A **compiler** is a program that converts source code written in a programming language into executable code that can be read and executed by the computer. “Hello World” is a simple example of a program that is used to test a development environment.

  **Variables** are spaces in computer memory used to store values. 

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
    - Slower execution time since the code is translated on the fly.
    - Less optimization compared to compiled code.

  Python files have the `.py` extension, and you need to have a Python interpreter installed to run them. Unlike C, Python does not compile to `.o` (object) files. Instead, Python code is interpreted at runtime. When you run a Python script, the Python interpreter compiles the code to bytecode, which is then executed by the Python Virtual Machine (PVM). This process is transparent to the user and does not produce .o files.

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

  ### Formatted String Literals (f-strings)

  In Python, formatted string literals, also known as f-strings, provide a way to embed expressions inside string literals using curly braces `{}`. This allows you to include the value of variables directly within a string.

  Example:
  ```python
  a = 10
  print(f"The value of a is {a}")
  ```
  In this example, the `f` before the string indicates that it is an f-string, and `{a}` is replaced with the value of the variable a when the string is printed.

  ### Lists
  A list is an ordered collection of items which can be of different types. Lists are mutable, meaning their elements can be changed.

  Example:
  ```python
  my_list = [1, 2, 3, "apple", 4.5]
  print(my_list[3])  # Output: apple
  ```
  ### Tuples
  A tuple is similar to a list, but it is immutable, meaning its elements cannot be changed after creation.

  Example:
  ```python
  my_tuple = (1, 2, 3, "apple", 4.5)
  print(my_tuple[3])  # Output: apple
  ```

  ### Dictionaries
  A dictionary is an unordered collection of key-value pairs. Each key is unique and is used to access its corresponding value.

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
  Loops in Python allow you to execute a block of code multiple times by iterating over a sequence of values. This concept is used when you need to repeat a specific action for a certain number of times or while a condition is true. Using loops can significantly reduce the amount of code you need to write, thereby reducing the computational cost of the algorithm.

  - `For` Loops: The for loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence. This is useful when you know in advance how many times you need to execute the block of code.
  Example:
  ```python
  for i in range(5):
    print("Iteration:", i)
  ```
  - `While` Loops: The while loop is used to execute a block of code as long as a certain condition is true. The programmer must ensure that the condition eventually becomes false; otherwise, the loop will run indefinitely, resulting in an infinite loop.
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

  </p>
</details>

<details>
  <summary><strong>Basic Exercises in Python</strong></summary>
  <p align="justify">

  `ex00_hello_world.py`:
  The first exercise is to write "Hello, World!" in Python.  To run the program, use the following command in the terminal: `python3 ex00_hello_world.py`. If there are any errors, they will be displayed in the console.

  `ex01_variable_types.py`:
  The second exercise is to declare and use different variable types in Python, including integers, floats, strings, and booleans. This exercise helps you understand how to work with basic data types in Python. 

  `ex02_list_tuples_dictionary.py`:
  The third exercise is to work with lists, tuples, and dictionaries in Python. Lists are ordered collections of items that can be changed, tuples are ordered collections of items that cannot be changed, and dictionaries are collections of key-value pairs. This exercise helps you understand how to use these data structures in Python. 

  `ex03_mathematical_operations.py`:
  The fourth exercise is to perform mathematical operations in Python. Python supports standard mathematical operators such as addition, subtraction, multiplication, division, remainder of division, power, and integer division. This exercise helps you understand how to use these operators in Python. Use the `input` function to allow the user to enter values.
  
  `ex04_input.py`:
  This exercise demonstrates how to use the `input` function in Python to get different types of input from the user. The program covers various types of input, including strings, integers, floats, booleans, lists, tuples, and dictionaries. It prompts the user to enter values and then prints the entered values to demonstrate how to handle different types of input in Python.

  `ex05_conditional_statements.py`:
  This program demonstrates the use of conditional statements in Python. It prompts the user to enter two numbers and then compares them using `if`, `elif`, and `else` statements. Based on the comparison, it prints whether the first number (x) is less than, equal to, or greater than the second number (y).


  `ex06_loops.py`:
  The sixth exercise is to use loops in Python. Python supports for and while loops to iterate over sequences and perform repetitive tasks. This exercise helps you understand how to use loops in Python. 

  `ex07_sphere.py`:
  This script calculates the volume of a sphere based on user input for the radius. It uses a `while` loop to repeatedly prompt the user for a valid radius until a positive number is entered. The script handles invalid inputs gracefully using a `try-except` block to catch `ValueError` exceptions when the user enters non-numeric values.

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