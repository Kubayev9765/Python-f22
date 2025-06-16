#1
from datetime import date
class Task:
    def __init__(self, title, description, due_date, status="Not Started"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"Task: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}"

    def update_status(self, new_status):
        self.status = new_status

    def is_overdue(self, current_date):
        return current_date > self.due_date


    from datetime import date

# Create a task
task1 = Task(
    title="Finish project report",
    description="Write and submit the final report for the project.",
    due_date=date(2025, 6, 20)
)

# Print task details
print(task1)

# Update the status
task1.update_status("In Progress")
print("\nUpdated Task:")
print(task1)

# Check if the task is overdue
today = date.today()
if task1.is_overdue(today):
    print("\nThis task is overdue.")
else:
    print("\nThis task is not overdue.")

#2
from datetime import date

class Task:
    def __init__(self, title, description, due_date, status="Not Started"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = "Complete"

    def is_complete(self):
        return self.status == "Complete"

    def __str__(self):
        return f"Task: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}\n"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print(f"Task '{title}' not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        found = False
        for task in self.tasks:
            if not task.is_complete():
                print(task)
                found = True
        if not found:
            print("No incomplete tasks.")


# Create a to-do list
todo = ToDoList()

# Create tasks
task1 = Task("Buy groceries", "Milk, Bread, Eggs", date(2025, 6, 18))
task2 = Task("Finish homework", "Math and Science", date(2025, 6, 19))

# Add tasks to the list
todo.add_task(task1)
todo.add_task(task2)

# List all tasks
print("All Tasks:")
todo.list_all_tasks()

# Mark a task as complete
todo.mark_task_complete("Buy groceries")

# List only incomplete tasks
print("\nIncomplete Tasks:")
todo.list_incomplete_tasks()


#3
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Task:
    title: str
    description: str
    due_date: datetime
    status: str = "Not Started"

    def mark_complete(self):
        self.status = "Complete"

    def is_complete(self):
        return self.status == "Complete"

    def __str__(self):
        return f"Task: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date.date()}\nStatus: {self.status}\n"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print(f"Task '{title}' not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        found = False
        for task in self.tasks:
            if not task.is_complete():
                print(task)
                found = True
        if not found:
            print("No incomplete tasks.")


def main():
    todo = ToDoList()

    while True:
        print("\n==== To-Do List Menu ====")
        print("1. Add a Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_input = input("Enter due date (YYYY-MM-DD): ")
            try:
                due_date = datetime.strptime(due_input, "%Y-%m-%d")
                task = Task(title, description, due_date)
                todo.add_task(task)
                print("Task added successfully.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        elif choice == "2":
            title = input("Enter the title of the task to mark as complete: ")
            todo.mark_task_complete(title)

        elif choice == "3":
            print("\n--- All Tasks ---")
            todo.list_all_tasks()

        elif choice == "4":
            print("\n--- Incomplete Tasks ---")
            todo.list_incomplete_tasks()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()

python todo_cli.py

# 4

from datetime import datetime

# Reuse the Task and ToDoList classes (already defined in earlier responses)

# Create a test function
def test_todo_list():
    # Step 1: Create the to-do list
    todo = ToDoList()

    # Step 2: Create task instances
    task1 = Task("Buy groceries", "Milk, Bread, Eggs", datetime(2025, 6, 18))
    task2 = Task("Do homework", "Math chapter 5", datetime(2025, 6, 19))
    task3 = Task("Read book", "Finish 3 chapters of novel", datetime(2025, 6, 21))

    # Step 3: Add tasks to the ToDoList
    todo.add_task(task1)
    todo.add_task(task2)
    todo.add_task(task3)

    print("=== All Tasks After Adding ===")
    todo.list_all_tasks()

    # Step 4: Mark one task as complete
    todo.mark_task_complete("Do homework")

    print("\n=== All Tasks After Marking One Complete ===")
    todo.list_all_tasks()

    print("\n=== Incomplete Tasks ===")
    todo.list_incomplete_tasks()

# Run the test
test_todo_list()

Homework_2

#1

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent:\n{self.content}\n"
# Create an instance of Post
post1 = Post(
    title="Python Tips",
    content="Always use virtual environments for your Python projects.",
    author="To'lqin"
)

# Print the post
print(post1)

#2
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"Post '{post.title}' added.")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
            return
        for post in self.posts:
            print(post)

    def display_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print(post)
                found = True
        if not found:
            print(f"No posts found by author '{author_name}'.")


# Reuse Post class from before
post1 = Post("Python Basics", "Learn about variables, loops, and functions.", "To'lqin")
post2 = Post("Advanced Python", "Dive into decorators and generators.", "To'lqin")
post3 = Post("JavaScript Intro", "Start with variables and functions.", "Ali")

# Create a blog
my_blog = Blog()

# Add posts to blog
my_blog.add_post(post1)
my_blog.add_post(post2)
my_blog.add_post(post3)

# List all posts
print("\n=== All Posts ===")
my_blog.list_all_posts()

# Display posts by a specific author
print("\n=== Posts by To'lqin ===")
my_blog.display_posts_by_author("To'lqin")


#3
# Post class
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent:\n{self.content}\n"


# Blog class
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"Post '{post.title}' added.\n")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.\n")
        else:
            for post in self.posts:
                print(post)

    def display_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print(post)
                found = True
        if not found:
            print(f"No posts found by author '{author_name}'.\n")


# CLI Main Program
def main():
    blog = Blog()

    while True:
        print("=== Blog Menu ===")
        print("1. Add a Post")
        print("2. List All Posts")
        print("3. Show Posts by Author")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == "2":
            print("\n=== All Blog Posts ===")
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author's name: ")
            print(f"\n=== Posts by {author} ===")
            blog.display_posts_by_author(author)

        elif choice == "4":
            print("Exiting the blog system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.\n")


# Run the main program
if __name__ == "__main__":
    main()


#4
from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Date: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Content:\n{self.content}\n")

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"Post '{post.title}' added.\n")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.\n")
        else:
            for post in self.posts:
                print(post)

    def display_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print(post)
                found = True
        if not found:
            print(f"No posts found by author '{author_name}'.\n")

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"Post '{title}' deleted.\n")
                return
        print(f"No post found with title '{title}'.\n")

    def edit_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                print("Leave blank to keep the current value.\n")
                new_title = input(f"New title (current: {post.title}): ") or post.title
                new_content = input(f"New content (current: {post.content}): ") or post.content
                new_author = input(f"New author (current: {post.author}): ") or post.author
                post.title = new_title
                post.content = new_content
                post.author = new_author
                print("Post updated.\n")
                return
        print(f"No post found with title '{title}'.\n")

    def display_latest_posts(self, count=3):
        sorted_posts = sorted(self.posts, key=lambda p: p.created_at, reverse=True)
        latest = sorted_posts[:count]
        if not latest:
            print("No posts available.\n")
        else:
            print(f"Showing latest {len(latest)} post(s):\n")
            for post in latest:
                print(post)
def main():
    blog = Blog()

    while True:
        print("=== Blog Menu ===")
        print("1. Add a Post")
        print("2. List All Posts")
        print("3. Show Posts by Author")
        print("4. Delete a Post")
        print("5. Edit a Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == "2":
            print("\n=== All Blog Posts ===")
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author's name: ")
            print(f"\n=== Posts by {author} ===")
            blog.display_posts_by_author(author)

        elif choice == "4":
            title = input("Enter title of the post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Enter title of the post to edit: ")
            blog.edit_post(title)

        elif choice == "6":
            try:
                count = int(input("How many latest posts to show? (default 3): ") or "3")
                blog.display_latest_posts(count)
            except ValueError:
                print("Invalid number. Please enter a digit.\n")

        elif choice == "7":
            print("Exiting the blog system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.\n")

#5
from datetime import datetime, timedelta
import time

# Assuming Post and Blog classes have been defined as before
# and include timestamp handling, edit/delete/display features

# Test function for the Blog system
def test_blog_system():
    blog = Blog()

    # Step 1: Create sample posts
    post1 = Post("Intro to Python", "Learn the basics of Python programming.", "To'lqin")
    time.sleep(1)  # Ensure different timestamps
    post2 = Post("Flask Web Dev", "Build web apps using Flask framework.", "Ali")
    time.sleep(1)
    post3 = Post("Data Science", "Intro to Pandas and data analysis.", "To'lqin")
    time.sleep(1)
    post4 = Post("Decorators in Python", "Understand how decorators work.", "Sara")

    # Step 2: Add posts to the blog
    blog.add_post(post1)
    blog.add_post(post2)
    blog.add_post(post3)
    blog.add_post(post4)

    # Step 3: List all posts
    print("=== All Posts ===")
    blog.list_all_posts()

    # Step 4: Display posts by specific author
    print("=== Posts by 'To'lqin' ===")
    blog.display_posts_by_author("To'lqin")

    # Step 5: Edit a post
    print("=== Editing Post 'Data Science' ===")
    post_to_edit = "Data Science"
    # Simulating inputs (normally user would enter this)
    for post in blog.posts:
        if post.title == post_to_edit:
            post.title = "Data Science with Pandas"
            post.content = "Learn how to use Pandas for data analysis."
            post.author = "To'lqin"
            print(f"Post '{post_to_edit}' updated.\n")
            break

    # Step 6: Delete a post
    print("=== Deleting Post 'Flask Web Dev' ===")
    blog.delete_post("Flask Web Dev")

    # Step 7: Display latest 2 posts
    print("=== Latest 2 Posts ===")
    blog.display_latest_posts(2)

# Run the test
test_blog_system()


homework_3

# 1
class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def __str__(self):
        return f"Account[{self.account_number}] - {self.holder_name}: ${self.balance:.2f}"
acc1 = Account("123456", "John Doe", 1000.0)
print(acc1)


#2
class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_number}] - {self.holder_name}: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            return account.get_balance()
        return "Account not found"

    def deposit_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            if account.deposit(amount):
                return f"${amount:.2f} deposited. New balance: ${account.get_balance():.2f}"
            return "Invalid deposit amount"
        return "Account not found"

    def withdraw_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            if account.withdraw(amount):
                return f"${amount:.2f} withdrawn. New balance: ${account.get_balance():.2f}"
            return "Insufficient balance or invalid amount"
        return "Account not found"
# Create Bank
my_bank = Bank()

# Create Accounts
acc1 = Account("111", "Alice", 500.0)
acc2 = Account("222", "Bob", 1000.0)

# Add accounts to bank
my_bank.add_account(acc1)
my_bank.add_account(acc2)

# Operations
print(my_bank.check_balance("111"))           # 500.0
print(my_bank.deposit_money("111", 200))      # Deposit result
print(my_bank.withdraw_money("111", 100))     # Withdraw result
print(my_bank.check_balance("111"))           # New balance


# 3

class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_number}] - {self.holder_name}: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            return account.get_balance()
        return None

    def deposit_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account and account.deposit(amount):
            return account.get_balance()
        return None

    def withdraw_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account and account.withdraw(amount):
            return account.get_balance()
        return None


