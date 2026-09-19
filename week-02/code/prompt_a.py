students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 64,
    "Emma": 78
}

marks = list(students.values())

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)
passed = sum(mark >= 50 for mark in marks)

print("Student Marks Analysis")
print("----------------------")

for name, mark in students.items():
    print(f"{name}: {mark}")

print(f"\nAverage mark: {average:.2f}")
print(f"Highest mark: {highest}")
print(f"Lowest mark: {lowest}")
print(f"Students passed: {passed}/{len(students)}")