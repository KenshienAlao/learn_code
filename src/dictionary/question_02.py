"""
Question 02: Safe Lookup Using get() and in

Input:  users = {"ravi": 20, "sana": 25} and name = "priya"
Output: users.get(name) returns: None
        users.get(name, 'Not found') returns: Not found
        'priya' in users -> False
        users.get('ravi') returns: 20
Tip:  d["key"] raises KeyError when the key is missing, but d.get("key", default) just returns the default.
"""


def main() -> None:
    print("=" * 50)
    print("Question 02: Safe Lookup Using get() and in")
    print("=" * 50)

    users = {"ravi": 20, "sana": 25}
    name = "priya"

    # --- STARTER ---
    # Look up a name that is NOT in the dict, in three different ways.
    # 1. users[name] would crash with a KeyError, so leave that line as a comment.
    # 2. users.get(name) returns None, which is safe and does not crash.
    # 3. users.get(name, "Not found") returns your own default text instead of None.
    # Then test membership with: name in users, and look up a name that IS present, "ravi".
    # Expected result: None, Not found, False, 20

    # --- SOLUTION ---
    # 1. The unsafe way. Do NOT uncomment this, it stops the whole program.
    # print(users[name])  # -> KeyError: 'priya'

    # 2. The safe way. Missing key, so get() hands back None.
    result = users.get(name)
    print("users.get(name) returns:", result)

    # 3. The safe way with a default. Missing key, so the default is used instead.
    result_with_default = users.get(name, "Not found")
    print("users.get(name, 'Not found') returns:", result_with_default)

    # 4. Membership test. This is Python's way to check if a key exists.
    print(f"'{name}' in users ->", name in users)

    # 5. A key that does exist, so get() returns the stored value 20.
    print("users.get('ravi') returns:", users.get("ravi"))


if __name__ == "__main__":
    main()
