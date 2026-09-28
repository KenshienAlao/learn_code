# What is a Dictionary?

A dict stores values under keys instead of under positions. A list is read by
number, `items[0]`. A dict is read by name, so the item itself tells you where
it lives.

```python
fruit_prices = {"apple": 3, "banana": 5}
print(fruit_prices["apple"])
```

```text
Output: 3

  fruit_prices

  +----------------+ :  +-----+
  | "apple"        | :  |  3  |
  +----------------+ :  |     |
  | "banana"       | :  |  5  |
  +----------------+ :  |     |
  +----------------+ :  +-----+

   keys                 values
   left of the colon    right of the colon
   the labels           the data
```

A dict grows as you add items. No size to declare, no index that shifts.

---

## Why Lookup Is Fast

Python works out a number from the key and jumps straight to the right spot. It
does not check `"banana"` first. Reading a value costs the same at three items
and at three million.

A list cannot do that. Looking for `"mango"` in
`["apple", "banana", "cherry", "kiwi", "mango"]` checks every element, because a
list knows positions, not labels.

```text
  A dict jumps.

  d["mango"] -> hash("mango") -> a number -> number % table size -> a bucket
                                                            +----------------+
                                                            | "mango": 7    |  <- here
                                                            +----------------+

  A list walks.

  ["apple", "banana", "cherry", "kiwi", "mango"]
      ^           ^           ^          ^          ^
      1           2           3          4          5  checked, no match,
                                                       gave up

  One jump, however big the dict is.
```

That jump is also why a key cannot change after you have used it. A changed key
gives a different number, so the dict would lose track of the slot the entry
sits in. Keys must be fixed values, which is the next section.

This is called **hashing**. You never do it by hand. It explains both the O(1)
timings and the fixed-key rule.

---

## Creating Dicts

```python
scores = {"a": 1}       # the literal, by far the most common
empty = {}              # an empty literal
point = dict(x=1, y=2)  # from keyword arguments
print(scores, empty, point)
```

```text
Output: {'a': 1} {} {'x': 1, 'y': 2}
```

`{}` is an **empty dict**, and that trips people up, because `{}` also looks
like an empty set. It is not. An empty set is `set()`; a non-empty one is
`{1, 2, 3}`.

An empty dict is **falsy**, so it drops straight into an `if`:

```python
counts = {}
if not counts:
    print("nothing yet")
```

```text
Output: nothing yet
```

`if len(counts) == 0` also works, just clumsier. There is no `.isEmpty()` method
on a dict.

A dict also keeps the order you insert keys in. Add `"apple"`, `"banana"`,
`"cherry"` and they always come back in that order, guaranteed in every current
version of Python.

---

## Keys Must Be Fixed

A key has to be a value Python can hash: `str`, `int`, `float`, `bool` and
`tuple`. A `list` and a `dict` are not.

```python
counts = {}
counts[["a", "b"]] = 1
```

```text
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
```

Not fussiness. A list can be changed after you store it, and then the number
Python worked out no longer matches the slot the entry sits in, so the dict
would lose track of its own data. A `dict` used as a key fails the same way.

A `tuple` works where a `list` does not, because a tuple cannot change once it
exists.

```python
print({("a", "b"): 1})
print({("a", ["b"]): 1})
```

```text
Output:
{('a', 'b'): 1}
TypeError: cannot use 'tuple' as a dict key (unhashable type: 'list')
```

A tuple holding a list still fails. The list inside it can change.

---

## Reading Values Safely

One way to read a value stops your program. The other does not.

```python
users = {"ravi": 20, "sana": 25}

print(users["ravi"])
print(users.get("priya"))
print(users.get("priya", "Not found"))
print("priya" in users)
print(users.get("ravi"))
```

```text
Output:
20
None
Not found
False
20
```

Square brackets are strict. `users["priya"]` raises, since there is no `"priya"`
key and Python assumes you know that:

```text
KeyError: 'priya'
```

No default can be pulled out of `d["key"]`. It has the key or it raises. `.get`
is the forgiving form: `None` for a missing key, or your own default if you
passed one. `key in d` is the membership test, answering `True` or `False`.

```text
  expression                     key missing            program
  ----------------------------   -------------------   -----------
  d["priya"]                     KeyError               stops
  d.get("priya")                 returns None           keeps going
  d.get("priya", "Not found")    returns "Not found"    keeps going
  "priya" in d                   returns False           keeps going
```

Use `in` or `.get` whenever the key might be missing, and square brackets only
for keys you are certain are there. A stored `None` is legal, so
`users.get(name) is not None` cannot tell "not found" from "found, and the value
is `None`". `in` can.

---

## Adding, Updating and Deleting

There is no separate add step. One assignment creates the key if it is missing
and replaces the value if it is not.

```python
counts = {}
counts["apple"] = 1
print(counts)
counts["apple"] = 2
print(counts)
```

