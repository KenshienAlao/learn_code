"""
Question 04: Keep Only the Even Numbers

Input:  [1, 2, 3, 4, 5, 6]
Output: EVEN: [2, 4, 6]
Tip:  Use a second list as temporary storage, and never pop from the list you loop over.
"""


def main() -> None:
    print("=" * 50)
    print("Question 04: Keep Only the Even Numbers")
    print("=" * 50)

    queue = [1, 2, 3, 4, 5, 6]
    temp = []

    # --- STARTER ---
    # You need a SECOND list here. Do not remove items while you are looping over
    # that same list, the shifting makes the loop skip elements without any error.
    # Step 1: `while queue:` pop(0) each number, and if num % 2 == 0, append it to temp.
    # Step 2: `while temp:` pop(0) from temp and append it back onto queue.
    # Step 3: print("EVEN:", queue). The result order should still be 2, 4, 6.
    # Expected result: EVEN: [2, 4, 6]

    # --- SOLUTION ---
    # Pass 1: empty the original queue, keeping only the even numbers.
    while queue:
        num = queue.pop(0)
        # % is the modulo operator, num % 2 == 0 means num divides evenly by 2.
        if num % 2 == 0:
            temp.append(num)

    # Pass 2: pour the keepers back onto the queue in the order they were found.
    while temp:
        num = temp.pop(0)
        queue.append(num)

    print("EVEN:", queue)


if __name__ == "__main__":
    main()
