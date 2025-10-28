# Variables and Data Types in Python
# This file shows how to declare variables and work with common data types.

# Variables: No need to declare type explicitly (dynamically typed)
name = "Alice"  # String
age = 25        # Integer
height = 5.6    # Float
is_student = True  # Boolean

# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# Data types: Check with type() function
print("Type of name:", type(name))  # <class 'str'>
print("Type of age:", type(age))    # <class 'int'>

# Lists (mutable collections)
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
fruits.append("orange")  # Add to list
print("Updated fruits:", fruits)

# Dictionaries (key-value pairs)
person = {"name": "Bob", "age": 30}
print("Person:", person)
print("Name from dict:", person["name"])