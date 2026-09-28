"""
Question 03: Count How Many Times a Value Appears

Input:  [10, 20, 10, 30, 10]  searching for 10
Output: Times 10 appears: 3
Tip:  Keep a counter at 0, then bump it up with count += 1 every time a value matches the target.
"""


def main() -> None:
    print("=" * 50)
    print("Question 03: Count How Many Times a Value Appears")
    print("=" * 50)

    numbers = [10, 20, 10, 30, 10]
    target = 10
    count = 0

    # --- STARTER ---
    # Loop over every value in the list.
    # If a value equals target, add 1 to count using a plain if statement.
    # Do not use numbers.count(target), the point is the loop and the if.
    # Print the answer as: print(f"Times {target} appears: {count}")
    # Expected result: Times 10 appears: 3

    # --- SOLUTION ---
    for value in numbers:
        if value == target:
            count += 1

    print(f"Times {target} appears: {count}")


if __name__ == "__main__":
    main()
