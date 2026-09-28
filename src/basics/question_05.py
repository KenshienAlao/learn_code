"""
Question 05: Multiple Assignment and divmod()

Input:  a = 7, b = 3, total_seconds = 3725
Output: a = 7, b = 3
        divmod(7, 3) -> quotient = 2, remainder = 1
        a, b = b, a  ->  a = 3, b = 7
        divmod(3725, 3600)  ->  hours = 1, remainder = 125
        divmod(125, 60)  ->  minutes = 2, seconds = 5

Tip: divmod() gives you the quotient and the remainder together, ready to unpack into two names.
"""


def main() -> None:
    print("=" * 50)
    print("Question 05: Multiple Assignment and divmod()")
    print("=" * 50)

    a = 7
    b = 3
    total_seconds = 3725

    # --- STARTER ---
    # Step 1: print(f"a = {a}, b = {b}")
    # Step 2: quotient, remainder = divmod(a, b)
    #         7 divided by 3 is 2 with 1 left over, so print
    #         divmod(7, 3) -> quotient = 2, remainder = 1
    # Step 3: a, b = b, a   then print a = 3, b = 7
    # Step 4: hours, rest = divmod(total_seconds, 3600)  gives (1, 125)
    # Step 5: minutes, seconds = divmod(rest, 60)  gives (2, 5)
    # One statement, two variables. The right side is built first, then unpacked
    # left to right, which is exactly why a, b = b, a needs no temporary variable.

    # --- SOLUTION ---
    print(f"a = {a}, b = {b}")

    quotient, remainder = divmod(a, b)
    print(f"divmod({a}, {b}) -> quotient = {quotient}, remainder = {remainder}")

    a, b = b, a
    print(f"a, b = b, a  ->  a = {a}, b = {b}")

    hours, rest = divmod(total_seconds, 3600)
    minutes, seconds = divmod(rest, 60)
    print(f"divmod({total_seconds}, 3600)  ->  hours = {hours}, remainder = {rest}")
    print(f"divmod({rest}, 60)  ->  minutes = {minutes}, seconds = {seconds}")


if __name__ == "__main__":
    main()
