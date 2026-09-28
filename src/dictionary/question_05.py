"""
Question 05: Group Items by First Letter

Input:  words = ["apple", "avocado", "banana", "blueberry", "cherry", "carrot"]
Output: a -> ['apple', 'avocado']
        b -> ['banana', 'blueberry']
        c -> ['cherry', 'carrot']
Tip:  Use setdefault(first, []).append(word) so the empty list is created only the first time that letter shows up.
"""


def main() -> None:
    print("=" * 50)
    print("Question 05: Group Items by First Letter")
    print("=" * 50)

    words = ["apple", "avocado", "banana", "blueberry", "cherry", "carrot"]

    # --- STARTER ---
    # Build a dict called groups where each key is a first letter and each value is a list of words.
    # Start with groups = {}, then loop over words and take first = word[0] for the key.
    # The beginner-friendly way: if first not in groups: groups[first] = [], then groups[first].append(word).
    # The one-liner version is groups.setdefault(first, []).append(word), which is the same thing.
    # After the loop, print each letter and its list. Keys come out in insertion order: a, b, c.
    # Expected result: a -> ['apple', 'avocado'], b -> ['banana', 'blueberry'], c -> ['cherry', 'carrot']

    # --- SOLUTION ---
    # Empty dict of groups. Each value will be a list, so the dict is str -> list.
    groups = {}

    # word[0] is the first character of the string.
    for word in words:
        first = word[0]

        # The letter is not a key yet, so create it and give it an empty list to hold words.
        if first not in groups:
            groups[first] = []

        # Now the key definitely exists, so appending is safe.
        groups[first].append(word)

    # Looping gives the keys in the order they were first added, so a, b, c.
    for letter in groups:
        print(f"{letter} -> {groups[letter]}")


if __name__ == "__main__":
    main()
