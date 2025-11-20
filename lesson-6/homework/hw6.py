# ==========================================
# Task 1: Modify String with Underscores
# ==========================================
# Answer
print("--- Task 1: Modify String ---")

def solve_underscore(txt):
    vowels = "aeiouAEIOU"
    result = ""
    count = 0
    
    for char in txt:
        result += char
        count += 1
        
        # Check if we reached the 3rd character
        if count >= 3:
            # If it's a vowel, we do NOT put underscore yet, 
            # we just continue counting (shifting the spot)
            if char in vowels:
                continue
            else:
                # It is a consonant, put underscore and reset count
                result += "_"
                count = 0
                
    # Remove the last underscore if the string ends with one
    if result.endswith("_"):
        result = result[:-1]
        
    return result

# Test cases from your image
print(f"hello -> {solve_underscore('hello')}")
print(f"assalom -> {solve_underscore('assalom')}")
print(f"abcabcabcdeabcdefabcdefg -> {solve_underscore('abcabcabcdeabcdefabcdefg')}")
print("-" * 30)


# ==========================================
# Task 2: Integer Squares Exercise
# ==========================================
# Answer
print("--- Task 2: Integer Squares ---")

# Note: In a real script, you would use input(). 
# For this demo, I will set n = 5 as per your example.
n = 5 
# n = int(input()) # Uncomment this line to use user input

for i in range(n):
    print(i ** 2)
print("-" * 30)


# ==========================================
# Task 3: Loop-Based Exercises (1-13)
# ==========================================
# Answer
print("--- Task 3: Loop Exercises ---")

print("\nEx 1: First 10 natural numbers (while loop)")
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

print("\nEx 2: Number Pattern")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nEx 3: Sum of numbers 1 to 10")
num_limit = 10
total_sum = sum(range(1, num_limit + 1))
print(f"Sum is: {total_sum}")

print("\nEx 4: Multiplication table of 2")
num_table = 2
for i in range(1, 11):
    print(num_table * i)

print("\nEx 5: Display numbers from list (Specific conditions)")
# Logic inferred from output: 
# Print if divisible by 5. Skip if > 150. Stop loop if > 500.
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)

print("\nEx 6: Count digits in 75869")
num_digits = 75869
count = 0
temp = num_digits
while temp != 0:
    temp //= 10
    count += 1
print(f"Output: {count}")

print("\nEx 7: Reverse Pattern")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print("\nEx 8: Print list in reverse")
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

print("\nEx 9: -10 to -1 using for loop")
for i in range(-10, 0):
    print(i)

print("\nEx 10: Loop with else")
for i in range(5):
    print(i, end="")
else:
    print("Done!")

print("\nEx 11: Primes between 25 and 50")
start, end = 25, 50
print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)

print("\nEx 12: Fibonacci up to 10 terms")
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end="  ")
    a, b = b, a + b
print()

print("\nEx 13: Factorial of 5")
num_fact = 5
factorial = 1
for i in range(1, num_fact + 1):
    factorial *= i
print(f"{num_fact}! = {factorial}")
print("-" * 30)


# ==========================================
# Task 4: Return Uncommon Elements
# ==========================================
# Answer
print("--- Task 4: Uncommon Elements ---")

def get_uncommon(list1, list2):
    result = []
    # Add items from list1 that are NOT in list2
    for item in list1:
        if item not in list2:
            result.append(item)
            
    # Add items from list2 that are NOT in list1
    for item in list2:
        if item not in list1:
            result.append(item)
            
    return result

# Test Cases
l1_a = [1, 1, 2]
l2_a = [2, 3, 4]
print(f"Input: {l1_a}, {l2_a}")
print(f"Output: {get_uncommon(l1_a, l2_a)}")

l1_b = [1, 2, 3]
l2_b = [4, 5, 6]
print(f"\nInput: {l1_b}, {l2_b}")
print(f"Output: {get_uncommon(l1_b, l2_b)}")

l1_c = [1, 1, 2, 3, 4, 2]
l2_c = [1, 3, 4, 5]
print(f"\nInput: {l1_c}, {l2_c}")
print(f"Output: {get_uncommon(l1_c, l2_c)}")
print("-" * 30)
