import sys

print("=== Exception Handling Exercises ===")

## 1. Handle ZeroDivisionError
#solution
print("\n--- Task 1: ZeroDivisionError ---")
def divide_numbers(x, y):
    try:
        result = x / y
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

divide_numbers(10, 0)


## 2. ValueError on Integer Input
#solution
print("\n--- Task 2: ValueError on Input ---")
def get_integer():
    try:
        num = int(input("Enter an integer: "))
        print(f"You entered: {num}")
    except ValueError:
        print("Error: Input is not a valid integer.")
# get_integer() # Uncomment to test interactive input


## 3. FileNotFoundError
#solution
print("\n--- Task 3: FileNotFoundError ---")
try:
    with open("non_existent_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: The file was not found.")


## 4. TypeError for Non-Numerical Inputs
#solution
print("\n--- Task 4: TypeError for Non-Numerical ---")
def check_numbers(a, b):
    try:
        # We manually check and raise TypeError as requested
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Inputs must be numerical.")
        print(f"Sum: {a + b}")
    except TypeError as e:
        print(f"Error: {e}")

check_numbers(5, "hello")


## 5. PermissionError
#solution
print("\n--- Task 5: PermissionError ---")
try:
    # Trying to open a directory as a file usually causes permission/is-a-directory error
    with open("/", "r") as f: 
        print("Opened successfully")
except PermissionError:
    print("Error: You do not have permission to access this file.")
except IsADirectoryError:
     print("Error: Found a directory, expected a file.")


## 6. IndexError
#solution
print("\n--- Task 6: IndexError ---")
my_list = [1, 2, 3]
try:
    print(my_list[10])
except IndexError:
    print("Error: List index out of range.")


## 7. KeyboardInterrupt
#solution
print("\n--- Task 7: KeyboardInterrupt ---")
try:
    # Simulating a prompt. In a real terminal, press Ctrl+C to trigger this.
    val = input("Enter a number (Press Ctrl+C to test interrupt): ")
except KeyboardInterrupt:
    print("\nError: Input cancelled by user.")


## 8. ArithmeticError
#solution
print("\n--- Task 8: ArithmeticError ---")
try:
    x = 10
    y = 0
    # ArithmeticError is the base class for ZeroDivisionError, OverflowError, etc.
    result = x / y
except ArithmeticError:
    print("Error: An arithmetic error occurred.")


## 9. UnicodeDecodeError
#solution
print("\n--- Task 9: UnicodeDecodeError ---")
# To test this, we create a binary file and try to read it as utf-8 text
with open("binary_temp.dat", "wb") as f:
    f.write(b'\x80\x81') # Invalid utf-8 bytes

try:
    with open("binary_temp.dat", "r", encoding="utf-8") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Error: Unable to decode file with specified encoding.")


## 10. AttributeError
#solution
print("\n--- Task 10: AttributeError ---")
try:
    number = 10
    # Integers do not have an 'append' method
    number.append(5)
except AttributeError:
    print("Error: Object does not have that attribute.")


import os
import string
import random

print("=== File I/O Exercises ===")

# SETUP: Create a dummy file for testing
filename = "demo_file.txt"
content = """Line 1: Python is great.
Line 2: File handling is essential.
Line 3: This is a test file.
Line 4: Apple, Banana, Cherry.
Line 5: End of file."""
with open(filename, "w") as f:
    f.write(content)
print(f"[Setup] Created {filename} for testing.\n")


## 1. Read entire text file
#solution
print("--- Task 1: Read Entire File ---")
with open(filename, "r") as f:
    print(f.read())


## 2. Read first n lines
#solution
print("\n--- Task 2: Read First n Lines ---")
def read_first_n_lines(fname, n):
    with open(fname) as f:
        for i in range(n):
            line = f.readline()
            print(line.strip())
read_first_n_lines(filename, 2)


## 3. Append text and display
#solution
print("\n--- Task 3: Append and Display ---")
with open(filename, "a+") as f:
    f.write("\nLine 6: Appended line.")
    f.seek(0) # Move cursor back to start to read
    print(f.read())


## 4. Read last n lines
#solution
print("\n--- Task 4: Read Last n Lines ---")
n = 2
with open(filename, "r") as f:
    lines = f.readlines()
    last_n = lines[-n:]
    for line in last_n:
        print(line.strip())


