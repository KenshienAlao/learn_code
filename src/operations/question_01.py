"""
Question 01: Area of a Circle Using Power 0.5

Input:  radius = 5, pi = 3.14159
Output: Radius squared (r ** 2)     : 25
        Area (pi * r ** 2)          : 78.53975
        Area rounded to 4 decimals  : 78.5397
        Square with the same area   : 8.8623

Tip: You never need Math.sqrt. In Python the ** operator is the power operator,
    so 9 ** 0.5 is the square root of 9. That means r ** 2 squares the radius
    and x ** 0.5 takes any square root you want, with no import at all.
"""


def main() -> None:
    print("=" * 50)
    print("Question 01: Area of a Circle Using Power 0.5")
    print("=" * 50)

    r = 5
    pi = 3.14159

    # --- STARTER ---
    # The formula is A = pi * r ** 2.
    # Step 1: store r ** 2 in a variable so you can see it on its own.
    # Step 2: multiply that by pi to get the area.
    # Step 3: print the area, then print it again with round(area, 4).
    # Step 4: take the square root of the area using ** 0.5 (NOT math.sqrt)
    #         and round it to 4 decimals as well.
    # Expected: 78.53975, then 78.5397, then 8.8623.

    # --- SOLUTION ---
    # Step 1: ** 2 raises the radius to the power of 2.
    r_squared = r ** 2
    print(f"Radius                      : {r}")
    print(f"Pi value used               : {pi}")
    print(f"Radius squared (r ** 2)     : {r_squared}")

    # Step 2: multiply the squared radius by pi.
    area = pi * r_squared
    print(f"Area (pi * r ** 2)          : {area}")

    # Step 3: round the area so the output is easier to read.
    area_rounded = round(area, 4)
    print(f"Area rounded to 4 decimals  : {area_rounded}")

    # Step 4: ** 0.5 is the square root.
    square_side = round(area ** 0.5, 4)
    print(f"Square with the same area   : {square_side}")
    print("=" * 50)


if __name__ == "__main__":
    main()
