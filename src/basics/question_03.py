"""
Question 03: Convert Seconds Into Hours, Minutes and Seconds

Input:  total_seconds = 3725
Output: 3725 seconds is 1 hours, 2 minutes, 5 seconds

Tip: divmod(total, 3600) hands you back the hours and what is left over in one go.
"""


def main() -> None:
    print("=" * 50)
    print("Question 03: Convert Seconds Into Hours, Minutes and Seconds")
    print("=" * 50)

    total_seconds = 3725

    # --- STARTER ---
    # 3725 / 3600 is 1 hour and 125 seconds left over.
    # 125 / 60 is 2 minutes and 5 seconds left over.
    # Step 1: hours, remainder = divmod(total_seconds, 3600)
    # Step 2: minutes, seconds = divmod(remainder, 60)
    # Step 3: print one f-string that reads exactly:
    #         3725 seconds is 1 hours, 2 minutes, 5 seconds
    # divmod() returns a pair, so you unpack it straight into two names.
    # 3725 = 3600 + 125, and 125 = 120 + 5.

    # --- SOLUTION ---
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"{total_seconds} seconds is {hours} hours, {minutes} minutes, {seconds} seconds")


if __name__ == "__main__":
    main()
