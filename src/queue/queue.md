# What is a Queue?

A queue is a collection where you add items at one end and take them out at the other end, so the item that arrived first is the first one served. That rule is called **FIFO**, First In First Out. In Python a queue is just a list. The back of the queue is the end of the list, and the front of the queue is index `0`.

You meet queues constantly: a printer working through a list of jobs, a line of people waiting, a music playlist, a task queue inside a program.

---

## The FIFO Idea

FIFO means no skipping the line. The oldest item comes out first, every time. Picture a printer with three jobs waiting.

![Queue FIFO](/assets/queue.webp)

The front of the queue is the start of the list (index `0`) and the back is the end. `append` adds to the back and `pop(0)` takes from the front. The diagram above is drawn front-first with the front on the left, which is how a queue is usually pictured. A list grows left to right from index `0`. That mismatch is why `append` goes to the back and `pop(0)` takes from the front.

---

## The Five Operations

Everything a queue does is a list operation.

**Add to the back.** `append` puts the item at the end of the list, which is the back of the queue.

```python
queue = ["Spongebob", "Patrick"]
queue.append("Squidward")
print(queue)

```

```text
['Spongebob', 'Patrick', 'Squidward']

```

**Take from the front.** `pop(0)` removes the item at index `0` and hands it back. That item is gone.

```python
queue = ["Spongebob", "Patrick", "Squidward"]
print(queue.pop(0))
print(queue)

```

```text
Spongebob
['Patrick', 'Squidward']

```

**Look at the front without removing it.** Index `0` reads the front item and leaves it in place, and `len(queue)` gives the size.

```python
queue = ["Spongebob", "Patrick", "Squidward"]
print(queue[0], len(queue))

```

```text
Spongebob 3

```

**The empty check.** `if not queue:` asks whether the queue is empty, because an empty list is falsy and a list holding anything is truthy. That is not a queue rule, it is how Python decides if a value counts as true, the same as `if name:`.

**The two loops.** `while queue:` drains the queue completely, and the condition is the guard, so the loop stops the moment the last item is taken. This is question 01: the names come out in the order they went in, and the queue ends empty.

```python
queue = ["Spongebob", "Patrick", "Squidward"]

while queue:
    print(queue.pop(0))

print("Queue is now:", queue)

```

```text
Spongebob
Patrick
Squidward
Queue is now: []

```

A plain `for item in queue:` walks the queue from front to back and changes nothing, printing the same three names. Use it when you only want to read.

Draining usually feeds something else. Question 02 adds each number to a running total, so the queue ends empty and the answer is the total. Question 05 polls one item at a time and compares it to the value it is hunting for with `==`, bumping a counter on a match.

```python
queue = [10, 20, 10, 30, 10, 40]
count = 0

while queue:
    if queue.pop(0) == 10:
        count += 1

print("Count:", count)
```

```text
Count: 3
```

Question 03 needs two accumulators, because an average is a total divided by a count. Track both while you drain, then divide once at the end. In Python `/` always gives a float, so `100 / 4` is `25.0` and no cast is needed.

```python
queue = [10, 20, 30, 40]
total = count = 0

while queue:
    num = queue.pop(0)
    total += num
    count += 1

print("Total:", total, "Count:", count, "Average:", total / count)

```

```text
Total: 100 Count: 4 Average: 25.0

```

---

## Popping an Empty Queue Raises IndexError

Nothing stops you calling `pop(0)` on a list that is already empty. Python does not hand you back `None` and carry on. It stops the program.

```python
queue = []
first = queue.pop(0)
print(first)

```

```text
Traceback (most recent call last):
  File "example.py", line 2, in <module>
    first = queue.pop(0)
IndexError: pop from empty list

```

The fix is the guard you already have. `while queue:` can never reach `pop(0)` with an empty list, because the moment the last item is taken the condition turns false and the loop ends. For a single removal use `if queue:` the same way. Never write a bare `pop(0)` with no check in front of it.

```python
queue = ["Spongebob", "Patrick", "Squidward"]

if queue:
    print(queue.pop(0))

```

```text
Spongebob

```

