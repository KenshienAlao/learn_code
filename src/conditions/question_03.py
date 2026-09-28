"""
Question 03: Leap Year Using and / or

Input:  2024, 1900
Output: 2024 is a leap year
        1900 is not a leap year

Tip: A leap year is divisible by 4 AND (NOT divisible by 100 OR divisible
     by 400). Python uses the words and, or and not, and and / or short
     circuit just like Python's and and or do.
"""


def main() -> None:
    print("=" * 50)
    print("Question 03: Leap Year Using and / or")
    print("=" * 50)

    year_1, year_2 = 2024, 1900

    # --- STARTER ---
    # Store two years in variables, for example 2024 and 1900.
    # Build one boolean that says whether a year is a leap year.
    # The rule is: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0).
    # Use the words and, or and not, never &&, || or !.
    # Then use if / else to print one line per year.
    # Expected result: 2024 is a leap year, 1900 is not a leap year.

    # --- SOLUTION ---
    for year in (year_1, year_2):
        is_leap = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

        if is_leap:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")


if __name__ == "__main__":
    main()
