"""
Question 04: Even or Odd Using the Modulo Operator

Input:  numbers = 7, 8, 13, 20
Output: 7 is Odd
        8 is Even
        13 is Odd
        20 is Even

Tip: A number is even when number % 2 == 0. You have to write the == 0 part,
    because any remainder other than zero counts as True in an if, so a
    remainder of 1 would already be treated as True.
"""


def main() -> None:
    print("=" * 50)
    print("Question 04: Even or Odd Using the Modulo Operator")
    print("=" * 50)

    numbers = 7, 8, 13, 20

    # --- STARTER ---
    # The test is: remainder = number % 2, then check remainder == 0.
    # Step 1: loop through the numbers with a plain for loop.
    # Step 2: store number % 2 in a variable called remainder.
    # Step 3: if remainder == 0 print Even, otherwise print Odd.
    # Expected: 7 is Odd, 8 is Even, 13 is Odd, 20 is Even.

    # --- SOLUTION ---
    for number in numbers:
        # Step 2: % gives the remainder after the division.
        remainder = number % 2

        # Step 3: == 0 is required. A remainder of 1 is already truthy,
        # so writing "if remainder:" would be True for every odd number.
        if remainder == 0:
            print(f"{number} is Even")
        else:
            print(f"{number} is Odd")

    print("=" * 50)


if __name__ == "__main__":
    main()
