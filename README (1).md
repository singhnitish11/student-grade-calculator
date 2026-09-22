
# Student Grade Calculator

## About the Project

This is my **Week 2 Python hands-on project**.

In this project, I created a simple Student Grade Calculator using Python.
The program asks for the student's name and marks and then calculates the grade.

I made this project while practicing Python concepts like conditions, functions, loops, and input validation.

## What I Practiced

While making this project, I practiced:

* Taking input from the user
* Using variables
* Using `if-elif-else`
* Creating and calling a function
* Using a `while` loop
* Checking valid and invalid marks
* Testing the program with different inputs
* Displaying the final result

## How the Program Works

First, the program asks for:

```text
Student Name
Marks
```

Then it checks whether the marks are between **0 and 100**.

If the marks are valid, the program calculates the grade.

If the marks are invalid, it shows an error message and asks for the marks again.

## Grading Logic

| Marks    | Grade |
| -------- | ----- |
| 90 - 100 | A     |
| 80 - 89  | B     |
| 70 - 79  | C     |
| 60 - 69  | D     |
| Below 60 | F     |

## Input Validation

I also added validation so that marks outside the range of **0 to 100** are not accepted.

For example:

```text
Enter marks (0-100): 105

Invalid marks! Please enter marks between 0 and 100.
```

The program then asks for the marks again.

## Function Used

I created a function called:

```python
calculate_grade(marks)
```

This function checks the marks using `if-elif-else` and returns the appropriate grade.

## Testing

I tested the program with different marks.

### Test 1

```text
Student Name: Nitish
Marks: 95
Grade: A
```

### Test 2

```text
Student Name: Rahul
Marks: 85
Grade: B
```

### Test 3

```text
Student Name: Aman
Marks: 75
Grade: C
```

### Test 4

```text
Student Name: Ravi
Marks: 65
Grade: D
```

### Test 5

```text
Student Name: Karan
Marks: 45
Grade: F
```

### Invalid Input Test

```text
Marks: 105

Invalid marks! Please enter marks between 0 and 100.
```

More test cases are available in `test_cases.txt`.

## Screenshot

I have added screenshots of my program execution in the `screenshots` folder.

The screenshots show:

* Normal grade calculation
* Invalid marks validation
* Final program output

## Project Files

```text
Week-2-Student-Grade-Calculator/
│
├── README.md
├── grade_calculator.py
├── test_cases.txt
│
└── screenshots/
    ├── normal-output.png
    ├── validation-test.png
    ├── test-cases-output.png
    └── code-and-output.png
```

## How to Run

If Python is installed, run:

```bash
python grade_calculator.py
```

The program will ask for the student's name and marks.

## What I Learned

After completing this hands-on task, I understood better how to use:

* `input()`
* Variables
* `if-elif-else`
* Functions
* `while` loop
* Input validation
* Basic testing

This project helped me practice combining these Python concepts into one small working program.

## Submission Checklist

* [x] README.md
* [x] grade_calculator.py
* [x] test_cases.txt
* [x] screenshots folder
* [x] Valid marks tested
* [x] Invalid marks tested
* [x] Grade calculation tested

---

**Week 2 Python Hands-on Project**
**Project:** Student Grade Calculator



