# Control Flow with Conditional Statements in Python

def classify_score(score):
    # Classify a student's score using if/elif/else.
    if score >= 90:
        grade = "A"
        remark = "Excellent!"
    elif score >= 80:
        grade = "B"
        remark = "Good job!"
    elif score >= 70:
        grade = "C"
        remark = "Not bad."
    elif score >= 60:
        grade = "D"
        remark = "Needs improvement."
    else:
        grade = "F"
        remark = "Please see your instructor."

    return grade, remark

def check_access(age, has_id):
    # Nested conditionals — check if someone can enter a venue.
    if age >= 18:
        if has_id:
            return "Access granted."
        else:
            return "Access denied: ID required."
    else:
        return "Access denied: must be 18 or older."

def describe_number(n):
    # Ternary (inline conditional) expressions.
    parity = "even" if n % 2 == 0 else "odd"
    sign = "positive" if n > 0 else ("negative" if n < 0 else "zero")
    return f"{n} is {sign} and {parity}."

def day_type(day):
    # Match a day name using match/case (Python 3.10+).
    match day.lower():
        case "saturday" | "sunday":
            return f"{day} is a weekend."
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return f"{day} is a weekday."
        case _:
            return f"'{day}' is not a valid day name."

# --- Demo ---
if __name__ == "__main__":
    # if / elif / else
    print("=== Score Classifier ===")
    for score in [95, 83, 74, 61, 45]:
        grade, remark = classify_score(score)
        print(f"  Score {score}: Grade {grade} {remark}")

    # Nested conditionals
    print("\n=== Venue Access ===")
    print(" ", check_access(20, True))
    print(" ", check_access(20, False))
    print(" ", check_access(16, True))

    # Ternary expressions
    print("\n=== Number Descriptions ===")
    for n in [7, -3, 0, 42]:
        print(" ", describe_number(n))

    # match / case
    print("\n=== Day Type ===")
    for day in ["Monday", "Saturday", "Wednesday", "Sunday", "Holiday"]:
        print(" ", day_type(day))
