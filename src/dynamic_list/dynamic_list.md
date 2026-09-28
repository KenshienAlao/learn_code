# What is a Dynamic List?

A static array is a block of memory with a capacity you pick up front. A dynamic array is
the same idea, except the block grows for you when it runs out of room. A Python `list` is
a dynamic array, which is why you never think about capacity when you use one.

The practical consequence is worth stating on its own: **`append` never fails because the
list got full.**

```python
fruits = []
fruits.append("Banana")
fruits.append("Apple")
fruits.append("Grapes")

print(fruits)
print(len(fruits))
```

```text
['Banana', 'Apple', 'Grapes']
3
```

No capacity to pass in, no error to catch. The interesting part is the memory work that
happened underneath those three lines, and that is what this lesson is about.

---

## Static and Dynamic Arrays

Start with the static version, because the dynamic one is only a difference from it.

A static array has a capacity chosen once, at creation time. It never changes. Here is a
block of four slots with three of them used.

```text
A static array: capacity chosen up front, never changed

        0          1          2          3
    "Banana"   "Apple"    "Grapes"   <empty>
    <-------- size: 3 -------->^  ^ capacity: 4
```

Two numbers, and they drift apart.

- **size** is how many slots hold real data. In Python this is `len(items)`.
- **capacity** is how many slots the block can hold in total. A Python list will not tell
  you this number.

The moment you create a list, size is 0 while capacity is already some room reserved. As
you append, size climbs one at a time and capacity only moves when the block fills.

Reading by index is O(1), because the address of slot `i` is the start address plus `i`
times the slot width. `fruits[0]` and `fruits[9999]` cost exactly the same.

Inserting at the front is a different story. Every following item has to slide one place
right so index 0 is free for the newcomer.

```text
Before insert(0, "Lemon")           After insert(0, "Lemon")

    0          1         2          3       0          1          2         3
"Banana"  "Apple"   "Grapes"  <empty>   "Lemon"  "Banana"  "Apple"   "Graces"
                                            ^ all three moved one slot right
```

That is O(n), because it touches every item already in the list. Deleting from the front is
the mirror image: everything slides one place left to close the gap, and that is also O(n).

So a fixed block has two problems. It fills up and can never hold another item. And
inserting or deleting anywhere other than the end costs O(n).

The dynamic array fixes the first problem from the inside. When the block fills, a bigger
block is allocated, every item is copied into it, and only then is the old block thrown
away.

```text
Step 1: full                          Step 2: allocate 8, copy across

    0          1         2         3          0          1         2         3    4    5    6    7
"Banana"  "Apple"  "Grapes"  "Lemon"    "Banana"  "Apple"  "Grapes"  "Lemon"   ?    ?    ?    ?
                               old block gone
    size: 4  capacity: 4                size: 4  capacity: 8
```

Size did not change. Growing is about capacity only, and that is the distinction behind
most of the confusion in this topic.

The copy is O(n), but it happens rarely. Growing by exactly one slot would copy on every
append. Instead the runtime grows by a **growth factor**, and the spare room pushes the
next resize a long way away. The sizes do not double every time. The next section shows
the real pattern.

---

## What Actually Happens When a List Grows

You can watch the resize happen, because Python will tell you the memory a list object
occupies.

```python
import sys

items = []
print("empty list:", sys.getsizeof(items), "bytes")

for value in range(20):
    items.append(value)
    print(f"len {len(items):>2}   bytes {sys.getsizeof(items):>3}")
```

Here is that run, with the reserved slots worked out. On a 64-bit machine an empty list is
56 bytes and every pointer slot adds 8, so reserved slots is `(bytes - 56) // 8`.

| `len(items)` | `sys.getsizeof` | reserved slots | what happened |
| --- | --- | --- | --- |
| 0 | 56 | 0 | base object, no slots yet |
| 1 | 88 | 4 | resize |
| 2 to 4 | 88 | 4 | flat, then full |
| 5 | 120 | 8 | resize |
| 6 to 8 | 120 | 8 | flat, then full |
| 9 | 184 | 16 | resize |
| 10 to 16 | 184 | 16 | flat, then full |
| 17 | 248 | 24 | resize |
| 18 to 20 | 248 | 24 | flat, then full |
| 25 | 312 | 32 | resize |