```text
Output:
{'apple': 1}
{'apple': 2}
```

`"apple"` is now `2`, not `3`. Assignment overwrites. To accumulate, read the
old value first, which is what the counting pattern does.

Merging applies that to every key:

```python
a = {"x": 1, "y": 2}
b = {"y": 20, "z": 3}

for key in b:
    a[key] = b[key]
print("Method 1 (for key in b):", a)

c = {"x": 1, "y": 2}
c.update(b)
print("Method 2 (c.update(b)):", c)
```

```text
Output:
Method 1 (for key in b): {'x': 1, 'y': 20, 'z': 3}
Method 2 (c.update(b)): {'x': 1, 'y': 20, 'z': 3}
```

Same answer both ways, and the shared `"y"` is **20**, not 22. Merging
overwrites. The loop lets you change each key on the way through.

`setdefault` does the opposite. It inserts only if the key is absent, and returns
the value either way.

```python
scores = {"ravi": 20}
print(scores.setdefault("ravi", 0))
print(scores.setdefault("amina", 0))
print(scores)
```

```text
Output:
20
0
{'ravi': 20, 'amina': 0}
```

Read it as "set this default only if it is not already there".

Deleting comes as a strict pair and a forgiving one:

```python
scores = {"ravi": 20, "sana": 25}

del scores["sana"]        # KeyError if the key is missing
print(scores.pop("ravi")) # KeyError if missing, returns 20
print(scores.pop("nobody", "gone"))
scores.clear()            # empties the dict in place
```

```text
Output:
20
gone
```

A real use is a phonebook. Two parallel lists, one loop, and the index pairs
each name with its own number:

```python
names = ["Ravi", "Sana", "Arun"]
phones = ["9876543210", "9876500011", "9123456780"]

phonebook = {}
for index in range(len(names)):
    phonebook[names[index]] = phones[index]

for name in phonebook:
    print(f"{name}: {phonebook[name]}")
print("Phonebook size:", len(phonebook))
print("Priya's number:", phonebook.get("Priya", "Not found"))
```

```text
Output:
Ravi: 9876543210
Sana: 9876500011
Arun: 9123456780
Phonebook size: 3
Priya's number: Not found
```

`range(len(names))` gives one index per name, and using that same index on both
lists is what keeps the pairs together. `zip(names, phones)` does it in one
line.

---

## Iterating a Dict

```python
users = {"ravi": 20, "sana": 25}

for name in users:
    print(name)

for name in users.keys():
    print(name)

for age in users.values():
    print(age)

for name, age in users.items():
    print(name, age)
```

```text
Output:
ravi
sana
ravi
sana
20
25
ravi 20
sana 25
```

A plain `for key in d` gives the **keys only**. This is the mistake people make
most often, because the loop looks like it should be walking the whole dict.
`for key, value in d.items():` is the one you want most, since it hands you both
without a second lookup.

You can also test for a value:

```python
users = {"ravi": 20, "sana": 25}

if 25 in users.values():
    print("value is there")
if "ravi" in users:
    print("key is there")
```

```text
Output:
value is there
key is there
```

`25 in users.values()` is O(n), because it must look at every value before it can
say no. Testing a key is O(1). And insertion order makes the loop predictable:
first key in, first key out.

---

## The Counting Pattern

The most useful thing people do with a dict. To count how often each item
appears, loop over the items and run one line:

```python
counts[item] = counts.get(item, 0) + 1
```

Three parts, and all are needed. `counts.get(item, 0)` reads the running count,
giving `0` the first time an item is seen and the real number every time after.
`+ 1` adds this occurrence. The assignment on the left writes the total back,
creating the key on the very first sighting.

```python
text = "the cat and the dog and the cat"
words = text.split()
print("Words:", words)

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
for word in counts:
    print(f"{word}: {counts[word]}")
```

```text
Output:
Words: ['the', 'cat', 'and', 'the', 'dog', 'and', 'the', 'cat']
{'the': 3, 'cat': 2, 'and': 2, 'dog': 1}
the: 3
cat: 2
and: 2
dog: 1
```

Trace it and the trick is obvious:

```text
  word   counts.get(word, 0)    + 1     counts now holds
  ----   -------------------    ---     -----------------------------
  the    0    (key missing)     1       {'the': 1}
  cat    0    (key missing)     1       {'the': 1, 'cat': 1}
  and    0    (key missing)     1       {'the': 1, 'cat': 1, 'and': 1}
  the    1    (found it)        2       {'the': 2, 'cat': 1, 'and': 1}
  and    1    (found it)        2       {'the': 2, 'cat': 1, 'and': 2}
  the    2    (found it)        3       {'the': 3, 'cat': 1, 'and': 2}
```

`"the"` prints first because it was inserted first, not because it has the
biggest count.

Grouping items into lists is the same pattern with a list instead of a number.
`setdefault` gives the shorter form:

