"""
Question 05: Implement a Mini DynamicArray Class with grow()

Input:  six values added to a DynamicArray created with capacity 4
Output: start: capacity 4, size 0
        is_empty() -> True
        added "Samsung" -> [Samsung]
            capacity 4, size 1
        added "Xiaomi" -> [Samsung, Xiaomi]
            capacity 4, size 2
        added "iPhone" -> [Samsung, Xiaomi, iPhone]
            capacity 4, size 3
        added "Nokia" -> [Samsung, Xiaomi, iPhone, Nokia]
            capacity 4, size 4
        added "OnePlus" -> [Samsung, Xiaomi, iPhone, Nokia, OnePlus]
            capacity 8, size 5
        added "Pixel" -> [Samsung, Xiaomi, iPhone, Nokia, OnePlus, Pixel]
            capacity 8, size 6
        pop_last() -> Pixel
        after pop_last: [Samsung, Xiaomi, iPhone, Nokia, OnePlus]
        is_empty() -> False

Tip: Track the used slots in a while loop inside grow() and copy each element across with
     a for loop, then point self.array at the new list.
"""

# This DynamicArray class demonstrates the grow() pattern with the bug fixed.
# The buggy logic would be: grow() {size = size * 2;}
# That doubles SIZE instead of CAPACITY and never copies the old elements anywhere,
# so enlarging the structure would have lost the data. See grow() below for the fix.


class DynamicArray:
    # Build the empty array with a starting capacity. The slots start as None because
    # Python has no null, and a list can hold a mix of types in one array.
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    # Add to the end. Check the room first, then store the value and count it.
    def add(self, data):
        if self.size >= self.capacity:
            self.grow()
        self.array[self.size] = data
        self.size = self.size + 1

    # Make more room when full: double the capacity, copy the live elements into a new
    # list, then adopt it. This is the line the buggy version got wrong.
    def grow(self):
        self.capacity = self.capacity * 2
        new_array = [None] * self.capacity
        for i in range(self.size):          # copy only the slots that hold real data
            new_array[i] = self.array[i]
        self.array = new_array

    # Insert anywhere. Walk from the end backwards so no value gets overwritten first.
    def insert(self, index, data):
        if self.size >= self.capacity:
            self.grow()
        i = self.size
        while i > index:
            self.array[i] = self.array[i - 1]
            i = i - 1
        self.array[index] = data
        self.size = self.size + 1

    # Remove the last element. Nothing shifts, so this is O(1).
    def pop_last(self):
        value = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size = self.size - 1
        return value

    # An empty array is just the case where no slot holds data yet.
    def is_empty(self):
        return self.size == 0

    # Show only the filled slots, not the empty ones.
    def __str__(self):
        parts = []
        for i in range(self.size):
            parts.append(str(self.array[i]))
        return "[" + ", ".join(parts) + "]"


def main() -> None:
    print("=" * 50)
    print("Question 05: Implement a Mini DynamicArray Class with grow()")
    print("=" * 50)

    # --- variables ---
    values = ["Samsung", "Xiaomi", "iPhone", "Nokia", "OnePlus", "Pixel"]
    data = DynamicArray(4)

    # --- STARTER ---
    # Write a class with capacity, array, and size. Call grow() from add() when full.
    # In main, add six values and print the capacity after each one so the doubling
    # from 4 to 8 is visible.

    # --- SOLUTION ---
    print(f"start: capacity {data.capacity}, size {data.size}")
    print(f"is_empty() -> {data.is_empty()}")

    # Add the six values one at a time and watch the capacity change at the fifth add.
    for value in values:
        data.add(value)
        # Capacity becomes 8 after the fourth add, which means grow() did its job.
        print(f'added "{value}" -> {str(data)}')
        print(f"    capacity {data.capacity}, size {data.size}")

    # Prove the class still works the way the original did.
    print(f"pop_last() -> {data.pop_last()}")
    print(f"after pop_last: {data}")
    print(f"is_empty() -> {data.is_empty()}")


if __name__ == "__main__":
    main()
