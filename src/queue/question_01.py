"""
Question 01: Print All Queue Elements

Input:  ["Spongebob", "Patrick", "Squidward"]
Output: Spongebob
        Patrick
        Squidward
        Queue is now: []
        Items left: 0
Tip:  Loop with `while queue:` and remove the front item with pop(0) each pass.
"""


def main() -> None:
    print("=" * 50)
    print("Question 01: Print All Queue Elements")
    print("=" * 50)

    queue = ["Spongebob", "Patrick", "Squidward"]

    # --- STARTER ---
    # A queue in Python is just a list. append() adds to the rear, pop(0) takes the front.
    # Loop with `while queue:` and print the item that pop(0) gives you back.
    # Never call pop(0) on an empty list, it raises IndexError, so the loop is the guard.
    # Expected result: the three names printed one per line, in the order they went in,
    # because a queue is FIFO so the first one in is the first one out.

    # --- SOLUTION ---
    # An empty list is falsy, so this loop runs while the queue still has anything in it.
    while queue:
        # pop(0) returns the front item AND removes it.
        name = queue.pop(0)
        print(name)

    # The loop only stops once the list is empty, so len(queue) is 0 here.
    print("Queue is now:", queue)
    print("Items left:", len(queue))


if __name__ == "__main__":
    main()
