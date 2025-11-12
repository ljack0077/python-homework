# --- Dictionary Exercises ---

## 1. Sort a Dictionary by Value
#solution
print("--- Dict Task 1: Sort by Value ---")
d = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1}
print(f"Original dictionary: {d}")

# Ascending sort
sorted_asc = dict(sorted(d.items(), key=lambda item: item[1]))
print(f"Sorted ascending by value: {sorted_asc}")

# Descending sort
sorted_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print(f"Sorted descending by value: {sorted_desc}")
print("-" * 25)


## 2. Add a Key to a Dictionary
#solution
print("--- Dict Task 2: Add a Key ---")
d = {0: 10, 1: 20}
print(f"Original dictionary: {d}")
d[2] = 30
print(f"Updated dictionary: {d}")
print("-" * 25)


## 3. Concatenate Multiple Dictionaries
#solution
print("--- Dict Task 3: Concatenate Dictionaries ---")
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
print(f"dic1: {dic1}")
print(f"dic2: {dic2}")
print(f"dic3: {dic3}")

# Using the | operator (Python 3.9+)
concatenated_dict = dic1 | dic2 | dic3
print(f"Concatenated (using |): {concatenated_dict}")

# Alternative for older Python (using update)
# dic_new = {}
# dic_new.update(dic1)
# dic_new.update(dic2)
# dic_new.update(dic3)
# print(f"Concatenated (using update): {dic_new}")
print("-" * 25)


## 4. Generate a Dictionary with Squares (n=5)
#solution
print("--- Dict Task 4: Generate Squares (n=5) ---")
n = 5
squares_dict_n = {x: x*x for x in range(1, n + 1)}
print(f"Dictionary of squares for n={n}: {squares_dict_n}")
print("-" * 25)


## 5. Dictionary of Squares (1 to 15)
#solution
print("--- Dict Task 5: Squares from 1 to 15 ---")
squares_dict_15 = {x: x*x for x in range(1, 16)}
print(f"Dictionary of squares (1-15): {squares_dict_15}")
print("-" * 25)


# --- Set Exercises ---

## 1. Create a Set
#solution
print("--- Set Task 1: Create a Set ---")
# Using curly braces
my_set_literal = {1, 2, "hello", 3, 2} # Duplicates are automatically removed
print(f"Set created with {{}}: {my_set_literal}")

# Using the set() function from a list
my_set_func = set([1, 2, "hello", 3, 2])
print(f"Set created with set(): {my_set_func}")
print("-" * 25)


## 2. Iterate Over a Set
#solution
print("--- Set Task 2: Iterate Over a Set ---")
s = {"apple", "banana", "cherry"}
print(f"Iterating over set: {s}")
for item in s:
    print(item)
print("-" * 25)


## 3. Add Member(s) to a Set
#solution
print("--- Set Task 3: Add Member(s) ---")
s = {"red", "green"}
print(f"Original set: {s}")
# Add a single member
s.add("blue")
print(f"After adding 'blue': {s}")
# Add multiple members
s.update(["yellow", "orange", "red"]) # 'red' is already in, so it's ignored
print(f"After updating with multiple items: {s}")
print("-" * 25)


## 4. Remove Item(s) from a Set
#solution
print("--- Set Task 4: Remove Item(s) ---")
s = {"a", "b", "c", "d", "e"}
print(f"Original set: {s}")

# .remove() will raise an error if the item is not found
s.remove("b")
print(f"After removing 'b' (using .remove()): {s}")

# .discard() will NOT raise an error if the item is not found
s.discard("c")
print(f"After removing 'c' (using .discard()): {s}")

# .pop() removes and returns an arbitrary item
popped_item = s.pop()
print(f"Popped an arbitrary item: {popped_item}")
print(f"Set after pop: {s}")
print("-" * 25)


## 5. Remove an Item if Present in the Set
#solution
print("--- Set Task 5: Remove an Item if Present ---")
s = {"cat", "dog", "lion"}
print(f"Original set: {s}")

# We want to remove 'dog'
s.discard("dog")
print(f"After discarding 'dog' (was present): {s}")

# We want to remove 'fish'
s.discard("fish")
print(f"After discarding 'fish' (was not present): {s}")
print("-" * 25)

print("\nAll tasks complete.")
