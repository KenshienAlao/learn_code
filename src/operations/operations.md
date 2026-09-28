# What are Operations in Python?

An operator is a symbol that tells Python to do something to a value: add, compare, decide. This lesson covers the operators you use every day.

---

## Arithmetic Operators

These are the maths symbols, and every result below is real.

| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| `+` | Addition | `2 + 3` | `5` |
| `-` | Subtraction | `7 - 2` | `5` |
| `*` | Multiplication | `3 * 4` | `12` |
| `/` | Division | `7 / 2` | `3.5` |
| `//` | Floor division | `7 // 2` | `3` |
| `%` | Remainder | `7 % 2` | `1` |
| `**` | Power | `2 ** 3` | `8` |

`%` is the leftover after a division that does not come out even. A remainder of `0` means the number divides evenly by 2 — that is the even and odd test.

`**` is power. Raising to `0.5` gives the square root, so `9 ** 0.5` is `3.0`.

Trap: `**` binds tighter than unary minus, so the power happens first.

```python
print(-2 ** 2)      # -4
print(-(2 ** 2))    # -4, safe
print((-2) ** 2)    # 4, negate first then square
```

Output:
```
-2 ** 2
  ^  ^^
  |  power first:  2 ** 2 = 4
  then minus:      -(4) = -4
```

If you meant the other reading, write `-(2 ** 2)`.

---

## Floor Division and the Double Slash

`//` divides and throws the fractional part away, so the result is always an `int`.

```python
print(7 // 2)    # 3
print(-7 // 2)   # -4
```

Floor means down to the next whole number. Down means negative infinity even for negatives. So `-7 // 2` is `-4`, not `-3`. It rounds down, not towards zero.

```
   7  |--------------    three whole groups
   2  |-------------     one left over

   7 // 2  =  3    the whole groups
   7 %  2  =  1    the leftover
```

Trap: `//` is an operator, not a comment. A stray `//` where you meant a comment stops Python.

```python
// q = 3
```

Output:
```
SyntaxError: invalid syntax
```

When you want a comment, use `#`.

---

## Division: / Versus //

`/` always gives a `float` in Python 3, whatever the numbers are.

```python
print(4 / 2)     # 2.0
print(4 // 2)    # 2
print(4 / 3)     # 1.3333333333333333
print(4 // 3)    # 1
```

`4 / 2` is `2.0`, not `2`. For a whole number you must ask: use `//`, or wrap the result in `int()`.

```python
print(int(-3.9))     # -3
print(-3.9 // 1)     # -4.0
```

`int()` cuts towards zero, `//` floors down. They agree for positives and disagree for negatives. Pick the one that matches what you mean.

---

## Power with **, and Why ^ Is Not Power

```python
print(2 ** 3)    # 8
print(2 ^ 3)     # 1
```

`^` is bitwise XOR. It works on the binary digits of integers. A bit is `1` in the answer only when the two bits differ.

```
  2 = 10
  3 = 11
     ^^
  10 XOR 11 = 01 = 1
```

`^` is not a mistake. It is a real operator on integers, the right tool for bit-level work. It is just not the tool for maths. Use `**` for power.

---

## Comparison Operators

`==`, `!=`, `<`, `>`, `<=`, `>=`. Each returns `True` or `False`, with capital letters.

A single `=` assigns a name, a double `==` compares values. Writing `if x = 5:` is a syntax error, so you cannot compare by accident.

```python
x = 5
if x = 5:
    print("hi")
```

Output:
```
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

`==` on two strings compares the characters one by one. That is the test you nearly always want. `is` compares identity: are two names pointing at the same object in memory, or just two things that look the same?

```python
a = "".join(["hel", "lo"])
b = "".join(["hel", "lo"])
print(a == b)   # True, same characters
print(a is b)   # False, two objects
```

`is` is almost never what you want. Use `==` for strings, numbers and lists.

---

## and, or, not

The logical operators, spelled out as words rather than symbols.

| `a` | `b` | `a and b` | `a or b` | `not a` |
| --- | --- | --- | --- | --- |
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

`and` is true only when both sides are true. `or` is true when at least one side is true. `not` flips the value and takes no symbol.

A value need not be `True` to count as true. An empty string is false, any non-empty string is true. Zero is false, any other number is true.

```python
print(bool("hello"), bool(""))    # True False
print(bool(0), bool(-5))          # False True
```

`and` and `or` short circuit: if the left side settles the answer the right side is never evaluated, so `name and name[0]` is safe on an empty string.

---

## Chained Comparisons

A range test fits in one expression.

```python
age = 20
print(18 <= age <= 65)    # True
```

That means `18 <= age and age <= 65`. It is a shortcut, not new logic, but it reads like the sentence you would say out loud.

```python
age = 20

if 18 <= age <= 65:                # chained
    print("In range")

if age >= 18 and age <= 65:        # spelled out
    print("In range")
