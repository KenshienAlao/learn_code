"""
Question 04: Use sys.getsizeof() to Demonstrate List Growth

Input:  a list built by appending the integers 0 to 19, one at a time
Output: empty list: 56 bytes (base object, no slots yet)
        size  1  size 88 bytes   <== RESIZE
        size  2  size 88 bytes
        size  3  size 88 bytes
        size  4  size 88 bytes
        size  5  size 120 bytes   <== RESIZE
        size  6  size 120 bytes
        size  7  size 120 bytes
        size  8  size 120 bytes
        size  9  size 184 bytes   <== RESIZE
        size 10  size 184 bytes
        size 11  size 184 bytes
        size 12  size 184 bytes
        size 13  size 184 bytes
        size 14  size 184 bytes
        size 15  size 184 bytes
        size 16  size 184 bytes
        size 17  size 248 bytes   <== RESIZE
        size 18  size 248 bytes
        size 19  size 248 bytes
        size 20  size 248 bytes
        The byte size stays FLAT for several appends, then JUMPS in one step.
        Those jumps are the resize: a bigger block allocated and the pointers copied in.
        The jumps are not doubles, because Python's list uses a smaller growth factor
        and over-allocates. Let the numbers above speak for themselves.

Tip: Append inside a for loop, remember the previous sys.getsizeof() result, and print a
     marker whenever the new size differs from the one you stored.
"""

# What getsizeof measures: a list is a block of POINTERS to the objects, not the objects
# themselves. So this number tracks the pointer block, and the small integers 0..19 live
# elsewhere entirely and are not counted here. That is why 20 elements cost far fewer than
# 20 x 28 bytes of int.
#
# The base object is 56 bytes on 64-bit CPython, and every extra pointer slot adds 8 bytes.
# That is why all the sizes below are multiples of 8 and why the block grows in 8-byte
# steps: those steps are new pointer slots being added.

import sys


def main() -> None:
    print("=" * 50)
    print("Question 04: Use sys.getsizeof() to Demonstrate List Growth")
    print("=" * 50)

    # --- variables ---
    items = []
    previous_size = 0
    total = 20

    # --- STARTER ---
    # Loop from 0 to 19 and append each integer to the list.
    # After every append, print the size (len) and sys.getsizeof(items).
    # Compare against the size you printed last time. When it changes, mark it as a
    # resize. Watch the flat stretches and the sudden jumps.

    # --- SOLUTION ---
    # Print the base size first so the 56 bytes at the bottom of every number is explained.
    print(f"empty list: {sys.getsizeof([])} bytes (base object, no slots yet)")

    # Append one integer at a time and watch the pointer block grow.
    value = 0
    while value < total:
        items.append(value)
        current_size = sys.getsizeof(items)

        # A different number than last time means the list was reallocated.
        if current_size != previous_size:
            print(f"size {len(items):>2}  size {current_size} bytes   <== RESIZE")
        else:
            print(f"size {len(items):>2}  size {current_size} bytes")

        # Remember this number so the next append can be compared against it.
        previous_size = current_size
        value = value + 1

    # The finding: the size is flat for long stretches, then jumps.
    print("The byte size stays FLAT for several appends, then JUMPS in one step.")
    print("Those jumps are the resize: a bigger block allocated and the pointers copied in.")
    print("The jumps are not doubles, because Python's list uses a smaller growth factor")
    print("and over-allocates. Let the numbers above speak for themselves.")


if __name__ == "__main__":
    main()
