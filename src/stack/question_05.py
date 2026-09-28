"""
Question 05: Browser Back Button Simulation

Input:  history = ["Google", "YouTube", "GitHub", "Facebook"], pages_visited = 2
Output: Current Page: Facebook
        Back -> GitHub
        Back -> YouTube
        Current Page: YouTube
        History left : ['Google', 'YouTube']

Tip: Use the guard `if len(history) > 1:` before every pop, so you can never
    pop the very first page you visited off the history stack.
"""


def main() -> None:
    print("=" * 50)
    print("Question 05: Browser Back Button Simulation")
    print("=" * 50)

    history = ["Google", "YouTube", "GitHub", "Facebook"]
    pages_visited = 2
    step = 0

    # --- STARTER ---
    # The history is a stack: the newest page is on top.
    # Step 1: print the current page using history[-1], that is peek in Python.
    # Step 2: repeat pages_visited times. Each time check `if len(history) > 1:`
    #         first, because popping the last page is not allowed, then pop and
    #         print the new current page as "Back -> <page>".
    # Step 3: after the loop, print the current page again.
    # Expected: start at Facebook, go back to GitHub, then back to YouTube.

    # --- SOLUTION ---
    # Step 1: history[-1] is the top of the stack, the page you are looking at.
    print(f"Current Page: {history[-1]}")

    # Step 2: press back pages_visited times.
    for step in range(pages_visited):
        # The guard. len(history) > 1 means at least one page is left below
        # the current one, so popping is safe and we keep the first page.
        if len(history) > 1:
            history.pop()
            print(f"Back -> {history[-1]}")
        else:
            print("No more pages to go back to.")

    # Step 3: where we ended up.
    print(f"Current Page: {history[-1]}")
    print(f"History left : {history}")


if __name__ == "__main__":
    main()
