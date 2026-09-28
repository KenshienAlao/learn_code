"""
Question 02: Simple Interest

Input:  principal = 1000, rate = 0.05, time = 2
Output: Simple interest              : 100.0
        Total amount                 : 1100.0
        Interest per year            : 50.0

Tip: The formula is I = P * r * t. Watch the names: you would have
    written P * r * t too, but the point here is that rate is 0.05 and not 5,
    and that the result prints as 100.0 because one of the values is a float.
"""


def main() -> None:
    print("=" * 50)
    print("Question 02: Simple Interest")
    print("=" * 50)

    p_principal, r_rate, t_time = 1000, 0.05, 2

    # --- STARTER ---
    # The formula is I = P * r * t.
    # Step 1: multiply principal * rate first and store it, then multiply by time.
    # Step 2: add the interest back to the principal to get the total amount.
    # Step 3: divide the interest by the time using / to get the interest per year.
    # Expected: 100.0, then 1100.0, then 50.0.

    # --- SOLUTION ---
    # Step 1: interest = P * r * t, done in two steps so you can see the parts.
    principal_times_rate = p_principal * r_rate
    interest = principal_times_rate * t_time
    print(f"Principal                    : {p_principal}")
    print(f"Rate                         : {r_rate}")
    print(f"Time (years)                 : {t_time}")
    print(f"Simple interest              : {interest}")

    # Step 2: total = principal + interest.
    total_amount = p_principal + interest
    print(f"Total amount                 : {total_amount}")

    # Step 3: / always gives a float in Python 3, so 100.0 / 2 gives 50.0.
    interest_per_year = interest / t_time
    print(f"Interest per year            : {interest_per_year}")
    print("=" * 50)


if __name__ == "__main__":
    main()