The finding: the byte size stays flat for several appends, then jumps in one step. **Each
jump is the resize.** A flat number means the item landed in a slot that was already
reserved. A jump means a bigger block was allocated and the pointers were copied across.

The reserved slots column is the growth factor made visible: 4, then 8, then 16, then 24,
then 32. The step up is shrinking each time, 4 slots, then 8, then 8. The sizes go up by
increasing amounts, so do not go looking for a clean doubling past 16.

Why do the numbers look like that at all? A Python list is a block of pointers to the
objects, not the objects themselves, so the size measures the pointer block.

```python
import sys

small = []
for value in (1, 2, 3):
    small.append(value)

big = []
for value in (10 ** 40, 10 ** 41, 10 ** 42):
    big.append(value)

print("small ints in a list:", sys.getsizeof(small), "bytes")
print("huge ints in a list:", sys.getsizeof(big), "bytes")
```

```text
small ints in a list: 88 bytes
huge ints in a list: 88 bytes
```

Identical list size, wildly different item sizes, identical number. So never read
`sys.getsizeof` as the total memory your data occupies. It does not count the objects the
list points at.

---

## Why Python Hides All This

You cannot set a list's capacity, ask for its capacity, or switch off the over-allocation.
All three are the runtime's job, not yours.

```python
items = [0] * 4      # four items, not four slots of room
print(items)

items = list()
print(items)

try:
    items.capacity
except AttributeError as err:
    print("AttributeError:", err)
```

```text
[0, 0, 0, 0]
[]
AttributeError: 'list' object has no attribute 'capacity'
```

`[0] * 4` makes four items. It repeats a value, it reserves nothing. `list()` takes no
arguments at all. And `capacity` is not an attribute, so asking for it raises
`AttributeError`.

That buys you three things. No capacity argument when you make a list. No "array is full"
error, because `append` always succeeds. No copying loop to forget when the list grows. An
entire category of bugs disappears.

Two costs remain. The list holds a little more memory than it strictly needs, because of
the spare slots. And inserting or deleting in the middle of a long list is still slow,
because the items have to move. The honest summary: a list is fast for reading and for
adding at the end, and slow for inserting or removing anywhere else.

You can rebuild the mechanism by hand, and it is worth seeing once.

```python
class DynamicArray:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def add(self, data):
        if self.size >= self.capacity:
            self.grow()
        self.array[self.size] = data
        self.size = self.size + 1

    def grow(self):
        self.capacity = self.capacity * 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def __str__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"


data = DynamicArray(4)
for value in ["Samsung", "Xiaomi", "iPhone", "Nokia", "OnePlus"]:
    data.add(value)
    print(f"added {value:<8} capacity {data.capacity}  size {data.size}  {data}")
```

```text
added Samsung  capacity 4  size 1  [Samsung]
added Xiaomi   capacity 4  size 2  [Samsung, Xiaomi]
added iPhone   capacity 4  size 3  [Samsung, Xiaomi, iPhone]
added Nokia    capacity 4  size 4  [Samsung, Xiaomi, iPhone, Nokia]
added OnePlus  capacity 8  size 5  [Samsung, Xiaomi, iPhone, Nokia, OnePlus]
```

`__init__` reserves the room and sets size to 0. `add` checks for room before it writes,
then bumps size. `__str__` prints only the filled slots, so the empty ones stay hidden.

Read `grow` line by line, because this is the step people get wrong. It creates a new,
bigger block. It copies every existing item across into that block, using a `for` loop over
`range(self.size)` so it touches only the slots that hold real data. Only then does it
point `self.array` at the new block, and that is the moment the old block becomes garbage.
Three steps, in that order, always.

Skip the copy and the data is gone, silently. Nothing complains, the names all look right,
and the values are gone:

```python
def grow_wrong(array, size):
    return [None] * (size * 2), size * 2


old = ["Banana", "Apple", "Grapes"]
print("before:", old)
print("after: ", grow_wrong(old, 3))
```

