import datetime
import math
import random
import string

## 1. Age Calculator
print("--- Task 1: Age Calculator ---")
name = input("Enter your name: ")
try:
    birth_year = int(input("Enter your year of birth: "))
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    print(f"Hello {name}, you are {age} years old.")
except ValueError:
    print("Invalid year entered. Please enter a number.")
print("-" * 25)


## 2. Extract Car Names
print("--- Task 2: Extract Car Names (LMaasleitbtui) ---")
txt2 = 'LMaasleitbtui'
car_name_2 = txt2[1::2]
print(f"From '{txt2}', the extracted name is: {car_name_2}")
print("-" * 25)


## 3. Extract Car Names
print("--- Task 3: Extract Car Names (MsaatmiazD) ---")
txt3 = 'MsaatmiazD'
car_name_3 = txt3[0::2]
print(f"From '{txt3}', the extracted name is: {car_name_3}")
print("-" * 25)


## 4. Extract Residence Area
print("--- Task 4: Extract Residence Area ---")
txt4 = "I'am John. I am from London"
try:
    residence = txt4.split('from ')[1]
    print(f"From '{txt4}', the residence is: {residence}")
except IndexError:
    print("Could not find the residence area.")
print("-" * 25)


## 5. Reverse String
print("--- Task 5: Reverse String ---")
user_string_5 = input("Enter a string to reverse: ")
reversed_string_5 = user_string_5[::-1]
print(f"The reversed string is: {reversed_string_5}")
print("-" * 25)


## 6. Count Vowels
print("--- Task 6: Count Vowels ---")
text_6 = input("Enter a string: ")
vowels_6 = "aeiouAEIOU"
count_6 = 0
for char in text_6:
    if char in vowels_6:
        count_6 += 1
print(f"The number of vowels is: {count_6}")
print("-" * 25)


## 7. Find Maximum Value
print("--- Task 7: Find Maximum Value ---")
# Using a predefined list
numbers_7 = [45, 12, 98, 56, 3, 222, 0, 49]
if numbers_7: # Check if the list is not empty
    max_value_7 = max(numbers_7)
    print(f"The list of numbers is: {numbers_7}")
    print(f"The maximum value is: {max_value_7}")
else:
    print("The list is empty.")
print("-" * 25)


## 8. Check Palindrome
print("--- Task 8: Check Palindrome ---")
word_8 = input("Enter a word to check: ")
cleaned_word_8 = word_8.lower().replace(" ", "")
if cleaned_word_8 == cleaned_word_8[::-1]:
    print(f"'{word_8}' is a palindrome.")
else:
    print(f"'{word_8}' is not a palindrome.")
print("-" * 25)


## 9. Extract Email Domain
print("--- Task 9: Extract Email Domain ---")
email_9 = input("Enter your email address: ")
try:
    domain_9 = email_9.split('@')[1]
    print(f"The domain is: {domain_9}")
except IndexError:
    print("Invalid email format.")
print("-" * 25)


## 10. Generate Random Password
print("--- Task 10: Generate Random Password ---")
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    if not characters:
        return "Error: No characters to choose from."
    password = ''.join(random.choice(characters) for i in range(length))
    return password

new_password_10 = generate_password()
print(f"Your random password is: {new_password_10}")
print("-" * 25)

print("\nAll tasks complete.")
