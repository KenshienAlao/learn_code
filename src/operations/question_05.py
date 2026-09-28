"""
Question 05: Chained Comparison to Check an Age Range

Input:  ages = 20, 12, 70
Output: 20: In range (18 to 65)
        12: Too young
        70: Too old

Tip: Python lets you write 18 <= age <= 65 as one expression, and it means
    18 <= age and age <= 65.
"""


def main() -> None:
    print("=" * 50)
    print("Question 05: Chained Comparison to Check an Age Range")
    print("=" * 50)

    ages = 20, 12, 70
    min_age, max_age = 18, 65

    # --- STARTER ---
    # The check is 18 <= age <= 65.
    # Step 1: loop through the ages with a plain for loop.
    # Step 2: if the chained comparison is True print In range (18 to 65).
    # Step 3: use an elif for the too young case, and a plain else for too old.
    # Expected: 20 In range, 12 Too young, 70 Too old.

    # --- SOLUTION ---
    for age in ages:
        # Step 2: the chained comparison 18 <= age <= 65 is the same as
        # 18 <= age and age <= 65.
        if min_age <= age <= max_age:
            print(f"{age}: In range ({min_age} to {max_age})")
        # Step 3: elif only runs when the if above was False.
        elif age < min_age:
            print(f"{age}: Too young")
        else:
            print(f"{age}: Too old")

    # The explicit version works in Python too, it is just longer.
    print("-" * 50)
    print("Same check written with 'and':")
    for age in ages:
        if age >= min_age and age <= max_age:
            print(f"{age}: In range ({min_age} to {max_age})")
        elif age < min_age:
            print(f"{age}: Too young")
        else:
            print(f"{age}: Too old")
    print("=" * 50)


if __name__ == "__main__":
    main()
