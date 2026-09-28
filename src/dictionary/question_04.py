"""
Question 04: Build a Phonebook Using zip()

Input:  names = ["Ravi", "Sana", "Arun"] and phones = ["9876543210", "9876500011", "9123456780"]
Output: Ravi: 9876543210
        Sana: 9876500011
        Arun: 9123456780
        Phonebook size: 3
        Priya's number: Not found
Tip:  Pair the two lists with for index in range(len(names)) and use names[index] as the key, phones[index] as the value.
"""


def main() -> None:
    print("=" * 50)
    print("Question 04: Build a Phonebook Using zip()")
    print("=" * 50)

    names = ["Ravi", "Sana", "Arun"]
    phones = ["9876543210", "9876500011", "9123456780"]

    # --- STARTER ---
    # Build a dict called phonebook mapping each name to its number.
    # Start with phonebook = {}, then loop with for index in range(len(names)):
    # Set phonebook[names[index]] = phones[index] so the name is the key and the number is the value.
    # After the loop, print every name and number, then len(phonebook), then a safe lookup with .get().
    # Expected result: three entries, a size of 3, and 'Not found' for a name that is not there.

    # --- SOLUTION ---
    # Empty dict first. Names are unique here, so every assignment creates a new key.
    phonebook = {}

    # The explicit loop. Using index on BOTH lists is what pairs the right number with the right name.
    # zip(names, phones) does the same job in one line, but the explicit loop is easier to read
    # when you are still learning, because you can see both lists being used.
    for index in range(len(names)):
        phonebook[names[index]] = phones[index]

    # Looping over the dict gives the keys, which are the names, so we look each value up.
    for name in phonebook:
        print(f"{name}: {phonebook[name]}")

    # len() returns the number of items in the dict.
    print("Phonebook size:", len(phonebook))

    # Safe lookup. 'Priya' is not a key, so .get() returns our default instead of raising KeyError.
    print("Priya's number:", phonebook.get("Priya", "Not found"))


if __name__ == "__main__":
    main()
