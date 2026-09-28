"""
Question 05: Merge Two Sorted Lists

Input:  list1 = [5, 1, 3] and list2 = [6, 2, 4]
Output: [1, 2, 3, 4, 5, 6]
Tip:  Sort both copies first, then run the two-pointer merge from merge sort: two index counters, always append the smaller front value, and drain the leftovers at the end.
"""


def main() -> None:
    print("=" * 50)
    print("Question 05: Merge Two Sorted Lists")
    print("=" * 50)

    list1 = [5, 1, 3]
    list2 = [6, 2, 4]
    first = [0]
    second = [0]
    i = 0
    j = 0
    merged = []

    # --- STARTER ---
    # Sort both copies first, then run the two-pointer merge from merge sort:
    #   1. copy the inputs first: first = list1.copy(), second = list2.copy()
    #   2. sort both copies in place using .sort() (inputs are throwaway)
    #   3. while both counters are in range, append the smaller front value
    #      and move only that one counter forward
    #   4. when one list runs out, append whatever is left in the other
    # This is the merge step of merge sort, and it is O(n + m) once sorted.
    # Expected result: [1, 2, 3, 4, 5, 6]

    # --- SOLUTION ---
    first = list1.copy()
    second = list2.copy()
    first.sort()
    second.sort()

    print("Original list1: " + str(list1))
    print("Original list2: " + str(list2))
    print("Sorted copy 1: " + str(first))
    print("Sorted copy 2: " + str(second))

    # Two-pointer merge: only look at the two front values each time.
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged.append(first[i])
            i = i + 1
        else:
            merged.append(second[j])
            j = j + 1

    # One list is empty now, so the rest of the other list is already in order.
    while i < len(first):
        merged.append(first[i])
        i = i + 1

    while j < len(second):
        merged.append(second[j])
        j = j + 1

    print("Merged: " + str(merged))
    print("Original list1 after: " + str(list1))
    print("Original list2 after: " + str(list2))


if __name__ == "__main__":
    main()
