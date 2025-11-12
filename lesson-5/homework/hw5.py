## 1. Leap Year Function
#solution
print("--- Task 1: Leap Year Function ---")

def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    # This single line implements the leap year logic.
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example Usage:
year_to_check = 2024
print(f"Is {year_to_check} a leap year? {is_leap(year_to_check)}")
year_to_check = 1900
print(f"Is {year_to_check} a leap year? {is_leap(year_to_check)}")
year_to_check = 2000
print(f"Is {year_to_check} a leap year? {is_leap(year_to_check)}")
print("-" * 25)
# 

[Image of leap year logic flowchart]


## 2. Conditional Statements Exercise
#solution
print("--- Task 2: Weird/Not Weird ---")

try:
    n_input = input("Enter a number (1-100): ").strip()
    n = int(n_input)

    # Check the constraint
    if not (1 <= n <= 100):
        print("Error: Number must be between 1 and 100.")
    else:
        # Solution logic
        if n % 2 != 0:
            # n is odd
            print("Weird")
        else:
            # n is even
            if 2 <= n <= 5:
                print("Not Weird")
            elif 6 <= n <= 20:
                print("Weird")
            elif n > 20:
                print("Not Weird")

except ValueError:
    print("Invalid input. Please enter an integer.")
print("-" * 25)
# 

## 3. Even Numbers Between a and b (No Loop)
#solution
print("--- Task 3: Even Numbers (No Loop) ---")

# You can change these values
a = 5
b = 13
print(f"Finding evens between {a} and {b} (inclusive)")
print("")

# --- Solution 1 with if-else statement ---
print("Solution 1 (with if-else):")
start_1 = 0
if a % 2 == 0:
    # 'a' is already even, so start with it
    start_1 = a
else:
    # 'a' is odd, so start with the next number
    start_1 = a + 1
    
# range(start, stop, step) generates numbers without a loop
even_list_1 = list(range(start_1, b + 1, 2))
print(even_list_1)
print("")


# --- Solution 2 without if-else statement ---
print("Solution 2 (without if-else):")

# This math finds the first even number >= a
# If a is even (a%2=0), start = a + 0 = a
# If a is odd (a%2=1),  start = a + 1
start_2 = a + (a % 2)

even_list_2 = list(range(start_2, b + 1, 2))
print(even_list_2)
print("-" * 25)

print("\nAll tasks complete.")
