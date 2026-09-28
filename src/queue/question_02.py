"""
Question 02: Sum All Numbers in a Queue

Input:  [10, 20, 30, 40]
Output: Total: 100
        Queue is now: []
Tip:  Poll each number with pop(0) and add it into a total variable that starts at 0.
"""


def main() -> None:
    print("=" * 50)
    print("Question 02: Sum All Numbers in a Queue")
    print("=" * 50)

    queue = [10, 20, 30, 40]
    total = 0

    # --- STARTER ---
    # Start a variable called total at 0, that is where an accumulator always begins.
    # Loop with `while queue:`, take the front item with pop(0), and add it to the total.
    # Add it to the SAME variable every pass, or you will just overwrite the old value.
    # Expected result: Total: 100, and the queue is empty afterwards because you
    # consumed every item on the way to the answer.

    # --- SOLUTION ---
    # while queue: is the guard that keeps pop(0) away from an empty list.
    while queue:
        # Take the front number out and add it to the running total.
        num = queue.pop(0)
        total += num

    print("Total:", total)
    # Every number was polled, so nothing is left in the queue. That is fine here.
    print("Queue is now:", queue)


if __name__ == "__main__":
    main()
