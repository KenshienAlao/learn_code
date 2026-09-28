"""
Question 02: Swap Two Variables Without a Temporary Variable

Input:  a = 5, b = 9
Output: Before: a = 5, b = 9
        After (tuple swap): a = 9, b = 5
        After (temp swap): a = 5, b = 9

Tip: a, b = b, a does the whole swap in one line. Try it, then undo it using a temporary variable.
"""


def main() -> None:
    print("=" * 50)
    print("Question 02: Swap Two Variables Without a Temporary Variable")
    print("=" * 50)

    a = 5
    b = 9

    # --- STARTER ---
    # Print the starting values, then swap a and b, then print them again.
    # Step 1: print(f"Before: a = {a}, b = {b}")
    # Step 2: use the one-line tuple swap, a, b = b, a
    # Step 3: print(f"After (tuple swap): a = {a}, b = {b}")
    # Step 4: swap them BACK using the classic temporary variable, so the file
#         ends where it started. The classic temporary variable swap works
#         because Python evaluates the right side first and then unpacks it,
#         so both values are ready before either is written.

    # --- SOLUTION ---
    print(f"Before: a = {a}, b = {b}")

    a, b = b, a
    print(f"After (tuple swap): a = {a}, b = {b}")

    temp = a
    a = b
    b = temp
    print(f"After (temp swap): a = {a}, b = {b}")


if __name__ == "__main__":
    main()
