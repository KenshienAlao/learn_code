"""
Question 01: Reverse a String

Input:  text = "Hello"
Output: Text               : Hello
        Stack at the start : []
        Stack after pushing: ['H', 'e', 'l', 'l', 'o']
        Reversed text      : olleH
        Stack is empty now : True

Tip: Push every character with append(), then pop() them off one at a time and
    glue each popped character onto a new string.
"""


def main() -> None:
    print("=" * 50)
    print("Question 01: Reverse a String")
    print("=" * 50)

    text = "Hello"
    stack = []
    reversed_text = ""

    # --- STARTER ---
    # A Python list used only with append() and pop() IS a stack.
    # Step 1: make an empty list called stack. That list is the stack.
    # Step 2: loop over every character in text and push it with stack.append(character).
    # Step 3: loop len(text) times, and each time pop the top character off and
    #         add it to the end of a new string.
    # Step 4: print the new string. The letters must come out with no spaces
    #         between them, as one word: olleH

    # --- SOLUTION ---
    print(f"Text               : {text}")

    # Step 1: the empty list is our stack, the bottom is index 0.
    stack = []
    print(f"Stack at the start : {stack}")

    # Step 2: push every character on. The last one in is 'o'.
    for character in text:
        stack.append(character)
    print(f"Stack after pushing: {stack}")

    # Step 3: pop one character per loop and glue it onto the answer.
    # The guard `if stack:` stops us popping past the bottom.
    for i in range(len(text)):
        if stack:
            top_character = stack.pop()
            reversed_text = reversed_text + top_character

    # Step 4: print the result. print() adds no spaces of its own, so the
    # characters come out packed together exactly as one word.
    print(f"Reversed text      : {reversed_text}")
    print(f"Stack is empty now : {not stack}")


if __name__ == "__main__":
    main()