```

`in` and `not in` are the other comparison-style operators you meet straight away. They test whether a value sits inside something.

```python
print(3 in [1, 2, 3])        # True
print(5 not in [1, 2, 3])    # True
print("ell" in "hello")      # True
print("cat" in "hello")      # False
```

On a list `in` matches a whole element. On a string it is a substring test, so `"ell"` matches without being the whole text.

---

## Augmented Assignment

These apply an operator to the variable you already have: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`. So `score += 1` means `score = score + 1`.

```python
score = 10
score += 1
print(score)    # 11

text = "hello"
text += "!"
print(text)     # hello!
```

`+` adds numbers and glues strings together, depending on what is on the right. When the two sides do not match, Python says so rather than guessing.

```python
text = "count: "
    # text += 1
text += 1
```

Output:
```
TypeError: can only concatenate str (not "int") to str
```

The middle line is commented out because the third raises. To mix a string and a number, convert first with `str(1)`.

---

## Operator Precedence

The order Python works in, highest first. Brackets always win and cost nothing, so use them when unsure.

| Order | Operators |
| --- | --- |
| Highest | `**` power, tighter than unary minus |
| | `-x`, `+x` unary sign |
| | `*`, `/`, `//`, `%` same level, left to right |
| | `+`, `-` same level, left to right |
| | `==`, `!=`, `<`, `>`, `<=`, `>=`, `in`, `not in` |
| | `not` |
| | `and` |
| | `or` |
| Lowest | `=`, `+=`, `-=`, ... |

Multiplication beats addition, so `2 + 3 * 4` groups as `2 + (3 * 4)`.

```python
print(2 + 3 * 4)     # 14
print((2 + 3) * 4)   # 20
```

That is why `v = u + a * t` gives `5 + (2 * 4)` which is `13`. On one level Python goes left to right, so `10 - 4 - 3` is `3`.

---

## Common Formulas

The school formulas in Python, with the numbers the practice questions use.

```python
m, x, b = 2, 5, 3
print("linear offset  ", m * x + b)
pi, r = 3.14159, 5
print("circle area    ", pi * r ** 2)
a, b_side = 3, 4
print("hypotenuse     ", (a ** 2 + b_side ** 2) ** 0.5)
principal, rate, years = 1000, 0.05, 2
print("simple interest", principal * rate * years)
u, a_acc, t = 5, 2, 4
print("velocity       ", u + a_acc * t)
mass, volume = 25, 10
print("density        ", mass / volume)
```

Output:
```
linear offset   13
circle area     78.53975
hypotenuse      5.0
simple interest 100.0
velocity        13
density         2.5
```

Interest is `100.0` and density is `2.5` because `0.05` and `/` make floats.

---

## A Note on Pi and Floats

`3.14159` is fine for school work and is what question 01 uses, so the area is `78.53975`. For the most accurate value, use `math.pi`.

A float holds a fixed number of digits, so a repeating decimal gets cut off.

```python
print(1 / 3)      # 0.3333333333333333
print(0.1 + 0.2)  # 0.30000000000000004
```

That trailing `004` is why `0.1 + 0.2` is not exactly `0.3`.

---

## Summary

| Python | What it does |
| --- | --- |
| `a + b`, `a - b`, `a * b` | Add, subtract, multiply |
| `a / b` | Division, always a float |
| `a // b`, `a % b` | Floor division, remainder |
| `a ** b`, `a ** 0.5`, `a ^ b` | Power, power 0.5 for a root, XOR |
| `a == b`, `a != b`, `a is b` | Compare values, or objects |
| `lo <= x <= hi`, `x in items` | Chained range test, is it inside |
| `a and b`, `a or b`, `not a` | Combine or flip truth |
| `x += 1` | Update in place |
| `#` | A comment |

---

## Common Mistakes

- Using `^` for power. `2 ^ 3` is `1`. Power is `2 ** 3`.
- Writing `//` where you meant a comment. Comments start with `#`.
- Expecting `4 / 2` to give `2`. It gives `2.0`. You wanted `4 // 2`.
- Forgetting `/` always returns a float, so averages keep their decimal point.
- Writing `text += 1` on a string. That raises a `TypeError`. Use `str(1)`.
- Writing `if x = 5`. A single `=` assigns. Use `if x == 5`.
- Using `is` instead of `==`. `is` compares objects, not contents.
- Forgetting `-2 ** 2` is `-4`. `**` binds tighter than unary minus, so write `-(2 ** 2)`.
- Using `&` or `|` instead of `and` and `or`. Python wants the words.
- Checking a remainder with `if number % 2:` when you meant `== 0`. A non-zero remainder is already true.

---

## Practice

The five questions in this folder put all of this to work, one topic each, and none of them need input. Run one with `python3 question_01.py`.

- [Question 01](./question_01.py)
- [Question 02](./question_02.py)
- [Question 03](./question_03.py)
- [Question 04](./question_04.py)
- [Question 05](./question_05.py)