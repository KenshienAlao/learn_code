# What are Conditions in Python?

Conditions are how a program makes decisions. Python checks something, gets back a yes or a no, and the answer picks which block of code runs. If this is true do this, otherwise do that.

This lesson covers `if / else`, `elif`, comparisons, `and` / `or` / `not`, chained comparisons, truthiness, `is None`, short-circuit evaluation, `match / case`, and the conditional expression.

---

## Basic if / else

`if` runs its block when the condition is true. `else` runs its block in every other case.

```python
x = 7

if x > 0:
    print("positive")
else:
    print("not positive")
```

Output:
```
positive
```

The line ends with a colon `:` and the body sits on the next line, indented. There are no braces. The colon says "the body starts here", the indentation says how far it goes.

```text
if x > 0:
|    print("positive")
|    print("still in the if, same indent")
|    print("also in the if, the indent never changed")
else:
|    print("not positive")
```

All three prints sit at the same level, so all three are in the same block. The moment you dedent out of that level, the block is over. Indentation is not decoration in Python, it *is* the block.

Two errors show a malformed block. Leave off the colon and the file will not run:
```
  File "demo.py", line 2
    if x > 0
            ^
SyntaxError: expected ':'
```

Add the colon, then indent the body one line further in than its neighbours:
```
  File "demo.py", line 5
    print("extra line")
IndentationError: unexpected indent
```

---

## elif

`elif` means "if nothing above me matched, try this instead". Stack as many as you like.

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
```

Output:
```
Grade: B
```

Only the first branch that matches runs. Everything after it is skipped, so a later `elif` never fires once an earlier one has matched:

```
if score >= 90:     ->  85 >= 90 is False, keep going
elif score >= 80:   ->  85 >= 80 is True, run this one
elif score >= 70:   ->  never even looked at
else:               ->  never even looked at
```

Branch order matters. Start a ladder at the top: 90 and up is an A, 80 and up a B, 70 and up a C, 60 and up a D, below 60 an F.

`else if` is a hard error. The keyword is `elif`:
```
  File "demo.py", line 4
    else if x == 2:
         ^^
SyntaxError: expected ':'
```

---

## Comparison Operators

A comparison produces a single yes or no. There are six of them.

| Operator | Means |
| --- | --- |
| `==` | equal |
| `!=` | not equal |
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal |
| `>=` | greater than or equal |

A single `=` assigns, a double `==` compares. Because they differ, `if x = 5:` cannot be parsed at all, so you cannot compare by accident:
```
  File "demo.py", line 2
    if x = 5:
       ^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

That message tells you exactly what to write instead.

On strings, `==` compares the actual characters, so it just works:

```python
name = "Ada"

if name == "Ada":
    print("hello Ada")
```

Output:
```
hello Ada
```

`is` asks a different question. `==` asks "do these hold the same value". `is` asks "are these the same object in memory".

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```

Output:
```
True
False
```

---

## and, or, not

Python spells its logical operators with words. `and` needs both sides true, `or` needs at least one, `not` flips the answer.

| `a` | `b` | `a and b` | `a or b` | `not a` |
| --- | --- | --- | --- | --- |
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

```python
age = 22
has_id = True

if age >= 18 and has_id:
    print("allowed")
```

Output:
```
allowed
```

`not` sits in front of the whole expression, so it usually needs brackets around it. This is the whole leap year rule on one line: divisible by 4, and either not divisible by 100 or divisible by 400.

```python
for year in (2024, 1900):
    is_leap = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
    print(year, "->", is_leap)
```

Output:
```
2024 -> True
1900 -> False
```

The other way to build a condition is `in`, which asks whether a value sits inside something:

```python
if "Saturday" in ("Saturday", "Sunday"):
    print("weekend")
if "z" not in "cat":
    print("z is missing from cat")
```

Output:
```
weekend
z is missing from cat
```

---

## Chained Comparisons

To ask whether a number sits inside a range, write the range the way you say it. `18 <= age <= 65` is a single expression:

```python
age = 41

if 18 <= age <= 65:
    print(age, "is a working age")
```

Output:
```
41 is a working age
```

Python reads it as `18 <= age and age <= 65`, and the middle value is compared only once. It replaces the longer nested form:

```python
if 18 <= age and age <= 65:
    print(age, "is a working age")
```

Use the chain for numbers, and write the `and` out when the two tests are too different to read as a range.

---

## Truthiness and Falsy Values

You do not always need a comparison. Any value can be handed straight to `if` and Python decides if it counts as true. A short fixed set is falsy, everything else is truthy.

| Value | Why |
| --- | --- |
| `0` | zero is the number that means nothing |
| `0.0` | still zero, written with a decimal point |
| `""` | an empty string has no characters |
| `[]` | an empty list has no items |
| `{}` | an empty dict has no keys |
| `set()` | an empty set has no members |
| `None` | the marker for "there is no value here" |
| `False` | the boolean false |

Falsy means "there is nothing here". For a number nothing is `0`, for a string nothing is `""`, for a list nothing is `[]`. Same idea, different type. So a non-empty string and a negative number are both truthy, and `"0"` is truthy because it is a string holding one character.

You can ask Python directly what it thinks of any value with `bool()`:

```python
print(bool(0), bool(""), bool("0"), bool(-1))
```

Output:
```
False False True True
```

---

## is None

`None` is Python's marker for "there is no value here". A function that returns nothing hands you `None`. Test for it with `is`, not `==`.

`==` asks whether two things hold the same value. `is` asks whether they are the same object. Python keeps exactly one `None` object, so `is None` means "this really is the nothing value".

```python
result = None

