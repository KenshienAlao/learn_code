"""
Question 02: Check Balanced Parentheses

Input:  text = "(())"  and  text = "(()"
Output: Text: (())
        (()) -> Balanced, leftover on the stack: []
        Text: (()
        (() -> Not balanced, leftover on the stack: ['(']

Tip: Push every "(" and pop one for every ")", but check `if stack:` before you
    pop, because a ")" with an empty stack means Not balanced straight away.
"""


def main() -> None:
    print("=" * 50)
    print("Question 02: Check Balanced Parentheses")
    print("=" * 50)

    texts = ["(())", "(()"]
    stack = []
    balanced = True
    result = ""

    # --- STARTER ---
    # A stack is perfect for brackets, because the last "(" you opened is the
    # first ")" you have to close.
    # Step 1: for each text in texts, start again with an empty stack.
    # Step 2: loop over the characters. Push "(" and pop ")".
    # Step 3: if a ")" turns up while the stack is empty, it is Not balanced.
    # Step 4: after the loop, the stack empty means Balanced, otherwise not.
    # Expected: (()) -> Balanced, and (() -> Not balanced

    # --- SOLUTION ---
    for text in texts:
        # Step 1: fresh stack for every text, so the runs do not mix up.
        stack = []
        balanced = True
        print(f"Text: {text}")

        # Step 2 and 3: push on "(", pop on ")".
        for character in text:
            if character == "(":
                stack.append(character)
            else:
                # The guard: a ")" with nothing to close is already broken.
                if stack:
                    stack.pop()
                else:
                    balanced = False

        # Step 4: the if/else ladder that decides the final word.
        if balanced:
            if stack:
                result = "Not balanced"
            else:
                result = "Balanced"
        else:
            result = "Not balanced"

        print(f"{text} -> {result}, leftover on the stack: {stack}")
        print("-" * 50)


if __name__ == "__main__":
    main()
