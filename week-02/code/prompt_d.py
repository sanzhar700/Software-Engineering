def analyze_marks(marks, pass_mark=50):
    if not marks:
        raise ValueError("marks cannot be empty")

    for mark in marks:
        if isinstance(mark, bool) or not isinstance(mark, (int, float)):
            raise ValueError("marks must contain only numeric values")
        if mark < 0 or mark > 100:
            raise ValueError("marks must be between 0 and 100")

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    passed = sum(mark >= pass_mark for mark in marks)
    pass_rate = round((passed / len(marks)) * 100, 2)

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "pass_rate": pass_rate
    }


# Tests

# 1. One mark
assert analyze_marks([75]) == {
    "average": 75,
    "highest": 75,
    "lowest": 75,
    "pass_rate": 100.0
}

# 2. Decimal marks
result = analyze_marks([70.5, 80.5, 90.0])
assert result["average"] == 80.33333333333333
assert result["highest"] == 90.0
assert result["lowest"] == 70.5
assert result["pass_rate"] == 100.0

# 3. Custom pass_mark
result = analyze_marks([40, 60, 80], 70)
assert result == {
    "average": 60.0,
    "highest": 80,
    "lowest": 40,
    "pass_rate": 33.33
}

# Example from the task
result = analyze_marks([40, 60, 80], 50)
assert result == {
    "average": 60.0,
    "highest": 80,
    "lowest": 40,
    "pass_rate": 66.67
}

# 4. Empty list
try:
    analyze_marks([])
    assert False
except ValueError:
    pass

# 5. Text value
try:
    analyze_marks([50, "60", 70])
    assert False
except ValueError:
    pass

# 6. Mark below 0
try:
    analyze_marks([-1, 50, 70])
    assert False
except ValueError:
    pass

# 7. Mark above 100
try:
    analyze_marks([50, 101, 70])
    assert False
except ValueError:
    pass

print("All tests passed.")