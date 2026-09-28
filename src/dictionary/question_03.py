"""
Question 03: Merge Two Dictionaries

Input:  a = {"x": 1, "y": 2} and b = {"y": 20, "z": 3}
Output: Method 1 (for key in b): {'x': 1, 'y': 20, 'z': 3}
        Method 2 (a.update(b)): {'x': 1, 'y': 20, 'z': 3}
        The shared key 'y' is 20, not 2 + 20. Merging overwrites.
Tip:  Merging overwrites, it does not add, so the shared key "y" ends up as 20 and not 2 + 20.
"""


def main() -> None:
    print("=" * 50)
    print("Question 03: Merge Two Dictionaries")
    print("=" * 50)

    a = {"x": 1, "y": 2}
    b = {"y": 20, "z": 3}

    # --- STARTER ---
    # Copy everything from b into a, twice, using two different styles.
    # 1. Loop over b with for key in b: and assign a[key] = b[key].
    # 2. Do it again in one line with a.update(b).
    # Both give the same result. The shared key "y" is OVERWRITTEN with 20, not added to.
    # Print the dict after each method so you can see that the answer matches.
    # Expected result: {'x': 1, 'y': 20, 'z': 3} both times.

    # --- SOLUTION ---
    # Method 1: the explicit loop, useful when you want to inspect or change each key.
    for key in b:
        a[key] = b[key]
    print("Method 1 (for key in b):", a)

    # Method 2: the one-liner. update() copies every key from b into a.
    # a is already merged here, so merging again just lands on the same dict.
    a.update(b)
    print("Method 2 (a.update(b)):", a)

    # Why 20 and not 22? Because assignment replaces the old value.
    # Both "y" keys point at the same name, so the second write wins.
    print("The shared key 'y' is 20, not 2 + 20. Merging overwrites.")


if __name__ == "__main__":
    main()
