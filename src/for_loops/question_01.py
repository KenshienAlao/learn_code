"""
Question 01: Print Numbers Using range(1, 11)

Input:  range(1, 11)
Output: 1
        2
        3
        4
        5
        6
        7
        8
        9
        10
Tip:  range(1, 11) starts at 1 and stops BEFORE 11, so 10 is the last number.
"""


def main() -> None:
    print("=" * 50)
    print("Question 01: Print Numbers Using range(1, 11)")
    print("=" * 50)

    start, stop = 1, 11

    # --- STARTER ---
    # Write a for loop that prints every number in the range, one per line.
    # Use: for i in range(start, stop):
    # Remember the stop is exclusive, so this prints 1 through 10, not 1 through 11.
    # Expected result: the numbers 1 to 10, each on its own line.

    # --- SOLUTION ---
    for i in range(start, stop):
        print(i)


if __name__ == "__main__":
    main()
