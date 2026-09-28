"""
Question 01: Count Word Frequencies

Input:  the string "the cat and the dog and the cat"
Output: Words: ['the', 'cat', 'and', 'the', 'dog', 'and', 'the', 'cat']
        the: 3
        cat: 2
        and: 2
        dog: 1
Tip:  Use the counting pattern counts[word] = counts.get(word, 0) + 1 inside the loop.
"""


def main() -> None:
    print("=" * 50)
    print("Question 01: Count Word Frequencies")
    print("=" * 50)

    text = "the cat and the dog and the cat"

    # --- STARTER ---
    # Split the string into a list of words with text.split(), then loop over the words.
    # Use an empty dict called counts, and count with: counts[word] = counts.get(word, 0) + 1
    # That line means "if the word is already there, add 1 to the old number, else start at 1".
    # After the loop, walk the dict with for word in counts: and print each word and its count.
    # Dicts keep insertion order, so the order is the, cat, and, dog.
    # Expected result: the: 3, cat: 2, and: 2, dog: 1

    # --- SOLUTION ---
    # split() with no argument breaks on any whitespace and gives us a plain list of words.
    words = text.split()
    print("Words:", words)

    # Empty dict to hold the counts. This is the {} empty dict, not an empty set.
    counts = {}

    # The counting pattern: get the old value or 0, add 1, store it back.
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    # Looping over a dict directly gives you the keys, so counts[word] fetches the value.
    # "the" is printed first because it was the first word inserted, not because it is the biggest.
    for word in counts:
        print(f"{word}: {counts[word]}")


if __name__ == "__main__":
    main()
