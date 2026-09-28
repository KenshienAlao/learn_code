"""
Question 04: Positive, Negative or Zero Using a Conditional Expression

Input:  25, -7, 0
Output: 25 is Positive
        -7 is Negative
        0 is Zero

Tip: Use a conditional expression instead of a full if / else. The order is
     The order has the value first and the condition second.
"""


def main() -> None:
    print("=" * 50)
    print("Question 04: Positive, Negative or Zero Using a Conditional Expression")
    print("=" * 50)

    num_1, num_2, num_3 = 25, -7, 0

    # --- STARTER ---
    # Store three numbers in variables, for example 25, -7 and 0.
    # For each number build a label with a conditional expression:
    #     label = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
    # Notice the value comes first and the condition comes second.
    # Then print the number and its label on one f-string line.
    # Expected result: 25 is Positive, -7 is Negative, 0 is Zero.

    # --- SOLUTION ---
    for num in (num_1, num_2, num_3):
        label = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
        print(f"{num} is {label}")


if __name__ == "__main__":
    main()
