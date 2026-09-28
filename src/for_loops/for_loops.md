# What are For Loops in Python?

A `for` loop walks a sequence of values and runs a block of code once per value. The sequence can be a range of numbers, a string, a list, or the keys of a dict. You never set up a counter: the loop produces the values, and the name after `in` receives the current one.

---

## The Basic for Loop

`range(n)` supplies the numbers 0 up to `n - 1`, one at a time. The loop variable receives them.

```python
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

Note the colon at the end of the header and the indented body. Leave out the colon and you get a `SyntaxError`; the indentation is how Python knows which lines are the body.

`i` is only a label, so `count` or `banana` works the same. `range` is a sequence, not a list, so you can print it: `print(range(5))` gives `range(0, 5)`.

Inside the body you write ordinary Python. `if` / `elif` / `else` pick a branch, `%` gives a remainder, and `and` joins two tests. Put the most specific test first:

```python
for i in range(1, 6):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    else:
        print(i)
```

Output:
```
1
2
Fizz
4
Buzz
```

Testing `and` first is what sends 15, divisible by both, to the branch that wants it.

---

## The Stop Is Exclusive

This is the idea that costs the most marks. `range` includes the start and excludes the stop, so `range(5)` gives five values and 5 is not one of them.

```text
call            values                     count
range(5)        0 1 2 3 4                  5
range(1, 5)     1 2 3 4                    4   you wanted 5 too
range(1, 6)     1 2 3 4 5                  5   the one you want
```

The stop is a "stop here" marker, not a "last value" marker. To include 5 you must ask for `range(6)`, and to count from 1 you ask for `range(1, 6)`. To print 1 through 10, write `range(1, 11)`.

Habit that saves you: write down the values you expect first. If you expect ten numbers, ten is what goes in `range`.

---

## `range(start, stop, step)`

The first argument is where to start, the second is the exclusive stop, the third is the step: how much to add each time.

| Call | Values |
| --- | --- |
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 11)` | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(10, 0, -1)` | 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 |
| `range(0, 1, 0)` | raises `ValueError: range() arg 3 must not be zero` |
| `range(0, 1, 0.1)` | raises `TypeError: 'float' object cannot be interpreted as an integer` |

A negative step turns the loop around, and the exclusive-stop rule still applies, so `range(10, 0, -1)` ends at 1. `range` is whole numbers only, so `0.1` is a `TypeError`, not a quiet approximation. To count in fractions, use a `while` loop with your own counter, or multiply an integer range: `for i in range(11): print(i / 10)`.

**Walking a list from the end.** `range(len(items) - 1, -1, -1)` gives the last index down to 0, which is how you build a reversed copy by hand:

```python
items = ["a", "b", "c", "d"]
reversed_items = []

for i in range(len(items) - 1, -1, -1):
    reversed_items.append(items[i])

print("Reversed list:", reversed_items)
```

Output:
```
Reversed list: ['d', 'c', 'b', 'a']
```

The original is untouched because you built a new list. `len()` asks any sequence how long it is, and it is a free function, not a method: `len(items)`, never `items.len()`.

---

## Looping Over Strings, Lists and Dicts

A `for` over a string gives one character at a time, over a list one item at a time, and over a dict the keys, not the values.

```python
for ch in "cat":
    print(ch)

for color in ["red", "green", "blue"]:
    print(color)

scores = {"alice": 90, "bob": 75}
for name in scores:
    print(name)
```

Output:
```
c
a
t
red
green
blue
alice
bob
```

For keys and values together use `scores.items()`.

Two results that look identical but come from different operations:

```python
print(list("abc"))
print("a b c".split())
```

Output:
```
['a', 'b', 'c']
['a', 'b', 'c']
```

`list("abc")` splits a string into characters. `"a b c".split()` cuts on the spaces and keeps the pieces as whole words.

**The accumulator pattern.** Start a total before the loop, add inside, print after:

```python
numbers = [10, 20, 30, 40, 50]
total = 0

for value in numbers:
    total += value

print("Sum of the list:", total)
```

Output:
```
Sum of the list: 150
```

The same shape with a counter and an `if` counts how many times a value appears:

```python
numbers = [10, 20, 10, 30, 10]
count = 0

