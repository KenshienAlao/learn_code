"""
Question 04: Remove Consecutive Duplicates

Input:  the list ["A", "A", "B", "B", "B", "C", "A"]
Output: ['A', 'B', 'C', 'A']
Tip:  Keep a previous variable seeded with the first element, then compare each later item to previous and update previous every single pass, hit or miss.
"""


def main() -> None:
    print("=" * 50)
    print("Question 04: Remove Consecutive Duplicates")
    print("=" * 50)

    items = ["A", "A", "B", "B", "B", "C", "A"]
    result = []
    previous = ""
    runs = 1

    # --- STARTER ---
    # The idea is to track the previous element and compare each subsequent
    # item against it. Same concept here, except a Python list is not drained:
    #   1. seed previous = items[0] and result = [items[0]]
    #   2. loop with: for item in items[1:]:
    #   3. if item != previous, result.append(item) and runs = runs + 1
    #   4. always set previous = item, even when the item was a duplicate
    #   5. print result, and note that the last "A" survives because it is
    #      not next to another "A", so this is not a unique-values set
    # Expected result: ['A', 'B', 'C', 'A']

    # --- SOLUTION ---
    previous = items[0]
    result.append(previous)

    for item in items[1:]:
        if item != previous:
            result.append(item)
            runs = runs + 1
        # previous tracks the last item seen, not the last item kept.
        previous = item

    print("Original: " + str(items))
    print("Runs of identical letters: " + str(runs))
    print("Result: " + str(result))
    print("Original after: " + str(items))


if __name__ == "__main__":
    main()