def main():
    bank = Bank()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            account = Account(acc_num, name, balance)
            bank.add_account(account)
            print("Account added successfully.")

        elif choice == '2':
            acc_num = input("Enter account number: ")
            balance = bank.check_balance(acc_num)
            if balance is not None:
                print(f"Balance: ${balance:.2f}")
            else:
                print("Account not found.")

        elif choice == '3':
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            new_balance = bank.deposit_money(acc_num, amount)
            if new_balance is not None:
                print(f"Deposit successful. New balance: ${new_balance:.2f}")
            else:
                print("Deposit failed. Account not found or invalid amount.")

        elif choice == '4':
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            new_balance = bank.withdraw_money(acc_num, amount)
            if new_balance is not None:
                print(f"Withdrawal successful. New balance: ${new_balance:.2f}")
            else:
                print("Withdrawal failed. Account not found or insufficient funds.")

        elif choice == '5':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 5.")


# Run the CLI program
if __name__ == "__main__":
    main()


#4
class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount, allow_overdraft=False):
        if amount <= 0:
            return False
        if amount > self.balance and not allow_overdraft:
            return False
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_number}] - {self.holder_name} - Balance: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        return account.get_balance() if account else None

    def deposit_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account and account.deposit(amount):
            return account.get_balance()
        return None

    def withdraw_money(self, account_number, amount, allow_overdraft=False):
        account = self.find_account(account_number)
        if account and account.withdraw(amount, allow_overdraft):
            return account.get_balance()
        return None

    def transfer_money(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)
        if sender and receiver and amount > 0:
            if sender.withdraw(amount, allow_overdraft=True):
                receiver.deposit(amount)
                return True
        return False

    def display_account_details(self, account_number):
        account = self.find_account(account_number)
        return str(account) if account else "Account not found."


