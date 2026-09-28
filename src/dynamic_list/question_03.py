"""
Question 03: Delete an Element and Show the Shifting

Input:  items = ["Lemon", "Banana", "Apple", "Grapes"], then items.pop(0)
Output: Before: ['Lemon', 'Banana', 'Apple', 'Grapes']
            0  Lemon
            1  Banana
            2  Apple
            3  Grapes
            4  <empty>
        Shifting every remaining element one slot to the left:
            1  Banana  ->  0
            2  Apple  ->  1
            3  Grapes  ->  2
        Removed: Lemon
        After:  ['Banana', 'Apple', 'Grapes']
            0  Banana
            1  Apple
            2  Grapes
            3  <empty>
        pop(0) is O(n) because the shift touches every remaining element.
        pop() from the end is O(1) because nothing has to move.
        del items[0] does the same job as pop(0) but throws the value away.

Tip: Print the index grid before and after, and use a while loop on the index to show the
     left shift that closes the gap left by the removed element.
"""

# pop(0) and del items[0] both close the gap on purpose: a list keeps no holes, so the
# element after the removed one slides down into its place.


def print_grid(values) -> None:
    # Print one row per index, then show the first free slot at the end.
    index = 0
    while index < len(values):
        print(f"    {index}  {values[index]}")
        index = index + 1
    print(f"    {len(values)}  <empty>")


def main() -> None:
    print("=" * 50)
    print("Question 03: Delete an Element and Show the Shifting")
    print("=" * 50)

    # --- variables ---
    items = ["Lemon", "Banana", "Apple", "Grapes"]

    # --- STARTER ---
    # Print the list and an index grid before the delete.
    # Call items.pop(0) to remove the first element, then print the list and grid again.
    # Compare the cost of removing from the front with removing from the back.

    # --- SOLUTION ---
    # --- Before ---
    print(f"Before: {items}")
    print_grid(items)
    print("Shifting every remaining element one slot to the left:")

    # Walk from index 1 upward to show where each survivor is about to land.
    index = 1
    while index < len(items):
        print(f"    {index}  {items[index]}  ->  {index - 1}")
        index = index + 1

    # pop(0) returns the value it removed, so we can show which element left.
    removed = items.pop(0)
    print(f"Removed: {removed}")

    # --- After ---
    print(f"After:  {items}")
    print_grid(items)

    # Compare the two ends of the list.
    print("pop(0) is O(n) because the shift touches every remaining element.")
    print("pop() from the end is O(1) because nothing has to move.")
    print("del items[0] does the same job as pop(0) but throws the value away.")


if __name__ == "__main__":
    main()