The same trap waits at `queue[0]`. Reading index `0` of an empty list raises `IndexError: list index out of range`, a different message for the same reason: there is no item there to hand back.

The rule is one sentence long: **every access to the front needs a guard in front of it.** `while queue:` to loop, `if queue:` for one removal.

---

## Why pop(0) Is Slow

This is the one idea in the topic that is not obvious, and it is worth understanding properly.

A Python list keeps its items next to each other in one continuous block of memory, in order, side by side. When you remove the item at index `0`, everything behind it must move one position left to close the gap, so the list stays one unbroken block.

```text
    Before:  [10, 20, 30, 40]     the front is the 10

    Step 1:  remove index 0, the 10 is taken out.
             [20, 30, 40]

    Step 2:  20 must now sit at index 0, 30 at index 1, 40 at index 2.
             To make that true, every one of them slides left.

             +-----+-----+-----+-----+
    before   | 10  | 20  | 30  | 40  |
             +-----+-----+-----+-----+
               ^     ^     ^     ^
              idx 0 idx 1 idx 2 idx 3

    after    +-----+-----+-----+-----+
             | 20  | 30  | 40  |     |
             +-----+-----+-----+-----+
               ^     ^     ^
             slides  slides  slides
             left    left    left

    1 item removed, 3 moves.  3 items in, 1 out, 2 moves.
    n items in, 1 out, n - 1 moves.

```

One `pop(0)` on a queue of n items costs n - 1 moves. That is **O(n)**: the work grows in proportion to the size of the queue. Empty a queue of ten thousand items with a `while queue:` loop and you do around fifty million moves.

Appending at the back is **O(1)** instead: nothing has to move, because the new item lands at the end of the block where it belongs. Python occasionally has to find a bigger block and copy everything across, but spread over many appends the average cost per append stays O(1). That is what "amortised" means, and it is why adding to the back never worries you.

Compare that with a stack. A stack also uses a list, but you add and remove at the same end. `pop()` with no argument takes the last item, and that item is already at the end of the block, so removing it is O(1) for exactly the same reason `append` is. One data structure, O(1) at the back and O(n) at the front. A deque gives you both ends at O(1).

---

## collections.deque for O(1) Removal

The standard library ships a list type made for exactly this job, called `deque`, short for double ended queue. Build it with `deque()` instead of `[]`, and remove from the front with `popleft()` instead of `pop(0)`.

```python
from collections import deque

queue = deque()
queue.append("Spongebob")
queue.append("Patrick")
queue.append("Squidward")

while queue:
    print(queue.popleft())

```

```text
Spongebob
Patrick
Squidward

```

The same logic written both ways, which is the whole swap:

```python
queue = []                                  queue = deque()
queue.append("Spongebob")                    queue.append("Spongebob")
while queue:                                while queue:
    name = queue.pop(0)                         name = queue.popleft()

```

Here is what that buys you, measured on a real run. Each loop moves 100000 items from the front of the queue to the back, 100000 times over.

```python
from collections import deque
from time import perf_counter

N = 100000
for kind in (list, deque):
    queue = kind(range(N))
    start = perf_counter()
    for _ in range(N):
        queue.append(queue.popleft() if kind is deque else queue.pop(0))
    took = perf_counter() - start
    print(f"{kind.__name__:>5} with {N} moves: {took:.3f} s")

```

```text
 list with 100000 moves: 2.013 s
deque with 100000 moves: 0.017 s

```

About a hundred times slower for the list, and the gap widens as the queue grows.

The reason is that a `deque` keeps a pointer to both ends of its block. Removing from the front moves that pointer instead of the items, so nothing shifts and the cost is O(1) however full the queue is. Almost nothing else in your code changes: `append`, `len(queue)`, `if not queue:` and `queue[0]` all work the same, because an empty deque is falsy too and reading index `0` from a deque is fine.

One limitation: you cannot jump to a middle index on a deque, so `queue[2]` raises `TypeError`. If your code only adds at the back and takes from the front, that never comes up.

**The questions in this folder all use the plain list.** That is the version you are practising, and it is correct for any queue you are likely to write by hand. Reach for `deque` the day your queue gets large enough for the difference above to matter.

---

## Reading a Queue

