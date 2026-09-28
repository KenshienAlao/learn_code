"""
Question 01: Search for an Element

Input:  the list ["SpongeBob", "Patrick", "Squidward"] and the search term "patrick"
Output: Found
Tip:  Loop with for, compare item == search using .lower() on both sides so the match ignores case, flip a found flag, and break out of the loop the moment it is set.
"""


def main() -> None:
    print("=" * 50)
    print("Question 01: Search for an Element")
    print("=" * 50)

    items = ["SpongeBob", "Patrick", "Squidward"]
    search = "patrick"
    found = False
    checked = 0

    # --- STARTER ---
    # In Python a plain for loop walks the list without destroying it, so do this:
    #   1. set found = False and checked = 0 before the loop
    #   2. loop with: for item in items:
    #   3. compare item.lower() == search.lower() so "Patrick" matches "patrick"
    #   4. on a match set found = True, then break (this is the break)
    #   5. after the loop print the found flag with a simple if / else
    # Expected result: Found

    # --- SOLUTION ---
    for item in items:
        # Count every item we actually looked at, so the break is visible.
        checked = checked + 1
        if item.lower() == search.lower():
            found = True
            break

    print("Items: " + str(items))
    print("Searching for: " + search)
    print("Items checked before the match: " + str(checked))

    if found:
        print("Found")
    else:
        print("Not found")


if __name__ == "__main__":
    main()
