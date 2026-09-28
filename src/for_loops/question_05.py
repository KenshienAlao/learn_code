"""
Question 05: FizzBuzz

Input:  the numbers 1 to 15
Output: 1
        2
        Fizz
        4
        Buzz
        Fizz
        7
        8
        Fizz
        Buzz
        11
        Fizz
        13
        14
        FizzBuzz
Tip:  Check both conditions with `and` first, so 15 hits FizzBuzz instead of stopping at Fizz.
"""


def main() -> None:
    print("=" * 50)
    print("Question 05: FizzBuzz")
    print("=" * 50)

    start, stop = 1, 16

    # --- STARTER ---
    # Loop over every number from 1 to 15 using: for i in range(start, stop):
    # Then use a plain if / elif / else chain, no clever one-liners:
    #   divisible by 3 and NOT by 5  -> print("Fizz")
    #   divisible by 5 and NOT by 3  -> print("Buzz")
    #   divisible by 3 AND by 5     -> print("FizzBuzz")
    #   otherwise                   -> print(i)
    # The `and` / `!=` conditions are what send 15 to FizzBuzz, so keep them.
    # Print the result for each number inside the loop, one per line.
    # Expected result: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

    # --- SOLUTION ---
    for i in range(start, stop):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)


if __name__ == "__main__":
    main()
