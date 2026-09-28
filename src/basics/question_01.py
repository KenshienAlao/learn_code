"""
Question 01: Formatted Introduction Card Using f-Prints

Input:  name = "Ravi", age = 20, city = "Chennai"
Output: Name: Ravi
        Age: 20
        City: Chennai
        Summary: Ravi is 20 years old and lives in Chennai.

Tip: Put an f in front of the quotes and drop values into {} to build a clean line of text.
"""


def main() -> None:
    print("=" * 50)
    print("Question 01: Formatted Introduction Card Using f-Prints")
    print("=" * 50)

    name = "Ravi"
    age = 20
    city = "Chennai"

    # --- STARTER ---
    # Build an introduction card with four f-strings.
    # Line 1: Name: Ravi
    # Line 2: Age: 20
    # Line 3: City: Chennai
    # Line 4: Summary: Ravi is 20 years old and lives in Chennai.
    # Each line is one print() call using an f-string, for example f"Name: {name}".
    # Note: f-strings do NOT add a space for you. print() adds the space between
    # its own arguments, but anything inside {} is inserted exactly as written.

    # --- SOLUTION ---
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Summary: {name} is {age} years old and lives in {city}.")


if __name__ == "__main__":
    main()
