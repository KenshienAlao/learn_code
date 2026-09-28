"""
Question 05: Day of the Week Using match / case

Input:  Monday, Saturday, Funday
Output: Monday is a weekday day
        Saturday is a weekend day
        Funday is an unknown day

Tip: match / case is Python's switch and it needs Python 3.10 or newer.
     Use case _ as the wildcard, and use |
     to put several values in one case. There is no break needed.
"""


def main() -> None:
    print("=" * 50)
    print("Question 05: Day of the Week Using match / case")
    print("=" * 50)

    day_1, day_2, day_3 = "Monday", "Saturday", "Funday"

    # --- STARTER ---
    # Store three day names in variables, for example Monday, Saturday, Funday.
    # Write a match block that sets a label for each day.
    # Put the five weekday names in one case joined with |, the weekend
    # names in another, and use case _ as the wildcard for anything else.
    # Then print the day and its label on one f-string line.
    # Expected result: Monday is a weekday day, Saturday is a weekend day,
    # Funday is an unknown day.

    # --- SOLUTION ---
    for day in (day_1, day_2, day_3):
        match day:
            case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
                label = "a weekday day"
            case "Saturday" | "Sunday":
                label = "a weekend day"
            case _:
                label = "an unknown day"

        print(f"{day} is {label}")


if __name__ == "__main__":
    main()
