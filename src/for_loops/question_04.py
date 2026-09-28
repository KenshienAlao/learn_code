"""
Question 04: Reverse a List Without Using reverse()

Input:  ["a", "b", "c", "d"]
Output: Reversed list: ['d', 'c', 'b', 'a']
Tip:  Walk the indexes from the last one down to the first, and .append() each value onto a new list.
"""


def main() -> None:
    print("=" * 50)
    print("Question 04: Reverse a List Without Using reverse()")
    print("=" * 50)

    items = ["a", "b", "c", "d"]
    reversed_items = []

    # --- STARTER ---
    # Do NOT call items.reverse(), and do not use items[::-1] or reversed().
    # Build the new list yourself, one value at a time, starting from the end.
    # Hint: range(len(items) - 1, -1, -1) counts the indexes backwards: 3, 2, 1, 0.
    # Inside the loop, add items[i] to the new list with reversed_items.append(items[i]).
    # Print the answer as: print("Reversed list:", reversed_items)
    # Expected result: Reversed list: ['d', 'c', 'b', 'a']

    # --- SOLUTION ---
    for i in range(len(items) - 1, -1, -1):
        reversed_items.append(items[i])

    print("Reversed list:", reversed_items)


if __name__ == "__main__":
    main()
