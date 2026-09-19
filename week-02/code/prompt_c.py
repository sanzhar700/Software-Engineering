def analyze_marks(marks, pass_mark=50):
    if not marks:
        raise ValueError("marks cannot be empty")

    for mark in marks:
        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            raise ValueError("all marks must be numeric")
        if mark < 0 or mark > 100:
            raise ValueError("marks must be between 0 and 100")

    if not isinstance(pass_mark, (int, float)) or isinstance(pass_mark, bool):
        raise ValueError("pass_mark must be numeric")
    if pass_mark < 0 or pass_mark > 100:
        raise ValueError("pass_mark must be between 0 and 100")

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    pass_rate = sum(mark >= pass_mark for mark in marks) / len(marks) * 100

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "pass_rate": round(pass_rate, 2)
    }


# Tests

# 1. Normal case
assert analyze_marks([40, 60, 80], 50) == {
    "average": 60.0,
    "highest": 80,
    "lowest": 40,
    "pass_rate": 66.67
}

# 2. One mark
assert analyze_marks([75]) == {
    "average": 75.0,
    "highest": 75,
    "lowest": 75,
    "pass_rate": 100.0
}

# 3. Decimals
result = analyze_marks([50.5, 60.5, 70.5])
assert result["average"] == 60.5
assert result["highest"] == 70.5
assert result["lowest"] == 50.5
assert result["pass_rate"] == 100.0

# 4. Custom pass_mark
assert analyze_marks([40, 60, 80], 70)["pass_rate"] == 33.33

# 5. Empty list
try:
    analyze_marks([])
    assert False
except ValueError:
    pass

# 6. Text value
try:
    analyze_marks([40, "60", 80])
    assert False
except ValueError:
    pass

# 7. Mark below 0
try:
    analyze_marks([-10, 50, 80])
    assert False
except ValueError:
    pass

# 8. Mark above 100
try:
    analyze_marks([50, 80, 101])
    assert False
except ValueError:
    pass

print("All tests passed!")