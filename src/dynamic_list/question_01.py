"""
Question 01: Show Size vs Capacity While Appending

Input:  values = [10, 20, 30, 40, 50, 60]
Output: size 1, capacity 4
        size 2, capacity 4
        size 3, capacity 4
        size 4, capacity 4 -> ARRAY IS FULL, capacity would double to 8
        size 5, capacity 8
        size 6, capacity 8

Tip: Track size and capacity in a for loop and double your capacity variable the moment
     size catches up to it.
"""

# NOTE: a real Python list has no capacity you can read. Python hides the room it reserved
# inside the object and manages the resizing for you. The `capacity` variable below is
# imaginary bookkeeping that we maintain by hand so the size-vs-capacity idea stays visible.


def main() -> None:
    print("=" * 50)
    print("Question 01: Show Size vs Capacity While Appending")
    print("=" * 50)

    # --- variables ---
    items = []
    capacity = 4
    values = [10, 20, 30, 40, 50, 60]

    # --- STARTER ---
    # Start with an empty list and a capacity of 4 that you track yourself.
    # Loop over `values` and append one at a time.
    # After every append print the size and the capacity, and when they become equal,
    # print that the array is full and the capacity would double to 8.

    # --- SOLUTION ---
    # Append each value, one per iteration.
    for value in values:
        items.append(value)
        size = len(items)

        # Check whether the imaginary capacity has been used up.
        if size == capacity:
            print(f"size {size}, capacity {capacity} -> ARRAY IS FULL, capacity would double to {capacity * 2}")
            # Simulate the resize that a real dynamic array performs internally.
            capacity = capacity * 2
        else:
            print(f"size {size}, capacity {capacity}")


if __name__ == "__main__":
    main()
