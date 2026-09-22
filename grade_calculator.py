
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")

while True:
    marks = float(input("Enter marks (0-100): "))

    if 0 <= marks <= 100:
        break
    else:
        print("Invalid marks! Please enter marks between 0 and 100.")

grade = calculate_grade(marks)

print("\n--- Student Result ---")
print("Student Name:", name)
print("Marks:", marks)
print("Grade:", grade)