A `for` loop walks a list from index `0` to the end. For a queue that is front to back, the order the items arrived in, so reading is safe and needs no guard.

What is not safe is removing from the same list you are looping over. The loop has already picked its position, and `pop(0)` slides everything left, so the item that slides into that position gets stepped over. It does not crash and it does not warn you. It quietly loses data.

```python
queue = ["Spongebob", "Patrick", "Squidward"]

for name in queue:
    queue.pop(0)
    print("popped", name)

print("Queue is now:", queue)

```

```text
popped Spongebob
popped Squidward
Queue is now: ['Squidward']
```

Three items went in and the loop only saw two. Patrick was removed on the second pass, but the loop had already moved past the slot he slid into, so he was never printed.

There are two clean ways to fix it. **Drain it with a `while` loop**, so the condition is rechecked every pass and there is no position to fall behind. Or **read with a `for` loop and build a second list**, so the list you are walking stays untouched and the keepers go into fresh storage.

Question 04 uses the second pattern, and that is why it needs a second list. It drains the original queue with `while queue:`, keeps the even numbers in `temp`, then pours `temp` back onto the queue, so the survivors are in the queue again in the order they were found.

```python
queue = [1, 2, 3, 4, 5, 6]
temp = []

while queue:
    num = queue.pop(0)
    if num % 2 == 0:
        temp.append(num)

while temp:
    queue.append(temp.pop(0))

print("EVEN:", queue)

```

```text
EVEN: [2, 4, 6]

```

The pattern to burn in: **if you change a list's length while looping over it, use a second list.**

---

## Summary

| What you want | Python | Time |
| --- | --- | --- |
| Build an empty queue | `queue = []` | - |
| Add at the back | `queue.append(item)` | O(1) amortised |
| Remove from the front | `queue.pop(0)` | O(n) |
| Look at the front, keep it | `queue[0]` | O(1) |
| Is it empty? | `if not queue:` | O(1) |
| How many items? | `len(queue)` | O(1) |
| Drain it completely | `while queue:` | - |
| Read it without changing it | `for item in queue:` | O(n) |
| Same end both ways, a stack | `queue.append(item)` / `queue.pop()` | O(1) |
| O(1) at both ends | `deque()` with `popleft()` | O(1) |

Three things to carry into the questions: a queue is a list, so the front is index `0` and `append` / `pop(0)` are the two ends. `pop(0)` on an empty list raises `IndexError`, so guard every removal with `while queue:` or `if queue:`. And `pop(0)` is O(n) because everything shifts left, while `deque` with `popleft()` is O(1) when the queue gets large.

---

## Common Mistakes

Faults that are all about Python lists:

- Calling `queue.pop()` with no `0`. `pop()` removes from the **back**, the same end `append` adds to, so you have built a stack and it prints Squidward, Patrick, Spongebob. Queue behaviour needs `pop(0)`.
- Peeking with `queue[-1]` instead of `queue[0]`. Index `-1` is the last item, which is the back of the queue.
- Popping an empty queue. `pop(0)` on `[]` raises `IndexError: pop from empty list`, and `queue[0]` on `[]` raises `IndexError: list index out of range`. Loop with `while queue:`, never `while True:`.
- Removing from the same list you are looping over with a `for` loop. The shifting makes the loop skip items with no error at all. Use `while queue:`, or a second list as temporary storage.
- Expecting `pop(0)` to be fast. It is O(n), so a long queue pays for every removal twice over. Use `popleft()` on a deque.
- Forgetting that a queue and a stack are the same data structure used from opposite ends. `append` and `pop()` make a stack, `append` and `pop(0)` make a queue.
- Writing `queue.len()`. `len` is a function, not a method, so it is `len(queue)`.

---

## Practice

The five questions for this topic live in this same folder. Each is self contained, with a commented `STARTER` section to attempt and a complete runnable `SOLUTION`, hardcoded data, and no user prompts. Run them one at a time with `python3 question_01.py` and so on.

- [Question 01](./question_01.py)
- [Question 02](./question_02.py)
- [Question 03](./question_03.py)
- [Question 04](./question_04.py)
- [Question 05](./question_05.py)
