"""
Question 03: Calculate the Average of a Queue

Input:  [10, 20, 30, 40]
Output: Total: 100
        Count: 4
        Average: 25.0
Tip:  Track the sum AND the count while polling, then divide with the / operator.
"""


def main() -> None:
    print("=" * 50)
    print("Question 03: Calculate the Average of a Queue")
    print("=" * 50)

    queue = [10, 20, 30, 40]
    total = 0
    count = 0

    # --- STARTER ---
    # An average needs two things, so keep two running variables: total and count.
    # Loop with `while queue:`, add the popped number to total, and add 1 to count.
    # After the loop, average = total / count.
    # Python 3 has no such trap, / always gives a float.
    # Expected result: Total: 100, Count: 4, Average: 25.0.

    # --- SOLUTION ---
    while queue:
        # One number off the front, added to both accumulators in the same pass.
        num = queue.pop(0)
        total += num
        count += 1

    print("Total:", total)
    print("Count:", count)

    # `/` in Python 3 always returns a float, so 100 / 4 gives 25.0 not 25.
    average = total / count
    print("Average:", average)


if __name__ == "__main__":
    main()
