"""
Question 02: Remove Odd Numbers

Input:  the list [1, 2, 3, 4, 5, 6]
Output: [2, 4, 6]
Tip:  Build a brand new list called even and append to it only when number % 2 == 0, instead of deleting from the list you are looping over.
"""


def main() -> None:
    print("=" * 50)
    print("Question 02: Remove Odd Numbers")
    print("=" * 50)

    items = [1, 2, 3, 4, 5, 6]
    even = []
    dropped = []

    # --- STARTER ---
    # Python lists have no removeIf, and deleting inside a for loop would
    # skip elements, so build a new list instead:
    #   1. start even = [] and dropped = []
    #   2. loop with: for number in items:
    #   3. if number % 2 == 0, even.append(number), otherwise dropped.append(number)
    #   4. print even, then print items again to show the original is untouched
    # Expected result: [2, 4, 6]

    # --- SOLUTION ---
    for number in items:
        if number % 2 == 0:
            even.append(number)
        else:
            dropped.append(number)

    print("Original: " + str(items))
    print("Dropped as odd: " + str(dropped))
    print("Kept as even: " + str(even))
    print("Original after: " + str(items))


if __name__ == "__main__":
    main()
