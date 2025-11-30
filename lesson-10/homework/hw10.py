import datetime

# ======================================================
# HOMEWORK 1: TODO LIST APPLICATION
# ======================================================

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"[{self.status}] {self.title} (Due: {self.due_date}) - {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        new_task = Task(title, description, due_date)
        self.tasks.append(new_task)
        print(f"Task '{title}' added.")

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f"Task '{self.tasks[index].title}' marked as complete.")
        else:
            print("Invalid task number.")

    def list_tasks(self):
        print("\n--- All Tasks ---")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def list_incomplete_tasks(self):
        print("\n--- Incomplete Tasks ---")
        found = False
        for task in self.tasks:
            if task.status == "Incomplete":
                print(task)
                found = True
        if not found:
            print("No incomplete tasks!")

def run_todo_app():
    todo = ToDoList()
    while True:
        print("\n=== ToDo List Menu ===")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Title: ")
            desc = input("Description: ")
            date = input("Due Date (YYYY-MM-DD): ")
            todo.add_task(title, desc, date)
        elif choice == '2':
            todo.list_tasks()
            try:
                idx = int(input("Enter task number to mark complete: ")) - 1
                todo.mark_task_complete(idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            todo.list_tasks()
        elif choice == '4':
            todo.list_incomplete_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid option.")

# ======================================================
# HOMEWORK 2: SIMPLE BLOG SYSTEM
# ======================================================

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"Title: {self.title} | Author: {self.author} | Posted: {self.timestamp.strftime('%Y-%m-%d %H:%M')}\nContent: {self.content}\n"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        new_post = Post(title, content, author)
        self.posts.append(new_post)
        print(f"Post '{title}' published.")

    def list_posts(self):
        print("\n--- All Blog Posts ---")
        # Enhancements: Display latest first (reverse order)
        for i, post in enumerate(reversed(self.posts)):
            print(f"ID {len(self.posts) - i}: {post}")

    def display_by_author(self, author):
        print(f"\n--- Posts by {author} ---")
        found = False
        for post in self.posts:
            if post.author.lower() == author.lower():
                print(post)
                found = True
        if not found:
            print("No posts found by this author.")

    def delete_post(self, index):
        # Adjusting index for 0-based list
        if 0 <= index < len(self.posts):
            removed = self.posts.pop(index)
            print(f"Post '{removed.title}' deleted.")
        else:
            print("Invalid post ID.")

    def edit_post(self, index, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].content = new_content
            print("Post updated.")
        else:
            print("Invalid post ID.")

def run_blog_app():
    blog = Blog()
    # Adding some dummy data for testing
    blog.add_post("First Post", "Hello World", "Admin")
    
    while True:
        print("\n=== Blog System Menu ===")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Find Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Exit to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            t = input("Title: ")
            c = input("Content: ")
            a = input("Author: ")
            blog.add_post(t, c, a)
        elif choice == '2':
            blog.list_posts()
        elif choice == '3':
            a = input("Enter Author Name: ")
            blog.display_by_author(a)
        elif choice == '4':
            try:
                idx = int(input("Enter Post ID to delete: ")) - 1
                blog.delete_post(idx)
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            try:
                idx = int(input("Enter Post ID to edit: ")) - 1
                new_c = input("Enter new content: ")
                blog.edit_post(idx, new_c)
            except ValueError:
                print("Invalid input.")
        elif choice == '6':
            break

# ======================================================
# HOMEWORK 3: SIMPLE BANKING SYSTEM
# ======================================================

class Account:
    def __init__(self, acc_num, holder, balance=0):
        self.acc_num = acc_num
        self.holder = holder
        self.balance = balance

    def __str__(self):
        return f"Account: {self.acc_num} | Holder: {self.holder} | Balance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {} # Using dictionary for faster lookup {acc_num: AccountObj}

    def add_account(self, acc_num, holder, initial_deposit):
        if acc_num in self.accounts:
            print("Account number already exists.")
        else:
            new_acc = Account(acc_num, holder, initial_deposit)
            self.accounts[acc_num] = new_acc
            print("Account created successfully.")

    def get_account(self, acc_num):
        return self.accounts.get(acc_num)

    def deposit(self, acc_num, amount):
        acc = self.get_account(acc_num)
        if acc:
            acc.balance += amount
            print(f"Deposited ${amount}. New Balance: ${acc.balance:.2f}")
        else:
            print("Account not found.")

    def withdraw(self, acc_num, amount):
        acc = self.get_account(acc_num)
        if acc:
            # Overdraft handling: strictly preventing negative balance
            if acc.balance >= amount:
                acc.balance -= amount
                print(f"Withdrew ${amount}. New Balance: ${acc.balance:.2f}")
            else:
                print(f"Transaction denied. Insufficient funds (Overdraft protection). Current Balance: ${acc.balance:.2f}")
        else:
            print("Account not found.")

    def transfer(self, from_acc_num, to_acc_num, amount):
        sender = self.get_account(from_acc_num)
        receiver = self.get_account(to_acc_num)

        if sender and receiver:
            if sender.balance >= amount:
                sender.balance -= amount
                receiver.balance += amount
                print(f"Transferred ${amount} from {from_acc_num} to {to_acc_num}.")
            else:
                print("Transfer failed: Insufficient funds.")
        else:
            print("One or both account numbers are invalid.")

def run_bank_app():
    bank = Bank()
    while True:
        print("\n=== Banking System Menu ===")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Exit to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            num = input("Account Number: ")
            name = input("Account Holder Name: ")
            try:
                bal = float(input("Initial Deposit: "))
                bank.add_account(num, name, bal)
            except ValueError:
                print("Invalid amount.")
        elif choice == '2':
            num = input("Account Number: ")
            acc = bank.get_account(num)
            if acc: print(acc)
            else: print("Account not found.")
        elif choice == '3':
            num = input("Account Number: ")
            try:
                amt = float(input("Amount: "))
                bank.deposit(num, amt)
            except ValueError: print("Invalid amount.")
        elif choice == '4':
            num = input("Account Number: ")
            try:
                amt = float(input("Amount: "))
                bank.withdraw(num, amt)
            except ValueError: print("Invalid amount.")
        elif choice == '5':
            f_num = input("From Account: ")
            t_num = input("To Account: ")
            try:
                amt = float(input("Amount: "))
                bank.transfer(f_num, t_num, amt)
            except ValueError: print("Invalid amount.")
        elif choice == '6':
            break

# ======================================================
# MASTER MENU (Runs the chosen project)
# ======================================================

if __name__ == "__main__":
    while True:
        print("\n################################")
        print("      HOMEWORK PROJECTS HUB     ")
        print("################################")
        print("1. Run ToDo List App")
        print("2. Run Blog System")
        print("3. Run Banking System")
        print("q. Quit")
        
        selection = input("\nWhich project would you like to run? ")
        
        if selection == '1':
            run_todo_app()
        elif selection == '2':
            run_blog_app()
        elif selection == '3':
            run_bank_app()
        elif selection.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")
