# What is Basic Python Syntax?

Python reads by the shape of each line. This lesson covers printing, comments, indentation, variables, types, f-strings, input, the main guard, and divmod.

---

## Printing

`print()` writes to the screen. Give it any value, it turns it into text and adds a newline.

`print()` with no arguments prints a blank line. `print("a", "b")` puts one space between values. `sep=` changes the separator. `end=` changes the ending.

```python
name = "Ravi"
age = 20
print("Name:", name)
print("Age:", age)
print()
print("a", "b")            # a b
print("a", "b", sep="-")   # a-b
print("loading", end="")   # no newline yet...
print("done")              # loadingdone
```

Output:
```
Name: Ravi
Age: 20

a b
a-b
loadingdone
```

`end=""` keeps the cursor on one line while loading.

---

## Comments and Docstrings

A comment starts with `#` and runs to the end of the line. Python ignores it.

```python
def main() -> None:
    # a comment can be as long as you like
    print("still runs")  # it can also sit after code
```

A docstring is three double quotes around a string. If it is the first thing in a file or function, Python attaches it as documentation. It is a real string, not decoration.

```python
def main() -> None:
    """Print a short greeting."""
    print("hello")


main()
print(main.__doc__)  # Print a short greeting.
```

`help(main)` shows that text in a readable block. Editors and doc tools also use it. Write one so the next reader knows what the function does without reading the code.

---

## Indentation Is the Block

Indentation groups statements. Leading spaces are part of the syntax, not style. A block starts on a line ending in `:` and continues on the indented lines beneath. It ends when indentation moves back left.

```python
age = 20
if age >= 18:
    print("adult")
else:
    print("minor")
```

Output: `adult`

Four spaces per level:

```text
L0   0 spaces  | def main() -> None:
L1   4 spaces  |     total = 3725
L2   8 spaces  |     if total > 60:
L3  12 spaces  |         print("long")
L2   8 spaces  |     print("done")
```

The colon is required; leave it off and Python stops with `SyntaxError: expected ':'`. Missing the indent raises `IndentationError`:

```python
if age > 18:
  print("adult")
    print("still inside")
```

Output:
```
IndentationError: unexpected indent
```

Mixing tabs and spaces raises `TabError: inconsistent use of tabs and spaces in indentation`.

---

## Variables and Types

A variable is a name bound to a value: name, equals sign, value. No type keyword is needed; the type belongs to the value, not the name.

```python
name = "Ravi"          # a str
is_student = True      # snake_case, not isStudent
a, b = 1, 2            # two names in one statement
x, y = y, x            # the swap, no temporary variable
```

A name can hold a `str` on one line and an `int` on the next. Names use `snake_case`, constants `UPPER_SNAKE_CASE`; both are conventions, not rules.

One statement can bind several names. The right side is collected first, then unpacked position by position, which is why `a, b = b, a` needs no temporary variable.

The four types you need:

| Type | Example | Note |
| --- | --- | --- |
| `int` | `20` | Whole numbers of any size |
| `float` | `4.5` | Always 64 bit, `4.50` becomes `4.5` |
| `str` | `"Ravi"` | Immutable, either quote style works |
| `bool` | `True` | Exactly two values, both capitalised |

`True` and `False` are capitalised; `true` raises `NameError: name 'true' is not defined`. A bool is an int underneath, so `True + True` is `2`. `type(x)` checks at runtime:

```python
print(type(20), type(4.5), type("Ravi"), type(True))
```

Output:
```
<class 'int'> <class 'float'> <class 'str'> <class 'bool'>
```

Type hints are optional and unchecked at runtime. They help editors catch mistakes early: `name: str = "Ravi"`, and `def main() -> None:` for a function returning nothing.

---

## f-Strings

An f-string builds a string with values dropped into `{}` braces. Put an `f` in front of the quotes, then put each expression between braces.

```python
name = "Ravi"
age = 20
city = "Chennai"
print(f"Name: {name}, Age: {age}")
print(f"Summary: {name} is {age} years old and lives in {city}.")
```

Output:
```
Name: Ravi, Age: 20
Summary: Ravi is 20 years old and lives in Chennai.
```

Inside `{}` you can write a whole expression. That is why f-strings win. `"Name: " + str(name)` needs `str()` around every non-string or it raises `TypeError: can only concatenate str (not "int") to str`. `.format()` pushes the values away from the text.

```python
print(f"2 + 2 = {2 + 2}")        # 2 + 2 = 4
print(f"in 6 months: {age + 6}")  # in 6 months: 26
```

One trap: `print("a", "b")` adds a space between its arguments, but an f-string never does; the space belongs to `print`. Triple quotes let an f-string span lines, handy for a card.

```python
card = f"""Name: {name}
Age: {age}"""
print(card)
```

Output:
```
Name: Ravi
Age: 20
```

---

