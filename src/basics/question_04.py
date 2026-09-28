"""
Question 04: Type Casting and type()

Input:  age = "20", price = "4.50"
Output: age = '20' -> type is <class 'str'>
        age after int(age) = 20 -> type is <class 'int'>
        price = '4.50' -> type is <class 'str'>
        price after float(price) = 4.5 -> type is <class 'float'>
        int("20") + 1 = 21
        "20" + 1  ->  TypeError: can only concatenate str (not "int") to str

Tip: Print type(x) before you convert to see what you really have. Casting is a promise, not a check.
"""


def main() -> None:
    print("=" * 50)
    print("Question 04: Type Casting and type()")
    print("=" * 50)

    age = "20"
    price = "4.50"

    # --- STARTER ---
    # Both values above are strings, even the one that looks like a number.
    # Step 1: print(f"age = '{age}' -> type is {type(age)}")
    #         the single quotes are typed by you, not printed by Python. They are
    #         there to show you that 20 is sitting in a string, not a real number.
    # Step 2: age_int = int(age)  then print the new value and {type(age_int)}
    # Step 3: do the same for price with float(price)
    #         careful, float("4.50") prints 4.5, not 4.50. The trailing zero is gone.
    # Step 4: print(f"int(\"20\") + 1 = {int(age) + 1}")  which is 21
    # Step 5: the line age + 1 is a TypeError, so leave it commented out and
    #         print the message below instead. Python will not add a str and an int.
    # Casting never checks that the text makes sense. int("abc") would raise a ValueError.

    # --- SOLUTION ---
    print(f"age = '{age}' -> type is {type(age)}")
    age_int = int(age)
    print(f"age after int(age) = {age_int} -> type is {type(age_int)}")

    print(f"price = '{price}' -> type is {type(price)}")
    price_float = float(price)
    print(f"price after float(price) = {price_float} -> type is {type(price_float)}")

    print(f"int(\"20\") + 1 = {int(age) + 1}")

    # age + 1  would raise TypeError, so it stays commented out on purpose
    print('"20" + 1  ->  TypeError: can only concatenate str (not "int") to str')


if __name__ == "__main__":
    main()