for value in numbers:
    if value == 10:
        count += 1

print(f"Times 10 appears: {count}")
```

Output:
```
Times 10 appears: 3
```

---

## `enumerate()`

When you need both the index and the item, `enumerate` hands you both, starting the counter at 0 and stepping by 1 for you.

```python
names = ["ana", "ben", "cleo"]

for index, name in enumerate(names):
    print(f"{index}: {name}")
```

Output:
```
0: ana
1: ben
2: cleo
```

Read the header as "unpack each item into two names". `enumerate` produces pairs, and the comma splits each pair into `index` and `name`. That unpacking is a Python feature you will see everywhere. Pass `start=1` and the counter begins at 1: `1: ana`, `2: ben`, `3: cleo`.

---

## `zip()`

`zip` walks two lists together, pairing them item by item.

```python
names = ["ana", "ben", "cleo"]
scores = [90, 75, 100]

for name, score in zip(names, scores):
    print(name, score)
```

Output:
```
ana 90
ben 75
cleo 100
```

Here is the trap, and nothing complains about it. `zip` stops when the shorter list runs out and drops the leftovers:

```python
a = [1, 2, 3]
b = ["x", "y"]

for num, letter in zip(a, b):
    print(num, letter)
```

Output:
```
1 x
2 y
```

The `3` was never paired and the loop ended without an error. When the lengths might not match, check them first with `if len(a) != len(b):`.

---

## while Loops

Use `for` when you know what you are walking over. Use `while condition:` when you do not know the count in advance.

```python
count = 3

while count > 0:
    print(count)
    count -= 1

print("Liftoff!")
```

Output:
```
3
2
1
Liftoff!
```

The trace of that run:

```text
count = 3
count > 0 ?  yes  -> print 3, count becomes 2
count > 0 ?  yes  -> print 2, count becomes 1
count > 0 ?  yes  -> print 1, count becomes 0
count > 0 ?  no   -> leave the loop, print Liftoff!
```

Every `while` needs something in the body that changes the condition, or it runs forever.

Python has no do-while keyword, because `while True:` with a `break` covers the need:

```python
n = 0

while True:
    n += 1
    if n >= 3:
        break

print("n is", n)
```

Output:
```
n is 3
```

---

## break, continue, and the Loop else

`break` leaves the loop immediately. `continue` skips to the next item. Both are straightforward:

```python
for i in range(1, 6):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)
```

Output:
```
1
2
4
```

A loop can also have an `else:` block, and it runs only if the loop finished without a `break`. That is the whole rule: the `else` is not the "otherwise" of the body, it is the "nothing broke out" case. Here it helps in a search loop where `break` means "found it":

```python
numbers = [4, 8, 15, 16, 23]
target = 42

for n in numbers:
    if n == target:
        print("Found it at index", numbers.index(n))
        break
else:
    print("Not found")
```

Output:
```
Not found
```

Change `target` to `15` and the `break` fires, printing `Found it at index 2` and skipping the `else`. Without the `else` you would need a flag set before the loop and checked after it.

---

## Nested Loops

An inner loop inside an outer one. The inner loop finishes completely on every turn of the outer loop.

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row}{col}", end="  ")
    print()
```

Output:
```
11  12  13
21  22  23
31  32  33
```

The `end="  "` stops `print` adding a newline each time, and the lone `print()` ends the row. The total passes is the two lengths multiplied, so nesting grows fast:

```text
outer runs 3 times (range(1, 4) -> 1, 2, 3)
inner runs 3 times (range(1, 4) -> 1, 2, 3)
total   3 * 3 = 9 prints
```

---

## List Comprehensions

A comprehension is the compact form of a loop that builds a list. Same work, both ways:

```python
numbers = [1, 2, 3, 4]
doubled = []
for n in numbers:
    doubled.append(n * 2)

print(doubled)
```

Output:
```
[2, 4, 6, 8]
```

```python
numbers = [1, 2, 3, 4]
doubled = [n * 2 for n in numbers]

print(doubled)  # [2, 4, 6, 8]
```