## Input and divmod

`input()` reads one line a person typed and always returns a `str`. Type `20`, you get the text `"20"`.

To get a number, convert it yourself, with the conversion on the outside, after the read.

```python
def main() -> None:
    age = int(input("Enter your age: "))      # correct: read first, convert second
    price = float(input("Enter a price: "))   # float for decimals
    # age = input(int("Enter your age: "))    # wrong order, kept as a comment
```

In the wrong order Python evaluates the inner call first, so `int()` fails on your prompt text before `input()` runs:

```
ValueError: invalid literal for int() with base 10: 'Enter your age: '
```

Read first, convert second.

`divmod(a, b)` returns a pair: the quotient and the remainder. Unpack it into two names.

```python
total = 3725
hours, rest = divmod(total, 3600)
minutes, seconds = divmod(rest, 60)
print(f"{total} seconds is {hours} hours, {minutes} minutes, {seconds} seconds")
```

Output:
```
3725 seconds is 1 hours, 2 minutes, 5 seconds
```

`3725 = 3600 + 125`, so `divmod(3725, 3600)` gives `(1, 125)`; `125 = 120 + 5`, so `divmod(125, 60)` gives `(2, 5)`. `//` and `%` do the same two jobs; `divmod` returns them together.

---

## The main Guard

`if __name__ == "__main__":` is the block a file runs when you execute it directly.

```python
def main() -> None:
    print("running the demo")


if __name__ == "__main__":
    main()
```

`__name__` is a special variable Python sets. Run a file directly and its value is `"__main__"`, so the block runs. When another file does `import helper`, `__name__` is the module name, the condition is false, and the block is skipped.

```
python3 helper.py      ->  __name__ == "__main__"   ->  main() runs
import helper          ->  __name__ == "helper"     ->  main() skipped
```

The practical reason: importing a module should let you reuse its functions, not fire its demo code. Under the guard the rest of the file stays safe to use anywhere.

---

## Handy String Methods

Strings carry their own tools. `len()` is a function, the rest are methods.

```python
text = "  Hello World  "
print(len(text))         # 15
print(text.strip())      # Hello World
print(text.upper())      #   HELLO WORLD
print("a b  c".split())  # ['a', 'b', 'c']
```

`len()` counts every character, spaces included. Call `.strip()` first when the text came from a person. `.split()` with no argument splits on any whitespace and returns a list; pass a separator like `text.split(",")` to split on something else.

None of these change the original string. Strings are immutable, so each call returns a new value you must store or print.

---

## Summary

| Thing | Example | Note |
| --- | --- | --- |
| Print | `print("a", "b")` | Adds a newline and a space |
| Comment | `# note` | Runs to end of line |
| Docstring | `"""note"""` | A real string on the object |
| Block | `if x:` then indented lines | Colon ends header, 4 spaces/level |
| Variable | `name = "Ravi"` | No type keyword, `snake_case` |
| Multiple assignment | `a, b = 1, 2` | Built, then unpacked |
| Swap | `a, b = b, a` | No temp variable |
| Types | `int`, `float`, `str`, `bool` | Check with `type(x)` |
| f-string | `f"{name} is {age}"` | Expressions in `{}`, no space |
| Read input | `int(input("..."))` | `input()` always returns a `str` |
| Quotient, remainder | `q, r = divmod(a, b)` | Returns a pair, unpack it |
| Entry point | `if __name__ == "__main__":` | Runs on execute, not on import |
| String tools | `len(s)`, `s.strip()`, `s.split()` | Return new values |

---

## Common Mistakes

- Forgetting the colon. `if x > 5` is a syntax error; write `if x > 5:`.
- Writing `//` expecting a comment. `//` is floor division. Use `#`.
- Mixing tabs and spaces, which raises `TabError`. Use four spaces.
- Misaligning a block body, raising `IndentationError: unexpected indent`.
- Writing `true` or `false` instead of `True` and `False`, which raises `NameError`.
- Writing `input(int("Enter: "))`. The conversion goes outside: `int(input("Enter: "))`.
- Assuming `input()` gives a number. It gives a `str` even when the user types `20`.
- Forgetting the main guard, so the demo code runs on every import.
- Using `==` when you meant `=`. `=` assigns, `==` compares.
- Reaching for `&`, `|` and `~`. The words are `and`, `or` and `not`; the symbols are bitwise.
- Expecting `s.upper()` to change `s`. Strings are immutable, so it returns a new one.
- Expecting `float("4.50")` to keep the trailing zero. It prints `4.5`.

---

## Practice

The five questions for this topic live in this folder. Run each one on its own, try the commented `STARTER`, then scroll to the `SOLUTION`.

- [Question 01](./question_01.py)
- [Question 02](./question_02.py)
- [Question 03](./question_03.py)
- [Question 04](./question_04.py)
- [Question 05](./question_05.py)