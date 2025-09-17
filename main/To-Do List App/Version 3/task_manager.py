class TaskManager:
    def __init__(self):
        """Initialize with an empty task list"""
        self.tasks = []

    def add_task(self, task):
        """Add a new task"""
        self.tasks.append(task)
        print(f"Task added: {task}")

    def view_tasks(self):
        """View all tasks"""
        if not self.tasks:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(self.tasks, start=1): # Start enumeration at 1 for user-friendly indexing
                print(f"{i}. {task}")

    def delete_task(self, index):
        """Delete a task by index"""
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1) # Adjust for 0-based index
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number.")

    def search_tasks(self, keyword):
        """Search tasks containing a keyword"""
        results = [t for t in self.tasks if keyword.lower() in t.lower()] # Makes the search case-insensitive
        if results:
            print("\n🔎 Search results:")
            for i, task in enumerate(results, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks matched your search.")

    def sort_tasks(self, by="alphabetical"):
        """Sort tasks either alphabetically or by length"""
        if not self.tasks:
            print("No tasks to sort.")
            return

        if by == "alphabetical":
            self.tasks.sort()
            print("Tasks sorted alphabetically.")
        elif by == "length":
            self.tasks.sort(key=len)
            print("Tasks sorted by length.")
        else:
            print("Invalid sort option.")