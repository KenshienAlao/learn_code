"""
Question 05: Count How Many Times a Value Appears

Input:  [10, 20, 10, 30, 10, 40], search = 10
Output: Count: 3
        Queue is now: []
Tip:  Poll each item, compare it to the search value with ==, and bump a counter on a match.
"""


def main() -> None:
    print("=" * 50)
    print("Question 05: Count How Many Times a Value Appears")
    print("=" * 50)

    queue = [10, 20, 10, 30, 10, 40]
    search = 10
    count = 0

    # --- STARTER ---
    # Start count at 0, it is the score you are keeping.
    # Loop with `while queue:`, pop(0) one item, and compare it to search with ==.
    # If they are equal, add 1 to count. If they are not, do nothing and carry on.
    # Remember == compares values, `is` would compare objects and is not what you want.
    # Expected result: Count: 3, and the queue is empty because polling consumed it,
    # which is fine here since we only wanted the count.

    # --- SOLUTION ---
    while queue:
        # Take one item off the front and compare it against the value we are hunting.
        num = queue.pop(0)
        # == compares the two values, so 10 == 10 is True.
        if num == search:
            count += 1

    print("Count:", count)
    # Every item was polled while searching, so the queue is empty at the end.
    print("Queue is now:", queue)


if __name__ == "__main__":
    main()