```text
before: ['Banana', 'Apple', 'Grapes']
after:  ([None, None, None, None, None, None], 6)
```

`size` is a fact about your data, and only the room reserved for that data is allowed to
change.

The remaining methods are bookkeeping you can predict. `insert` walks backwards from the
end, so no value gets overwritten before it moves to its new slot. `pop_last` reads the
last filled slot, blanks it, and lowers the size, so nothing moves. `is_empty` is just
`self.size == 0`. Writing all of this by hand is what Python does for you every time
`append` finds a full block.

---

## Time Complexity

| Operation | Cost | Why |
| --- | --- | --- |
| Read by index, `items[i]` | O(1) | Address is start plus the offset |
| `append` | O(1) amortised | Usually one write, occasionally a resize |
| `insert` at the start | O(n) | Every item shifts one slot right |
| `insert` at the end | O(1) | The same work as `append` |
| `pop` at the start | O(n) | Every remaining item shifts one slot left |
| `pop` at the end | O(1) | Just a smaller size, nothing moves |
| `item in items`, `items.count(x)` | O(n) | Every item is compared |
| Resize | O(n) | Copies every item, but happens rarely |

Amortised, in one sentence: a single `append` is occasionally slow because the block had
to grow, but that happens rarely enough that the average cost per append stays O(1).

Here is that gap in plain numbers. Growing a list of ten thousand items with `append` is
fast, because the resizes are rare. Inserting at the front of a list of ten thousand items
is slow, because every one of those items has to move.

```python
count = 10000

appended = []
for value in range(count):
    appended.append(value)

fronted = []
moved_by_insert = 0
for value in range(count):
    fronted.insert(0, value)
    moved_by_insert += len(fronted)   # every item already in the list shifts right

print(f"{count} appends:       1 write each, resizes are rare")
print(f"{count} front inserts: {moved_by_insert} item moves")
```

```text
10000 appends:       1 write each, resizes are rare
10000 front inserts: 50005000 item moves
```

Fifty million moves to build one list. If you are inserting at the front in a loop,
appending instead and walking the result backwards at the end is almost always the fix.

---

## Summary

| Concept | What a Python `list` does |
| --- | --- |
| Capacity | Managed by the runtime, not visible to you |
| Size | `len(items)` |
| Full | Never announced, `append` always succeeds |
| Grow step | Handled inside `append`, over-allocated not doubled |
| Read by index | O(1) |
| Add or remove at the end | O(1) amortised |
| Insert or remove at the start | O(n) |
| `sys.getsizeof` measures | The pointer block, not the items |

---

## Common Mistakes

- Expecting a list to tell you its capacity. `items.capacity` raises `AttributeError`, and
  only `len(items)` is available, which is size.
- Trying to set a capacity when you create a list. `[0] * 4` repeats a value four times. It
  reserves nothing.
- Expecting `append` to be slow because of resizing. It is O(1) amortised, and a list that
  has already grown holds its speed.
- Inserting at the front of a long list and wondering why it crawls. `insert(0, x)` moves
  every item already in the list.
- Assuming a list stores the items themselves. It stores pointers to them, which is why
  `sys.getsizeof` gives the same number for a list of small ints and a list of enormous
  ones.
- Reading `sys.getsizeof` as the total memory of your data. It counts the pointer block
  only.
- Expecting the byte size to keep doubling. It doubles twice and then stops doubling: the
  reserved slots in the run above went 4, 8, 16, 24, 32.
- Calling `pop()` on an empty list. It raises `IndexError: pop from empty list`.

---

## Practice

The five questions walk the same ground in order: tracking size and capacity by hand while
appending, watching every item shift right on an insert at index 0, watching every item
shift left on `pop(0)`, measuring a real list with `sys.getsizeof`, and finally writing
the mini `DynamicArray` class with a `grow` that actually copies. Run them in order.

- [Question 01](./question_01.py)
- [Question 02](./question_02.py)
- [Question 03](./question_03.py)
- [Question 04](./question_04.py)
- [Question 05](./question_05.py)