```python
words = ["apple", "avocado", "banana", "blueberry", "cherry", "carrot"]

groups = {}
for word in words:
    groups.setdefault(word[0], []).append(word)

for letter in groups:
    print(f"{letter} -> {groups[letter]}")
```

```text
Output:
a -> ['apple', 'avocado']
b -> ['banana', 'blueberry']
c -> ['cherry', 'carrot']
```

The plain spelling is `if first not in groups: groups[first] = []` and then
`groups[first].append(word)`. `setdefault` does both in one step and hands the
list back, so `.append()` chains onto it.

`collections` has a `defaultdict` that removes even the `.get`:

```python
from collections import defaultdict

counts = defaultdict(int)
for word in words:
    counts[word[0]] += 1
print(dict(counts))
```

```text
Output: {'a': 2, 'b': 2, 'c': 2}
```

---

## Dict Comprehensions

A dict comprehension builds a dict in one line, the way a list comprehension
builds a list. It is a loop written sideways:

```python
pairs = [("a", 1), ("b", 2)]

d = {}
for key, value in pairs:
    d[key] = value
print(d)

d = {key: value for key, value in pairs}
print(d)
```

```text
Output:
{'a': 1, 'b': 2}
{'a': 1, 'b': 2}
```

Add an `if` at the end to keep only some entries:

```python
scores = {"ravi": 20, "sana": 5, "tom": 40}
print({name: age for name, age in scores.items() if age >= 10})
```

```text
Output: {'ravi': 20, 'tom': 40}
```

There is a counting form, `{word: 1 for word in words}`, but think first. Every
word gets 1 and duplicates are dropped, so `["a", "b", "a"]` gives
`{'a': 1, 'b': 1}` when you wanted `{'a': 2, 'b': 1}`. The counting pattern
above is the one that is right.

Use a comprehension when it stays on one line and still reads aloud. Anything
longer belongs in a real loop. A comprehension always builds a **new** dict, so
it cannot change one in place.

---

## Time Complexity

| Operation | Average |
| --- | --- |
| read a value, `d[k]` | O(1) |
| write a value, `d[k] = v` | O(1) |
| test a key, `k in d` | O(1) |
| delete, `del d[k]`, `d.pop(k)` | O(1) |
| iterate the dict | O(n) |
| search among the values, `v in d.values()` | O(n) |

The O(1) rows are averages, and they are fast for one reason: the hashing from
the early section. Hash the key, jump to the slot, done. The O(n) rows are slow
because they must touch every entry.

---

## Summary

| Idea | Python |
| --- | --- |
| make a dict | `{"a": 1}` or `dict(a=1)`; `{}` is a dict, `set()` is a set |
| empty dict is falsy | `if not d:` |
| store under a name | `d[k] = v` creates the key, or overwrites the value |
| keys must be fixed | `str`, `int`, `float`, `bool`, `tuple`; never a list or dict |
| read a value | `d[k]` raises `KeyError`; `d.get(k, default)` does not |
| ask if a key is there | `k in d` |
| merge another dict | `d.update(other)`, shared keys overwritten |
| insert only if absent | `d.setdefault(k, v)` |
| delete | `del d[k]`, `d.pop(k, default)`, `d.clear()` |
| loop over pairs | `for k, v in d.items():`; `for k in d` gives keys only |
| count things | `counts[k] = counts.get(k, 0) + 1` |
| build in one line | `{k: v for k, v in pairs}`, always a new dict |
| order | insertion order, guaranteed |

---

## Common Mistakes

- Using a list as a key. `d[["a"]] = 1` raises `TypeError: unhashable type: 'list'`. Use a `tuple`.
- Expecting `d["missing"]` to give `None`. It raises `KeyError`. `.get()` returns `None`.
- Assigning to an existing key and finding the old value gone. `counts[w] = 1` throws the total away.
- Writing `{}` and expecting an empty set. An empty set is `set()`.
- Iterating a dict directly and getting keys when you wanted values. Use `d.items()`.
- Forgetting the comma in `d.get(key, default)`. With no comma you get `None`, and the default is never stored.
- Counting with `if v in d:`. That tests keys. You want `v in d.values()`, which is O(n), not O(1).
- Assuming a dict loses insertion order. It keeps it, and it is guaranteed.
- Calling `d.size()`. The size is `len(d)`, a function and not a method.
- Using a comprehension to change a dict in place. It builds a new dict; the original is untouched.
- Changing a dict while looping over it. That raises `RuntimeError: dictionary changed size during iteration`.

---

## Practice

Five questions for this topic sit in this same folder. Each is self contained,
with a commented `STARTER` block to attempt and a complete runnable `SOLUTION`.
Run them one at a time, starting with `python3 question_01.py`.

- [Question 01](./question_01.py)
- [Question 02](./question_02.py)
- [Question 03](./question_03.py)
- [Question 04](./question_04.py)
- [Question 05](./question_05.py)