## 5. Read file line by line into a list
#solution
print("\n--- Task 5: File to List ---")
with open(filename, "r") as f:
    lines_list = f.readlines() # readlines() returns a list automatically
    # OR manual loop: [line.strip() for line in f]
    print(lines_list)


## 6. Read file line by line into a variable
#solution
print("\n--- Task 6: File to Variable ---")
with open(filename, "r") as f:
    file_content_var = f.read()
    print(f"Variable contains {len(file_content_var)} characters.")


## 7. Read file into an array
#solution
print("\n--- Task 7: File to Array ---")
lines_array = []
with open(filename, "r") as f:
    for line in f:
        lines_array.append(line.strip())
print(lines_array)


## 8. Find the longest words
#solution
print("\n--- Task 8: Longest Words ---")
with open(filename, "r") as f:
    text = f.read()
    words = text.split()
    max_len = len(max(words, key=len))
    longest_words = [word for word in words if len(word) == max_len]
    print(longest_words)


## 9. Count number of lines
#solution
print("\n--- Task 9: Count Lines ---")
with open(filename, "r") as f:
    count = len(f.readlines())
    print(f"Total lines: {count}")


## 10. Count frequency of words
#solution
print("\n--- Task 10: Word Frequency ---")
from collections import Counter
with open(filename, "r") as f:
    words = f.read().split()
    print(Counter(words))


## 11. Get file size
#solution
print("\n--- Task 11: File Size ---")
file_size = os.path.getsize(filename)
print(f"File size: {file_size} bytes")


## 12. Write a list to a file
#solution
print("\n--- Task 12: Write List to File ---")
colors = ["Red", "Green", "Blue"]
with open("colors.txt", "w") as f:
    for c in colors:
        f.write(c + "\n")
print("Written colors.txt")


## 13. Copy contents to another file
#solution
print("\n--- Task 13: Copy File ---")
import shutil
shutil.copyfile(filename, "copy_demo.txt")
print("Copied to copy_demo.txt")


## 14. Combine lines from two files
#solution
print("\n--- Task 14: Combine Two Files ---")
with open(filename) as f1, open("colors.txt") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " - " + l2.strip())


## 15. Read random line
#solution
print("\n--- Task 15: Random Line ---")
import random
with open(filename, "r") as f:
    lines = f.readlines()
    print(random.choice(lines).strip())


## 16. Check if file is closed
#solution
print("\n--- Task 16: Is File Closed? ---")
f = open(filename, "r")
print(f"Closed before close(): {f.closed}")
f.close()
print(f"Closed after close(): {f.closed}")


## 17. Remove newline characters
#solution
print("\n--- Task 17: Remove Newlines ---")
with open(filename, "r") as f:
    lines = [line.rstrip() for line in f]
    print(lines)


## 18. Count words (handling commas)
#solution
print("\n--- Task 18: Count Words (Comma separated) ---")
with open(filename, "r") as f:
    text = f.read()
    # Replace comma with space to handle "Apple,Banana"
    text = text.replace(",", " ")
    words = text.split()
    print(f"Total words: {len(words)}")


## 19. Extract chars from files to list
#solution
print("\n--- Task 19: Extract Chars ---")
char_list = []
with open(filename, "r") as f:
    while True:
        char = f.read(1)
        if not char: break
        char_list.append(char)
print(f"Extracted {len(char_list)} characters.")


## 20. Generate 26 Text Files (A.txt ... Z.txt)
#solution
print("\n--- Task 20: Generate A-Z Files ---")
# Created in a separate folder to avoid clutter
if not os.path.exists("alphabet_files"):
    os.makedirs("alphabet_files")

for letter in string.ascii_uppercase:
    with open(f"alphabet_files/{letter}.txt", "w") as f:
        f.write(f"This is file {letter}")
print("Generated A.txt through Z.txt in 'alphabet_files' folder.")


## 21. Alphabet list with n letters per line
#solution
print("\n--- Task 21: Alphabet File ---")
def create_alpha_file(n):
    with open("alphabet_lines.txt", "w") as f:
        alphabet = string.ascii_uppercase
        for i in range(0, len(alphabet), n):
            f.write(alphabet[i:i+n] + "\n")

create_alpha_file(3) # 3 letters per line
with open("alphabet_lines.txt", "r") as f:
    print(f.read())