Output:
```
[2, 4, 6, 8]
```

Read it inside out: "take `n * 2`, for each `n` in `numbers`". The filter form puts an `if` after the sequence:

```python
nums = [-3, 5, -1, 8, 0, 12]
print([n for n in nums if n > 0])
```

Output:
```
[5, 8, 12]
```

A comprehension is still one pass over the data, so it is the same speed as the loop, just denser. Use it only while it stays short; the moment you need three or four lines of logic, write a real loop.

The classic mistake is calling `.append()` inside a comprehension. A comprehension produces values, it has no body, so there is nowhere for the call to go. Write `[n * 2 for n in numbers]`, or write a plain loop. Never both.

---

## Do Not Mutate a List While Looping Over It

This trap silently produces wrong answers. When you loop over a list, Python walks it by position. Remove an item partway through and everything after it slides down a slot, so the loop skips whatever moved into the slot it was about to read.

```python
nums = [1, 2, 3, 4, 5]

for n in nums:
    if n < 3:
        nums.remove(n)

print(nums)
```

Output:
```
[2, 3, 4, 5]
```

The answer should be `[3, 4, 5]`. The `2` survived, never visited:

```text
index 0  value 1  -> 1 < 3, remove it. list is now 2 3 4 5
index 1  value 3  <- the 2 slid into slot 1, we read slot 1 and got 3
                     3 is not < 3, so it is kept
index 2  value 4  -> kept
index 3  value 5  -> kept
index 4  past the end

result [2, 3, 4, 5]   but it should be [3, 4, 5]
```

The safe pattern is to build a new list:

```python
nums = [1, 2, 3, 4, 5]
kept = []

for n in nums:
    if n >= 3:
        kept.append(n)

print(kept)
```

Output:
```
[3, 4, 5]
```

`[n for n in nums if n >= 3]` does the same in one line, and you can also loop over a copy with `for n in nums[:]:`. The rule: if the loop changes the length of the list it is looping over, build a new list.

---

## Summary

| Task | Python |
| --- | --- |
| Repeat n times, or 1 to 10 | `range(n)` / `range(1, 11)` |
| Count by twos, or count down | `range(0, 10, 2)` / `range(10, 0, -1)` |
| Over a list, string or dict | `for x in items:` / `for ch in text:` / `for k in d:` |
| Index and item together | `for i, v in enumerate(items):` |
| Two lists in step | `for a, b in zip(xs, ys):` |
| Leave early, or skip one | `break` / `continue` |
| Search comes up empty | `for ... else:` |
| Build a list from a loop | `[x * 2 for x in items]` |

1. `range()` excludes the stop value. Add one when you want an upper bound included.
2. A `for` loop walks a sequence, not a counter. The same syntax works for numbers, strings, lists and dict keys.
3. The loop variable only exists once the loop runs, so if the loop ran zero times there is no name.

---

## Common Mistakes

- Writing `range(1, 5)` when you meant 1 to 5 inclusive, because you were thinking `<=`. Use `range(1, 6)`.
- Forgetting the colon. `for i in range(5)` is a `SyntaxError`; it needs `for i in range(5):`.
- Expecting the stop value to be printed. `range(1, 6)` gives 1 to 5, not 1 to 6.
- Writing `i++` in the loop header. There is no update clause and no `++` operator; use `i += 1`.
- Writing `items.size()` instead of `len(items)`. `len` is a free function, not a method.
- Removing items from a list while looping over it, which silently skips elements and gives a wrong answer.
- Calling `.append()` inside a comprehension. A comprehension produces values, it has no body.
- Using `zip` on two lists of different lengths and losing the extra data with no error.
- Assuming the loop variable exists outside the loop. If the loop never ran, you get a `NameError`.

---

## Practice

The five questions for this topic live in this same folder. Each is self contained, with a commented `STARTER` to attempt and a runnable `SOLUTION`. Run them one at a time with `python3 question_01.py` and so on.

- [Question 01](./question_01.py)
- [Question 02](./question_02.py)
- [Question 03](./question_03.py)
- [Question 04](./question_04.py)
- [Question 05](./question_05.py)