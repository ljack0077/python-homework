import os

# This dictionary contains the filepath (key) and the code content (value)
project_structure = {
    
    # --- Task 2: Custom Modules ---
    "math_operations.py": """
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
""",

    "string_utils.py": """
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
""",

    # --- Task 3: Geometry Package ---
    "geometry/__init__.py": "",
    
    "geometry/circle.py": """
import math

def calculate_area(radius):
    return math.pi * (radius ** 2)

def calculate_circumference(radius):
    return 2 * math.pi * radius
""",

    # --- Task 3: File Operations Package ---
    "file_operations/__init__.py": "",

    "file_operations/file_reader.py": """
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
""",

    "file_operations/file_writer.py": """
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Successfully wrote to {file_path}")
""",

    # --- Main Test File (to prove it works) ---
    "main.py": """
# Import Custom Modules
import math_operations
import string_utils

# Import Custom Packages
from geometry import circle
from file_operations import file_writer, file_reader

def run_tests():
    print("=== HOMEWORK TEST RUNNER ===")
    
    # 1. Test Math
    print("\\n1. Testing Math Operations:")
    print(f"   5 + 3 = {math_operations.add(5, 3)}")
    print(f"   10 / 2 = {math_operations.divide(10, 2)}")

    # 2. Test String Utils
    print("\\n2. Testing String Utils:")
    text = "Hello World"
    print(f"   Original: {text}")
    print(f"   Reversed: {string_utils.reverse_string(text)}")
    print(f"   Vowels: {string_utils.count_vowels(text)}")

    # 3. Test Geometry Package
    print("\\n3. Testing Geometry Package:")
    r = 5
    print(f"   Radius: {r}")
    print(f"   Area: {circle.calculate_area(r):.2f}")
    print(f"   Circumference: {circle.calculate_circumference(r):.2f}")

    # 4. Test File Operations Package
    print("\\n4. Testing File Operations Package:")
    file_name = "test_log.txt"
    file_writer.write_file(file_name, "This is a test file created by Python.")
    content = file_reader.read_file(file_name)
    print(f"   Read content from file: '{content}'")
    
    print("\\nAll tests completed successfully!")

if __name__ == "__main__":
    run_tests()
"""
}

def create_project():
    print("Setting up homework files...")
    
    for file_path, content in project_structure.items():
        # Handle directories (if the path has a slash)
        if "/" in file_path:
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Created directory: {directory}")
        
        # Write the file
        with open(file_path, "w") as f:
            f.write(content.strip())
        print(f"Created file: {file_path}")

    print("\nSUCCESS! All files created.")
    print("Run 'python main.py' to test the homework.")

if __name__ == "__main__":
    create_project()
