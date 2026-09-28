"""
Question 03: Print Stack Contents Without Destroying It

Input:  stack = ["iPhone", "Tablet", "Samsung", "Xiaomi"]
Output: INITIAL STACK: ['iPhone', 'Tablet', 'Samsung', 'Xiaomi']
        Top
        Xiaomi
        Samsung
        Tablet
        iPhone
        Stack after the empty loop : []
        Temporary list             : ['Xiaomi', 'Samsung', 'Tablet', 'iPhone']
        Restored stack             : ['iPhone', 'Tablet', 'Samsung', 'Xiaomi']
        The stack is unchanged.

Tip: Use a temporary list to store the items as you pop them, then push them
    back so you can put the original stack back exactly as it was.
"""


def main() -> None:
    print("=" * 50)
    print("Question 03: Print Stack Contents Without Destroying It")
    print("=" * 50)

    stack = ["iPhone", "Tablet", "Samsung", "Xiaomi"]
    temporary = []

    # --- STARTER ---
    # A stack only lets you look at the top, so to print every item top first
    # you have to empty it. Emptying it destroys it, so empty it into a
    # temporary list and then pour the temporary list back in.
    # Step 1: while the stack is not empty, pop an item, print it, and append
    #         it to the temporary list.
    # Step 2: while the temporary list is not empty, pop from it and push that
    #         item back onto the stack.
    # Step 3: print the stack again. It must match the INITIAL STACK line.
    # Expected top first order: Xiaomi, Samsung, Tablet, iPhone

    # --- SOLUTION ---
    # The bottom of a Python list is index 0, the top is the last index.
    print(f"INITIAL STACK: {stack}")

    # Step 1: pop everything, printing as we go. The guard is what stops the
    # loop at the bottom:
    print("Top")
    while stack:
        item = stack.pop()
        print(item)
        temporary.append(item)

    # The original stack is gone at this point, but nothing is lost.
    print(f"Stack after the empty loop : {stack}")
    print(f"Temporary list             : {temporary}")

    # Step 2: pour it back. Popping the temporary gives the bottom item first,
    # so pushing it back rebuilds the stack in the original order.
    while temporary:
        stack.append(temporary.pop())

    # Step 3: the stack is identical to how it started.
    print(f"Restored stack             : {stack}")
    print("The stack is unchanged.")


if __name__ == "__main__":
    main()
