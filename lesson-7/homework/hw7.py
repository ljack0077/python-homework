# ==========================================
# PART 1: Map and Filter Explanation
# ==========================================

"""
EXPLANATION FOR CLASS:

1. map(function, iterable)
   - What it does: It takes a function and applies it to every single item in a list (or other iterable).
   - Result: Returns a map object (which you usually convert to a list).
   
2. filter(function, iterable)
   - What it does: It looks at every item in a list and decides whether to keep it or throw it away based on a function that returns True or False.
   - Result: Returns only the items where the function returned True.

3. lambda arguments : expression
   - What it is: A small, anonymous function (a function without a name) defined in a single line.
"""

# --- Examples using lambda ---

# Example 1: MAP
# Goal: Square every number in the list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Mapped (Squared): {squared_numbers}") 
# Output: [1, 4, 9, 16, 25]


# Example 2: FILTER
# Goal: Keep only even numbers
numbers_mix = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_mix))
print(f"Filtered (Evens): {even_numbers}")
# Output: [2, 4, 6, 8, 10]


print("-" * 30)


# ==========================================
# PART 2: Problem Solutions
# ==========================================

## 1. is_prime(n) funksiyasi
# Task: Check if n is prime. Return True or False.
print("--- Task 1: is_prime(n) ---")

def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # Check divisibility from 2 up to the square root of n
    # We use int(n**0.5) + 1 to be efficient
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            
    return True

# Test Cases
print(f"Input: 4 -> {is_prime(4)}")  # False
print(f"Input: 7 -> {is_prime(7)}")  # True
print("-" * 30)


## 2. digit_sum(k) funksiyasi
# Task: Calculate the sum of digits of number k.
print("--- Task 2: digit_sum(k) ---")

def digit_sum(k):
    # We can use map and lambda here effectively!
    # 1. str(k) converts number to string "502"
    # 2. map(int, ...) converts each character back to integer [5, 0, 2]
    # 3. sum(...) adds them up
    return sum(map(int, str(k)))

# Test Cases
print(f"Input: 24 -> {digit_sum(24)}")   # 6
print(f"Input: 502 -> {digit_sum(502)}") # 7
print("-" * 30)


## 3. Ikki sonning darajalari
# Task: Print powers of 2 (2^k) that do not exceed N.
print("--- Task 3: Powers of 2 ---")

def print_powers_of_two(N):
    power = 2 # Starting from 2^1 based on your example (2, 4, 8)
    
    result_list = []
    while power <= N:
        result_list.append(power)
        power *= 2 # Multiply by 2 to get next power
        
    # Printing as space-separated string
    print(*result_list)

# Test Case
print("Input: 10")
print("Result:", end=" ")
print_powers_of_two(10) # Expected: 2 4 8
print("-" * 30)
