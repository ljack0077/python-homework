import math
from datetime import date

# ==========================================
# 1. Circle Class
# ==========================================
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# ==========================================
# 2. Person Class
# ==========================================
class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date  # Expecting datetime.date object

    def calculate_age(self):
        today = date.today()
        # Returns True (1) if birthday hasn't happened yet, False (0) otherwise
        not_birthday_yet = (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        return today.year - self.birth_date.year - not_birthday_yet

# ==========================================
# 3. Calculator Class
# ==========================================
class Calculator:
    def add(self, x, y): return x + y
    def subtract(self, x, y): return x - y
    def multiply(self, x, y): return x * y
    def divide(self, x, y):
        return "Error: Cannot divide by zero." if y == 0 else x / y

# ==========================================
# 4. Shape and Subclasses
# ==========================================
class Shape:
    def area(self): pass
    def perimeter(self): pass

class CircleShape(Shape): # Renamed to avoid conflict with Q1
    def __init__(self, radius):
        self.radius = radius
    def area(self): return math.pi * self.radius ** 2
    def perimeter(self): return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self): return self.side ** 2
    def perimeter(self): return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# ==========================================
# 5. Binary Search Tree Class
# ==========================================
class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None: self.root = BSTNode(key)
        else: self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.val:
            if current.left is None: current.left = BSTNode(key)
            else: self._insert_recursive(current.left, key)
        else:
            if current.right is None: current.right = BSTNode(key)
            else: self._insert_recursive(current.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        if current is None or current.val == key: return current
        if key < current.val: return self._search_recursive(current.left, key)
        return self._search_recursive(current.right, key)

# ==========================================
# 6 & 9. Stack Data Structure (with Display)
# ==========================================
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"[Stack] Pushed: {item}")

    def pop(self):
        return self.items.pop() if not self.is_empty() else "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(f"[Stack] Current: {self.items}")

# ==========================================
# 7. Linked List Data Structure
# ==========================================
class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = LLNode(data)
        if not self.head: self.head = new_node
        else:
            last = self.head
            while last.next: last = last.next
            last.next = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp: prev.next = temp.next

    def display(self):
        elems = []
        current = self.head
        while current:
            elems.append(str(current.data))
            current = current.next
        print(" -> ".join(elems) + " -> None")

# ==========================================
# 8. Shopping Cart Class
# ==========================================
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items: del self.items[name]

    def calculate_total(self):
        return sum(self.items.values())

# ==========================================
# 10. Queue Data Structure
# ==========================================
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"[Queue] Enqueued: {item}")

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

# ==========================================
# 11. Bank Class
# ==========================================
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_num, initial_balance=0):
        if acc_num not in self.accounts:
            self.accounts[acc_num] = initial_balance
            print(f"[Bank] Account {acc_num} created.")
        else: print("[Bank] Account already exists.")

    def deposit(self, acc_num, amount):
        if acc_num in self.accounts:
            self.accounts[acc_num] += amount
            print(f"[Bank] Deposited {amount}. New Balance: {self.accounts[acc_num]}")

    def withdraw(self, acc_num, amount):
        if acc_num in self.accounts and self.accounts[acc_num] >= amount:
            self.accounts[acc_num] -= amount
            print(f"[Bank] Withdrew {amount}. New Balance: {self.accounts[acc_num]}")

# ==========================================
# Main Execution Block (Test Code)
# ==========================================
if __name__ == "__main__":
    print("--- Q1: Circle ---")
    c = Circle(5)
    print(f"Area: {c.calculate_area():.2f}")

    print("\n--- Q2: Person ---")
    p = Person("Sam", "UK", date(1995, 6, 20))
    print(f"{p.name} is {p.calculate_age()} years old.")

    print("\n--- Q3: Calculator ---")
    print(f"10 / 2 = {Calculator().divide(10, 2)}")

    print("\n--- Q4: Shapes ---")
    print(f"Square Area: {Square(4).area()}")

    print("\n--- Q5: BST ---")
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    print("Found 30?" , "Yes" if bst.search(30) else "No")

    print("\n--- Q6 & 9: Stack ---")
    s = Stack()
    s.push(1)
    s.push(2)
    s.display()
    print(f"Popped: {s.pop()}")

    print("\n--- Q7: Linked List ---")
    ll = LinkedList()
    ll.insert("A")
    ll.insert("B")
    ll.display()

    print("\n--- Q8: Shopping Cart ---")
    cart = ShoppingCart()
    cart.add_item("Laptop", 1000)
    cart.add_item("Mouse", 50)
    print(f"Cart Total: ${cart.calculate_total()}")

    print("\n--- Q10: Queue ---")
    q = Queue()
    q.enqueue("Ticket 1")
    q.dequeue()

    print("\n--- Q11: Bank ---")
    b = Bank()
    b.create_account(101, 100)
    b.withdraw(101, 50)
