# 🎓 Student Grade Manager

A simple **Python console application** that lets you add students, record their scores, calculate averages, and assign letter grades (A–F).
This project was built as a **Week 2 mini-project** to practice:

* **Functions** (`*args`, return values, docstrings)
* **Loops** (`for`, `while`)
* **Conditionals** (`if`, `elif`, `else`, ternary logic)
* **Lists & Dictionaries** for storing structured data
* **Input validation** and clean **output formatting**

---

## 🚀 Features

* Add a student with multiple subject scores
* Automatically calculate average score
* Assign a grade (`A`–`F`) based on the average
* View a full student report (name, scores, average, grade)
* Input validation (only accepts numeric scores 0–100)
* Menu-driven interface with continuous loop until exit

---

Run the program

You’ll see:

```
🎓 Student Grade Manager
1. Add Student
2. View All Students
3. Exit
```

### Example:

```
Enter choice (1/2/3): 1
Enter student name: Kaps
Enter score for subject 1 (0-100): 80
Enter score for subject 2 (0-100): 90
Enter score for subject 3 (0-100): 70
✅ Alice added with average 80.00 and grade A.
```

Then view the report:

```
Enter choice (1/2/3): 2
Student Report
------------------
Kaps: Scores=[80, 90, 70] | Avg=80.00 | Grade=A
```

---

## What I Learned

* How to organize code using **functions**
* How to handle **variable arguments** with `*args`
* The difference between **local and global scope**
* How to use loops and conditionals for **menu-driven programs**
* String formatting with **f-strings** and `.join()`
* Why **validation** is important for user input

---

## Possible Improvements

* Allow any number of subjects (not fixed to 3)
* Edit or delete a student
* Find the best/worst student automatically
* Save and load student data from a file