if result is None:
    print("result is missing")
```

Output:
```
result is missing
```

That check is the guard that makes attribute access safe. Write `is not None` for the other direction:

```python
class Order:
    def __init__(self, total):
        self.total = total


item = None

if item is not None and item.total > 0:
    print("total:", item.total)
else:
    print("no order to show")
```

Output:
```
no order to show
```

Without the guard, `item.total` would raise `AttributeError`.

---

## Short-Circuit Evaluation

`and` and `or` do not evaluate both sides. They stop the moment the answer is already decided. `and` stops as soon as the left side is false, `or` stops as soon as the left side is true.

```
a and b     a is False  ->  b is never evaluated, answer is already False
             a is True   ->  b must run, its answer is the result

a or b      a is True   ->  b is never evaluated, answer is already True
             a is False  ->  b must run, its answer is the result
```

That is what makes it safe to chain a check with something dangerous. The right side runs only when the left side said yes:

```python
for x in (0, 5):
    if x != 0 and 100 / x > 10:
        print(x, "-> big")
    else:
        print(x, "-> not big")
```

Output:
```
0 -> not big
5 -> big
```

With `x` set to 0 the left side is already false, so the division never happens and you never see a `ZeroDivisionError`. The same protects an attribute: in `if result is not None and result.total > 0:` the left side is false whenever `result` is missing, so `result.total` is never touched. Put the safety check on the left, the risky thing on the right.

---

## match / case

`match / case` matches one value against a list of fixed options. It needs Python 3.10 or newer, and it is a statement, not a function call.

```python
day = "Saturday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("weekday")
    case "Saturday" | "Sunday":
        print("weekend")
    case _:
        print("unknown day")
```

Output:
```
weekend
```

`match day:` is the value being tested, each `case` is one option. The `|` puts several values in one arm, so `case 6 | 7:` catches both 6 and 7. `case _:` is the wildcard, catching anything no earlier case wanted.

Cases do not fall through. When one matches, Python runs that block and stops there, so there is no `break` to write and no way to run two blocks by accident.

Use `match / case` for one value against several fixed options, and an `if / elif` ladder when the tests are ranges or expressions instead.

---

## The Conditional Expression

A conditional expression is an `if / else` squeezed into one expression. The value comes first, the condition second, then `else` and the other value.

```python
score = 85
result = "PASS" if score >= 60 else "FAIL"
print(result)
```

Output:
```
PASS
```

A long one wraps across lines inside parentheses:

```python
num = 25
label = (
    "Positive"
    if num > 0
    else "Negative"
)
print(f"{num} is {label}")
```

Output:
```
25 is Positive
```

One can hold another, which handles a three way choice with no `if` at all:

```python
for num in (25, -7, 0):
    label = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
    print(f"{num} is {label}")
```

Output:
```
25 is Positive
-7 is Negative
0 is Zero
```

Keep it for short choices. The moment the branches need several statements each, it belongs in a real `if / else` block.

---

## Summary

| What you want | Python |
| --- | --- |
| Run a block when a test is true | `if x > 0:` and an indented body |
| Cover the other cases | `else:` |
| Add one more option | `elif x > 0:` |
| Compare values | `==` `!=` `<` `>` `<=` `>=` |
| Both sides true | `a and b` |
| Either side true | `a or b` |
| Flip the answer | `not a` |
| Check a range | `18 <= age <= 65` |
| Test a value with no comparison | `if items:` |
| Check for a missing value | `x is None` |
| Guard something risky | `x is not None and x.total > 0` |
| One value against fixed options | `match day:` with `case` arms |
| A short one line choice | `"yes" if ok else "no"` |
| Mark a block | a trailing `:` and indentation |

---

## Common Mistakes

- Forgetting the trailing colon on an `if`, `elif`, `else` or `case` line. You get `SyntaxError: expected ':'`.
- Indenting the body wrongly, so one line sits at a different level than the rest and you get `IndentationError: unexpected indent`.
- Dedenting the body out of the `if` by accident, so it runs on every pass.
- Writing `else if` instead of `elif`. It is a `SyntaxError`, nothing runs.
- Expecting a later `elif` to run after an earlier one matched. Only the first match counts.
- Writing `if x = 5:`. Python refuses it and points at the `=`.
- Testing a missing value with `== None` instead of `is None`.
- Forgetting that `0` and `""` are falsy, so `if name:` skips the block on an empty string.
- Writing a conditional expression with the condition and the value swapped. It is `value if condition else other`.

---

## Practice

The five questions for this topic live in this folder. Work through them in order. They build from a single `if / else` up to `match / case`.

- [Question 01](./question_01.py)
- [Question 02](./question_02.py)
- [Question 03](./question_03.py)
- [Question 04](./question_04.py)
- [Question 05](./question_05.py)