def main():
    bank = Bank()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            account = Account(acc_num, name, balance)
            bank.add_account(account)
            print("✅ Account added successfully.")

        elif choice == '2':
            acc_num = input("Enter account number: ")
            balance = bank.check_balance(acc_num)
            if balance is not None:
                print(f"💰 Balance: ${balance:.2f}")
            else:
                print("❌ Account not found.")

        elif choice == '3':
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            new_balance = bank.deposit_money(acc_num, amount)
            if new_balance is not None:
                print(f"✅ Deposit successful. New balance: ${new_balance:.2f}")
            else:
                print("❌ Deposit failed. Check account or amount.")

        elif choice == '4':
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            new_balance = bank.withdraw_money(acc_num, amount, allow_overdraft=True)
            if new_balance is not None:
                status = "⚠️ Overdraft used!" if new_balance < 0 else "✅ Withdrawal successful."
                print(f"{status} New balance: ${new_balance:.2f}")
            else:
                print("❌ Withdrawal failed. Check account or amount.")

        elif choice == '5':
            from_acc = input("Enter sender account number: ")
            to_acc = input("Enter receiver account number: ")
            amount = float(input("Enter amount to transfer: "))
            success = bank.transfer_money(from_acc, to_acc, amount)
            if success:
                print("✅ Transfer successful.")
            else:
                print("❌ Transfer failed. Check accounts or amount.")

        elif choice == '6':
            acc_num = input("Enter account number: ")
            print(bank.display_account_details(acc_num))

        elif choice == '7':
            print("👋 Exiting the system. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please select from 1 to 7.")


