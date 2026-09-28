"""
Question 04: Find the Largest Value and Print the Stack

Input:  stack = [10, 5, 50, 3, 13]
Output: INITIAL STACK  : [10, 5, 50, 3, 13]
        Top value      : 13
        Largest: 50
        Stack: [10, 5, 50, 3, 13]
        The stack is unchanged.

Tip: Use a temporary list to hold the values as you pop them, keep a running
    largest value in a variable, then push the temporary values back to restore
    the stack.
"""


def main() -> None:
    print("=" * 50)
    print("Question 04: Find the Largest Value and Print the Stack")
    print("=" * 50)

    stack = [10, 5, 50, 3, 13]
    temporary = []
    largest = 0

    # --- STARTER ---
    # You cannot walk a stack without emptying it, so use the same trick as
    # question 03: pop everything into a temporary list, then push it all back.
    # Step 1: set largest to the top value, which is stack[-1] in Python.
    # Step 2: while the stack is not empty, pop a value, and if the value is
    #         greater than largest then update largest.
    # Step 3: push the temporary values back to restore the stack.
    # Step 4: print the largest and the restored stack.
    # Expected: Largest: 50, and the stack back as [10, 5, 50, 3, 13]

    # --- SOLUTION ---
    print(f"INITIAL STACK  : {stack}")

    # Step 1: stack[-1] is peek, the top value without removing it.
    largest = stack[-1]
    print(f"Top value      : {largest}")

    # Step 2: pop every value and keep track of the biggest one seen so far.
    while stack:
        value = stack.pop()
        if value > largest:
            largest = value
        temporary.append(value)

    # Step 3: pour the temporary list back so the stack is whole again.
    while temporary:
        stack.append(temporary.pop())

    # Step 4: the answer and the restored stack.
    print(f"Largest: {largest}")
    print(f"Stack: {stack}")
    print("The stack is unchanged.")


if __name__ == "__main__":
    main()
