"""
Question 01: Odd or Even

Input:  7, 8
Output: 7 is Odd
        8 is Even

Tip: Use the modulo operator %. When the remainder is 0 the number is even,
     anything else makes it odd.
"""


def main() -> None:
    print("=" * 50)
    print("Question 01: Odd or Even")
    print("=" * 50)

    num_1, num_2 = 7, 8

    # --- STARTER ---
    # Declare two numbers, for example 7 and 8.
    # Write an if / else that checks each number with the modulo operator.
    # Remember: num % 2 == 0 means even, anything else means odd.
    # Print one line per number, like "7 is Odd".
    # Expected result: 7 is Odd, then 8 is Even.

    # --- SOLUTION ---
    for num in (num_1, num_2):
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")


if __name__ == "__main__":
    main()
