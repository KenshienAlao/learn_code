"""
Question 03: Remove Every Second Element

Input:  the list ["A", "B", "C", "D", "E", "F"]
Output: ['A', 'C', 'E']
Tip:  Loop over the indexes with for index in range(len(items)) and append to a new list only when index % 2 == 0, which keeps positions 0, 2 and 4.
"""


def main() -> None:
    print("=" * 50)
    print("Question 03: Remove Every Second Element")
    print("=" * 50)

    items = ["A", "B", "C", "D", "E", "F"]
    kept = []
    kept_positions = []
    dropped_positions = []

    # --- STARTER ---
    # On a Python list, deleting inside a loop over that same list makes the
    # remaining items slide left and the next index skips one, so letters get
    # dropped by accident. Build a new list instead:
    #   1. loop with: for index in range(len(items)):
    #   2. if index % 2 == 0, kept.append(items[index]) and record the index
    #   3. otherwise record the index as dropped, so the trace is visible
    # Expected result: ['A', 'C', 'E']

    # --- SOLUTION ---
    for index in range(len(items)):
        if index % 2 == 0:
            kept.append(items[index])
            kept_positions.append(index)
        else:
            dropped_positions.append(index)

    print("Original: " + str(items))
    print("Kept positions: " + str(kept_positions))
    print("Dropped positions: " + str(dropped_positions))
    print("Kept letters: " + str(kept))
    print("Original after: " + str(items))


if __name__ == "__main__":
    main()
