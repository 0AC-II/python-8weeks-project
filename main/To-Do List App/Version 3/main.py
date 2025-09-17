from task_manager import TaskManager

def main():
    manager = TaskManager()
    running = True

    while running:
        print("\n📋 To-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Search Tasks")
        print("5. Sort Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task = input("Enter task: ")
            manager.add_task(task)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            try:
                index = int(input("Enter task number to delete: "))
                manager.delete_task(index)
            except ValueError:                                      # Handle non-integer input
                print("Invalid input! Enter a number.")

        elif choice == "4":
            keyword = input("Enter keyword to search: ")
            manager.search_tasks(keyword)

        elif choice == "5":
            option = input("Sort by 'alphabetical' or 'length': ").lower() # Normalize input to lowercase
            manager.sort_tasks(option)
            manager.view_tasks()

        elif choice == "6":
            print("Goodbye!")
            running = False

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