#5
# Reuse the Account and Bank classes from before

# Create a bank instance
bank = Bank()

# Add test accounts
acc1 = Account("101", "Alice", 1000.0)
acc2 = Account("102", "Bob", 500.0)
acc3 = Account("103", "Charlie", 0.0)

bank.add_account(acc1)
bank.add_account(acc2)
bank.add_account(acc3)

# Test deposit
print("👉 Deposit $200 to Bob:")
print(bank.deposit_money("102", 200))  # Expected: 700.0

# Test withdrawal
print("\n👉 Withdraw $150 from Alice:")
print(bank.withdraw_money("101", 150))  # Expected: 850.0

# Test overdraft withdrawal
print("\n👉 Withdraw $100 from Charlie (overdraft allowed):")
print(bank.withdraw_money("103", 100, allow_overdraft=True))  # Expected: -100.0

# Test transfer
print("\n👉 Transfer $300 from Alice to Bob:")
transfer_result = bank.transfer_money("101", "102", 300)
print("Transfer success:", transfer_result)
print("Alice’s balance:", bank.check_balance("101"))  # Expected: 550.0
print("Bob’s balance:", bank.check_balance("102"))    # Expected: 1000.0

# Test displaying account details
print("\n👉 Display all account details:")
for acc_num in ["101", "102", "103"]:
    print(bank.display_account_details(acc_num))

# Test invalid deposit
print("\n👉 Try depositing negative amount to Alice:")
print(bank.deposit_money("101", -50))  # Expected: None

# Test invalid transfer (nonexistent account)
print("\n👉 Try transferring to non-existing account:")
print(bank.transfer_money("101", "999", 50))  # Expected: False

