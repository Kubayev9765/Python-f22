#1

1.
python -m venv myenv

myenv\Scripts\activate

pip install numpy pandas matplotlib

pip freeze > requirements.txt

pip install -r requirements.txt


#2

my_project/
│
├── math_operations.py
├── string_utils.py
└── main.py  ← (You can test from here)



# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b




# string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)



# main.py

import math_operations as mo
import string_utils as su

# Math operations
print("Add:", mo.add(10, 5))
print("Subtract:", mo.subtract(10, 5))
print("Multiply:", mo.multiply(10, 5))
print("Divide:", mo.divide(10, 0))

# String utilities
print("Reversed:", su.reverse_string("Hello"))
print("Vowel Count:", su.count_vowels("Hello World"))


python main.py

#3

your_project/
│
├── geometry/
│   ├── __init__.py
│   └── circle.py
│
└── main.py  ← (for testing)


# geometry/__init__.py

# Optional: import functions here to make them directly accessible via geometry
from .circle import calculate_area, calculate_circumference



# geometry/circle.py

import math

def calculate_area(radius):
    """Returns the area of a circle given the radius."""
    return math.pi * radius ** 2

def calculate_circumference(radius):
    """Returns the circumference of a circle given the radius."""
    return 2 * math.pi * radius


# main.py

from geometry import calculate_area, calculate_circumference

radius = 5
print(f"Area of circle: {calculate_area(radius):.2f}")
print(f"Circumference of circle: {calculate_circumference(radius):.2f}")



python main.py



----------------------------------------



your_project/
│
├── file_operations/
│   ├── __init__.py
│   ├── file_reader.py
│   └── file_writer.py
│
└── main.py  ← (for testing)


# file_operations/__init__.py

from .file_reader import read_file
from .file_writer import write_file



# file_operations/file_reader.py

def read_file(file_path):
    """Reads and returns the content of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"




# file_operations/file_writer.py

def write_file(file_path, content):
    """Writes the given content to the specified file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            return "Write successful."
    except Exception as e:
        return f"Error: {e}"




# main.py

from file_operations import read_file, write_file

file_path = "sample.txt"
content = "Hello from custom file_operations package!"

# Write to file
print(write_file(file_path, content))

# Read from file
print(read_file(file_path))


python main.py



