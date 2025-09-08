# To-Do List App (V2)

# This is a simple command-line to-do list application that allows users to add, view, and delete tasks.

# Functions
def add_task(tasks):  # Function 1
    """Add a new task to the list"""
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks(tasks):  # Function 2
    """View all tasks in the list"""
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

def delete_task(tasks):  # Function 3
    """Delete a task by number."""
    if not tasks:
        print("No tasks to delete.")
    else:
        view_tasks(tasks)
        choice = int(input("Enter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")

# Main loop
def main():
    tasks = []  # list to hold tasks
    running = True

    while running:
        print("\nWelcome to your To-Do List App!")  
        print("\nChoose an option:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")     

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            running = False
            print("Goodbye!")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
