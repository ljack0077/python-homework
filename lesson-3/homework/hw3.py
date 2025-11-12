## 1. Create and Access List Elements
#solution
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("--- Task 1 ---")
print(f"The list of fruits is: {fruits}")
print(f"The third fruit is: {fruits[2]}")
print("-" * 25)


## 2. Concatenate Two Lists
#solution
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("--- Task 2 ---")
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Concatenated list: {concatenated_list}")
print("-" * 25)


## 3. Extract Elements from a List
#solution
numbers_3 = [10, 20, 30, 40, 50]
middle_index = len(numbers_3) // 2
extracted = [numbers_3[0], numbers_3[middle_index], numbers_3[-1]]
print("--- Task 3 ---")
print(f"Original list: {numbers_3}")
print(f"Extracted elements (first, middle, last): {extracted}")
print("-" * 25)


## 4. Convert List to Tuple
#solution
movies_list = ["Inception", "The Matrix", "Interstellar", "Parasite", "Pulp Fiction"]
movies_tuple = tuple(movies_list)
print("--- Task 4 ---")
print(f"Original list: {movies_list}")
print(f"Converted tuple: {movies_tuple}")
print("-" * 25)


## 5. Check Element in a List
#solution
cities = ["Tokyo", "London", "New York", "Paris", "Sydney"]
is_in_list = "Paris" in cities
print("--- Task 5 ---")
print(f"List of cities: {cities}")
print(f"Is 'Paris' in the list? {is_in_list}")
print("-" * 25)


## 6. Duplicate a List Without Using Loops
#solution
numbers_6 = [1, 2, 3]
duplicated_list = numbers_6 * 2
print("--- Task 6 ---")
print(f"Original list: {numbers_6}")
print(f"Duplicated list: {duplicated_list}")
print("-" * 25)


## 7. Swap First and Last Elements of a List
#solution
numbers_7 = [10, 20, 30, 40, 50]
print("--- Task 7 ---")
print(f"Original list: {numbers_7}")
# Swap using tuple assignment
numbers_7[0], numbers_7[-1] = numbers_7[-1], numbers_7[0]
print(f"Swapped list: {numbers_7}")
print("-" * 25)


## 8. Slice a Tuple
#solution
tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Slice from index 3 up to (but not including) index 8 to get indices 3, 4, 5, 6, 7
slice_8 = tuple_8[3:8]
print("--- Task 8 ---")
print(f"Original tuple: {tuple_8}")
print(f"Slice from index 3 to 7: {slice_8}")
print("-" * 25)


## 9. Count Occurrences in a List
#solution
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
count_blue = colors.count("blue")
print("--- Task 9 ---")
print(f"List of colors: {colors}")
print(f"The color 'blue' appears {count_blue} times.")
print("-" * 25)


## 10. Find the Index of an Element in a Tuple
#solution
animals = ("cat", "dog", "lion", "elephant", "tiger")
lion_index = animals.index("lion")
print("--- Task 10 ---")
print(f"Tuple of animals: {animals}")
print(f"The index of 'lion' is: {lion_index}")
print("-" * 25)


## 11. Merge Two Tuples
#solution
tuple_11a = (1, 2, 3)
tuple_11b = (4, 5, 6)
merged_tuple = tuple_11a + tuple_11b
print("--- Task 11 ---")
print(f"Tuple 1: {tuple_11a}")
print(f"Tuple 2: {tuple_11b}")
print(f"Merged tuple: {merged_tuple}")
print("-" * 25)


## 12. Find the Length of a List and Tuple
#solution
list_12 = [1, "a", True, 4.5]
tuple_12 = (1, "a", True, 4.5, "extra")
print("--- Task 12 ---")
print(f"List: {list_12}")
print(f"Length of list: {len(list_12)}")
print(f"Tuple: {tuple_12}")
print(f"Length of tuple: {len(tuple_12)}")
print("-" * 25)


## 13. Convert Tuple to List
#solution
tuple_13 = (100, 200, 300, 400, 500)
list_13 = list(tuple_13)
print("--- Task 13 ---")
print(f"Original tuple: {tuple_13}")
print(f"Converted list: {list_13}")
print("-" * 25)


## 14. Find Maximum and Minimum in a Tuple
#solution
numbers_14 = (7, 2, 9, 1, 5, 12, 0)
max_val = max(numbers_14)
min_val = min(numbers_14)
print("--- Task 14 ---")
print(f"Tuple of numbers: {numbers_14}")
print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")
print("-" * 25)


## 15. Reverse a Tuple
#solution
words_15 = ("hello", "world", "python", "is", "fun")
reversed_tuple = words_15[::-1]
print("--- Task 15 ---")
print(f"Original tuple: {words_15}")
print(f"Reversed tuple: {reversed_tuple}")
print("-" * 25)

print("\nAll tasks complete.")
