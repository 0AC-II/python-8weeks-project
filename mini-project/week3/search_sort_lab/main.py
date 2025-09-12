# main.py
from search import linear_search, binary_search
from sort import bubble_sort, quick_sort
from recursion import factorial, fibonacci


def search_menu():
    arr = list(map(int, input("Enter numbers (comma-separated): ").split(","))) # Takes a comma-separated input from the user, splits it, converts each part into an integer, and stores it as a list of numbers.
    target = int(input("Enter target number: "))

    print("\n1. Linear Search")
    print("2. Binary Search (requires sorted list)")
    choice = input("Choose search type: ")

    if choice == "1":
        pos = linear_search(arr, target)
    else:
        pos = binary_search(sorted(arr), target) # Binary search requires a sorted array

    if pos != -1:
        print(f"Found at position {pos}")
    else:
        print("Not found")


def sort_menu():
    arr = list(map(int, input("Enter numbers (comma-separated): ").split(",")))

    print("\n1. Bubble Sort")
    print("2. Quick Sort")
    choice = input("Choose sorting method: ")

    if choice == "1":
        print("Sorted:", bubble_sort(arr))
    else:
        print("Sorted:", quick_sort(arr))


def recursion_menu():
    print("\n1. Factorial")
    print("2. Fibonacci")
    choice = input("Choose recursion example: ")

    if choice == "1":
        n = int(input("Enter n: "))
        print(f"Factorial({n}) = {factorial(n)}")
    elif choice == "2":
        n = int(input("Enter n: "))
        print(f"Fibonacci({n}) = {fibonacci(n)}")



def main():
    running = True
    while running:
        print("\n--- Search & Sort Lab + Recursive Toolbox ---") # Main menu loop
        print("1. Search")
        print("2. Sort")
        print("3. Recursion")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            search_menu()
        elif choice == "2":
            sort_menu()
        elif choice == "3":
            recursion_menu()
        elif choice == "4":
            print("Goodbye")
            running = False
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__": # Entry point
    main()
