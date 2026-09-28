"""
Question 03: Velocity Using v = u + at

Input:  u = 5, a = 2, t = 4
Output: a * t                       : 8
        Velocity (u + a * t)        : 13
        Distance travelled          : 36.0

Tip: Multiplication binds tighter than addition, so u + a * t is read as
    u + (a * t), not as (u + a) * t. If you want the other reading, you must
    type the parentheses yourself.
"""


def main() -> None:
    print("=" * 50)
    print("Question 03: Velocity Using v = u + at")
    print("=" * 50)

    u, a_acc, t_acc = 5, 2, 4

    # --- STARTER ---
    # The formula is v = u + a * t.
    # Step 1: compute a * t on its own and store it as acceleration_times_time.
    # Step 2: add u to that value to get the final velocity.
    # Step 3: also try the distance formula d = u * t + 0.5 * a * t ** 2.
    # Expected: velocity 13, and distance 36.0.

    # --- SOLUTION ---
    # Step 1: a * t is done first because * has higher precedence than +.
    acceleration_times_time = a_acc * t_acc
    print(f"Initial velocity (u)        : {u}")
    print(f"Acceleration (a)            : {a_acc}")
    print(f"Time (s)                    : {t_acc}")
    print(f"a * t                       : {acceleration_times_time}")

    # Step 2: v = u + (a * t). Writing the brackets here just makes it obvious.
    velocity = u + (a_acc * t_acc)
    print(f"Velocity (u + a * t)        : {velocity}")

    # Step 3: s = u * t + 0.5 * a * t ** 2. The 0.5 makes the result a float.
    distance = u * t_acc + 0.5 * a_acc * t_acc ** 2
    print(f"Distance travelled          : {distance}")
    print("=" * 50)


if __name__ == "__main__":
    main()
