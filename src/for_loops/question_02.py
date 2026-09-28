"""
Question 02: Sum All Numbers in a List

Input:  [10, 20, 30, 40, 50]
Output: Sum of the list: 150
Tip:  Start a running total at 0, add every value inside the for loop, then print the total after the loop.
"""


def main() -> None:
    print("=" * 50)
    print("Question 02: Sum All Numbers in a List")
    print("=" * 50)

    numbers = [10, 20, 30, 40, 50]
    total = 0

    # --- STARTER ---
    # Loop over every value in the list and add it to total.
    # total already starts at 0 for you, so inside the loop just do total += value.
    # Do not use sum(), the point is to write the loop yourself.
    # Print the answer as: print("Sum of the list:", total)
    # Expected result: Sum of the list: 150

    # --- SOLUTION ---
    for value in numbers:
        total += value

    print("Sum of the list:", total)


if __name__ == "__main__":
    main()
