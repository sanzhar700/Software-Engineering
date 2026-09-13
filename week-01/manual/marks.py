marks = input("Enter marks separated by commas: ").split(",")

valid = []

for mark in marks:
    try:
        mark = float(mark)
        if 0 <= mark <= 100:
            valid.append(mark)
    except:
        continue

if not valid:
    print("No valid marks")
else:
    print("Number of valid marks:", len(valid))
    print("Average:", f"{sum(valid) / len(valid):.2f}")
    print("Highest:", max(valid))
    print("Lowest:", min(valid))

    passed = 0
    for mark in valid:
        if mark >= 50:
            passed += 1

    print("Pass rate:", f"{passed / len(valid) * 100:.1f}%")