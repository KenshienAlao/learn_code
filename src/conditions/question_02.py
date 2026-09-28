"""
Question 02: Grade Calculator Using if / elif / else

Input:  85
Output: Score: 85
        Grade: B
        Result: PASS (a score of 60 or higher is a pass)

Tip: Build an if / elif / else ladder. The bands are 90-100 A, 80-89 B,
     70-79 C, 60-69 D and 0-59 F. The first matching branch wins, so start
     from the highest band and work downwards.
"""


def main() -> None:
    print("=" * 50)
    print("Question 02: Grade Calculator Using if / elif / else")
    print("=" * 50)

    score = 85

    # --- STARTER ---
    # Store a score in a variable, for example 85.
    # Write an if / elif / else ladder that assigns a letter to a variable.
    # Bands: 90+ is A, 80+ is B, 70+ is C, 60+ is D, everything else is F.
    # Check from the top down, because the first matching branch wins.
    # Then build a pass or fail note with a conditional expression.
    # Expected result for 85: Grade B, Result PASS.

    # --- SOLUTION ---
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    result = "PASS" if score >= 60 else "FAIL"

    print(f"Score: {score}")
    print(f"Grade: {grade}")
    print(f"Result: {result} (a score of 60 or higher is a pass)")


if __name__ == "__main__":
    main()
