"""
Question 02: Insert at the Start and Show the Shifting

Input:  items = ["Samsung", "Xiaomi", "iPhone"], then items.insert(0, "Nokia")
Output: Before: ['Samsung', 'Xiaomi', 'iPhone']
            0  Samsung
            1  Xiaomi
            2  iPhone
            3  <empty>
        Shifting every element one slot to the right:
            0  Samsung  ->  1
            1  Xiaomi  ->  2
            2  iPhone  ->  3
        After:  ['Nokia', 'Samsung', 'Xiaomi', 'iPhone']
            0  Nokia
            1  Samsung
            2  Xiaomi
            3  iPhone
            4  <empty>
        insert(0, data) is O(n) because every element shifted one slot to the right.

Tip: Print the index grid before and after, and use a while loop on the index to show each
     element moving up by one position.
"""

# The shifting is not something we write by hand in Python; insert(0, data) does it
# internally. Printing the grid before and after makes that invisible work visible.


def print_grid(values) -> None:
    # Print one row showing every index next to the element sitting in it.
    index = 0
    while index < len(values):
        print(f"    {index}  {values[index]}")
        index = index + 1
    # Show the first free slot so the empty space is visible too.
    print(f"    {len(values)}  <empty>")


def main() -> None:
    print("=" * 50)
    print("Question 02: Insert at the Start and Show the Shifting")
    print("=" * 50)

    # --- variables ---
    items = ["Samsung", "Xiaomi", "iPhone"]
    new_item = "Nokia"

    # --- STARTER ---
    # Print the list and an index grid before the insert.
    # Call items.insert(0, new_item), then print the list and grid again.
    # Point out that the insert cost O(n) because everything shifted right by one.

    # --- SOLUTION ---
    # --- Before ---
    print(f"Before: {items}")
    print_grid(items)
    print("Shifting every element one slot to the right:")

    # Walk the old list and show where each element is about to end up.
    index = 0
    while index < len(items):
        print(f"    {index}  {items[index]}  ->  {index + 1}")
        index = index + 1

    # The one call that performs all of the shifting.
    items.insert(0, new_item)

    # --- After ---
    print(f"After:  {items}")
    print_grid(items)

    # State the cost honestly: one line of code, but n slots moved.
    print("insert(0, data) is O(n) because every element shifted one slot to the right.")


if __name__ == "__main__":
    main()
