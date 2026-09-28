# What is a List?

A list is an ordered collection of values. You can add, remove, and change items in place. It grows and shrinks as needed, so you never declare a size up front. Items keep their order. A list can hold different types together: `["apple", 3, 2.5, True, None]`.

---

## Creating and Indexing

Empty or not, square brackets make a list.

```python
print([1, 2, 3, 4], [])
print(list(range(5)))
print(list("abc"))
print(["apple", 3, 2.5, True, None])
```

Output:
```
[1, 2, 3, 4] []
[0, 1, 2, 3, 4]
['a', 'b', 'c']
['apple', 3, 2.5, True, None]
```

`list("abc")` splits the string into single characters: `['a', 'b', 'c']`.

Positions start at 0. `items[0]` is the first item, `items[-1]` is the last. Negative indexes count from the end.

```python
items = [1, 2, 3, 4]
print(items[0], items[-1], items[1])
```

Output:
```
1 4 2
```

```text
      +----+----+----+----+
Value:| 1  | 2  | 3  | 4  |
      +----+----+----+----+
Index:   0    1    2    3
```

Asking for an index that does not exist raises an error:

```python
items = [1, 2, 3, 4]
print(items[4])
```

Output:
```
IndexError: list index out of range
```

---

## Slicing Returns a New List

A slice takes a piece with `start:stop`.

```python
items = [1, 2, 3, 4]
print(items[1:3], items[:2], items[2:], items[::-1])
```

Output:
```
[2, 3] [1, 2] [3, 4] [4, 3, 2, 1]
```

The start is included, the stop is not. `items[1:3]` is index 1 and 2, not 3. Omitted start means 0, omitted stop means the end. `::-1` steps backwards and reverses the list.

A slice always creates a new list. The original is unchanged.

```python
items = [1, 2, 3, 4]
small = items[1:3]
small.append(99)
print(items, small)
items[1] = 20
print(items)
```

Output:
```
[1, 2, 3, 4] [2, 3, 99]
[1, 20, 3, 4]
```

So a slice gives a copy. An index assignment changes the original.

---

## Adding and Removing

```python
items = [1, 2, 3]
items.append(4)
print(items)
items.insert(1, 99)
print(items)
items.remove(2)
print(items)
items.pop()
print(items)
items.pop(0)
print(items)
items.clear()
print(items)
```

Output:
```
[1, 2, 3, 4]
[1, 99, 2, 3]
[1, 99, 3]
[1, 99]
[99]
[]
```

Errors:
- `remove(value)` raises `ValueError` if the value is not there.
- `pop()` on an empty list raises `IndexError`.
- `remove` only removes the first match.

---

## Reading a List

```python
items = [1, 2, 3, 4]
print(len(items))
print(2 in items)
print(items.count(2))
print(items.index(2))
for item in items:
    print(item)
```

Output:
```
4
True
1
0
1
2
3
4
```

`in` and `count` walk the whole list, so they are O(n).

---

## sort() Mutates, sorted() Returns

```python
items = [3, 1, 2]
items.sort()
print(items)

items = [3, 1, 2]
new = sorted(items)
print(items, new)

items = [3, 1, 2]
items = items.sort()
print(items)
```

Output:
```
[1, 2, 3]
[3, 1, 2] [1, 2, 3]
None
```

`sort()` changes the list in place and returns `None`. `sorted()` returns a new sorted list and leaves the original alone. `items = items.sort()` loses the list.

---

## Do Not Mutate While Looping

Removing items while looping over the same list skips items.

```python
items = [1, 2, 3, 4, 5]
for item in items:
    if item < 3:
        items.remove(item)
print(items)
```

Output:
```
[2, 3, 4, 5]
```

The loop skips `3` because `2` shifted into its position.

Safe patterns:

```python
items = [1, 2, 3, 4, 5]
kept = []
for item in items:
    if item >= 3:
        kept.append(item)
print(kept)
```

Or loop over a copy:

```python
items = [1, 2, 3, 4, 5]
for item in items.copy():
    if item < 3:
        items.remove(item)
print(items)
```

Output:
```
[3, 4, 5]
```

---

## Aliasing: Two Names, One List

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a, b)
```

Output:
```
[1, 2, 3, 4] [1, 2, 3, 4]
```

`b = a` does not copy the list. Both names point to the same list.

To copy:

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a, b)
```

Output:
```
[1, 2, 3] [1, 2, 3, 4]
```

---

## What Costs What

| Operation | Time |
|---|---|
| Read by index | O(1) |
| `append` | O(1) amortised |
| `insert` | O(n) |
| `pop()` (end) | O(1) |
| `pop(0)` / `remove` | O(n) |
| `in` / `count` / `index` | O(n) |
| `sort` | O(n log n) |
| Slice | O(n) |

O(1) means the same speed regardless of list size. O(n) gets slower as the list grows. Appending at the end is fast; inserting at the front is slow.

---

## Summary

| Python | What it does |
|---|---|
| `items = []` | empty list |
| `items.append(x)` | add to end |
| `items.insert(i, x)` | insert at position i |
| `items.remove(x)` | remove first matching value |
| `items.pop()` | remove and return last item |
| `items.pop(i)` | remove and return item at i |
| `len(items)` | number of items |
| `x in items` | check if x exists |
| `items.sort()` | sort in place, returns None |
| `sorted(items)` | return new sorted list |
| `items.copy()` | real copy, not alias |

---

## Common Mistakes

- Writing `items = items.sort()` — makes `items` become `None`.
- Using `items[len(items) - 1]` instead of `items[-1]`.
- Forgetting the stop of a slice is not included.
- Removing items while looping over the same list — skips items.
- Writing `b = a` and expecting a copy.
- Calling `remove` once and expecting all duplicates gone.
- Popping an empty list — raises `IndexError`.
- Assuming a slice changes the original list.

---

## Practice

The five questions for this topic live in this folder. Each is self-contained with a `STARTER` section and a runnable `SOLUTION`. Run them with:

```bash
python3 question_01.py
```

- [Question 01](./question_01.py)
- [Question 02](./question_02.py)
- [Question 03](./question_03.py)
- [Question 04](./question_04.py)
- [Question 05](./question_05.py)