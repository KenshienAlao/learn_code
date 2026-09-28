# What is a Stack?

A stack is a collection where you add items to one end and take them off that same end, so the last item you added is the first one you get back. That rule is called **LIFO**, Last In First Out. Python has no `Stack` class, because a plain `list` already does the job as long as you only ever touch the top.

---

## LIFO in One Picture

Push Apple, push Banana, push Orange. Orange went on last, so Orange comes off first.

![Stack LIFO](/assets/stack.webp)

The end of the list is the top of the stack and index `0` is the bottom. `append()` adds at the **end** of the list and `pop()` takes from the **end**, so the end of the list is the top of the stack and index `0` is the bottom. The diagram above is drawn top-first, while the list grows left to right. That mismatch between the picture and the list is the thing that confuses people.

---

## The Four Operations

**`append(item)` puts an item on top.**

```python
stack = []
stack.append("Apple")
stack.append("Banana")
stack.append("Orange")
print(stack)
```

Output:
```
['Apple', 'Banana', 'Orange']
```

There is no `push` method in Python. `list` is a general tool, and `append` is its normal way to add something. If you want to be clear, write the comment `stack.append("Apple")  # push`.

**`pop()` returns the top item and removes it.**

```python
stack = ["Apple", "Banana", "Orange"]
item = stack.pop()
print(item)
print(stack)
```

Output:
```
Orange
['Apple', 'Banana']
```

This one keeps its name. What happens on an empty stack is the one difference, and it has its own section below.

**`stack[-1]` looks at the top without removing it.**

```python
stack = ["Apple", "Banana", "Orange"]
top = stack[-1]
print(top)
print(stack)
```

Output:
```
Orange
['Apple', 'Banana', 'Orange']
```

There is no `peek` method either. Python lets you read from either end of a list with negative indexes, and `-1` is the last item, which here is the top of the stack.

**`len(stack)` is how many items there are, and `if not stack:` is how you check for empty.**

```python
stack = ["Apple", "Banana", "Orange"]
print(len(stack))
if not stack:
    print("empty")
else:
    print("not empty")
```

Output:
```
3
not empty
```

There is no `isEmpty()` method. An empty list is falsy and a non-empty list is truthy, so `not stack` is the check you want. `len()` is a builtin function rather than a method, because any object with a length can use it.

**`item in stack` asks whether a value is somewhere in the stack.**

```python
stack = ["Apple", "Banana", "Orange"]
print("Orange" in stack)
print("Pear" in stack)
```

Output:
```
True
False
```

It answers yes or no, never a position. It also walks the whole stack from the bottom looking for the item, so it is O(n). The other four operations are O(1).

---

## Popping an Empty Stack

`pop()` on an empty list raises `IndexError: pop from empty list`. This is the one thing in this lesson that will crash your program.

```python
stack = []
stack.pop()
```

Output:
```
Traceback (most recent call last):
  File "stack_demo.py", line 2, in <module>
    stack.pop()
    ~~~~~~~~~^^
IndexError: pop from empty list
```

The guard is a plain truth test. Check `if stack:` before every pop.

```python
text = "Hello"
stack = []
for character in text:
    stack.append(character)

result = ""
while stack:
    result = result + stack.pop()
print(result)
```

Output:
```
olleH
```

`while stack:` is the whole guard. It stops the loop at the bottom of the stack without you counting anything.

`stack[-1]` needs the same guard, and the message is different.

```python
stack = []
print(stack[-1])
```

Output:
```
Traceback (most recent call last):
  File "stack_demo.py", line 2, in <module>
    print(stack[-1])
          ~~~~~^^^^
IndexError: list index out of range
```

So `if stack:` protects both operations. If you prefer a length test, `len(stack) == 0` asks the same question. Sometimes you want a stricter condition: `if len(history) > 1:` stops the pop when only one item is left, which is how you keep the first page of a history stack from being popped away.

---

## Reading a Stack Without Changing It

A `for` loop over a stack walks it from **bottom to top**, not from the top down. So it does not give you the pop order.

```python
stack = ["iPhone", "Tablet", "Samsung", "Xiaomi"]
for item in stack:
    print(item)
```

Output:
```
iPhone
Tablet
Samsung
Xiaomi
```

`for item in stack` starts at index `0`, which is the bottom, and walks upwards. There are three ways to read a stack top first.

**Use `stack[::-1]` to get a reversed copy.**

```python
stack = ["iPhone", "Tablet", "Samsung", "Xiaomi"]
for item in stack[::-1]:
    print(item)
print(stack)
```

Output:
```
Xiaomi
Samsung
Tablet
iPhone
['iPhone', 'Tablet', 'Samsung', 'Xiaomi']
```

The slice steps backwards and builds a new list, so the original stack is still full. The cost is a full copy.

**Drain into a temporary list, then put the items back.**

```python
stack = ["iPhone", "Tablet", "Samsung", "Xiaomi"]
temporary = []
while stack:
    temporary.append(stack.pop())

while temporary:
    stack.append(temporary.pop())
print(stack)
print(temporary)
```

Output:
```
['iPhone', 'Tablet', 'Samsung', 'Xiaomi']
[]
```

This is the proper stack way. Popping `temporary` hands you the bottom item first, so pushing it back rebuilds the stack exactly as it was. The fourth question uses the same loop to track the largest value on the way past. You need the copy because a stack only gives items up by destroying them. Without a temporary list the stack ends up empty.

**Index backwards.**

```python
stack = ["iPhone", "Tablet", "Samsung", "Xiaomi"]
for i in range(len(stack) - 1, -1, -1):
    print(stack[i])
```

Output:
```
Xiaomi
Samsung
Tablet
iPhone
```

`range(len(stack) - 1, -1, -1)` counts down from the last index to `0`, so nothing is changed and nothing is copied.

---

## Time Complexity

| Operation | Python | Complexity |
| --- | --- | --- |
| push | `stack.append(x)` | O(1) amortised |
| pop | `stack.pop()` | O(1) amortised |
| peek | `stack[-1]` | O(1) |
| isEmpty | `if not stack:` | O(1) |
| size | `len(stack)` | O(1) |
| search | `x in stack` | O(n) |

"Amortised" in one sentence: now and then a push is slow because the list had to make room by copying everything into a bigger block of memory, but that is rare enough that the average cost of a push stays O(1).

Search is O(n) because a stack is by definition only a top, so `in` has to walk down the whole stack one item at a time to answer the question. Peek, size and isEmpty are O(1) because they only look at the end of the list.

---

## Summary

| Python | What it does |
| --- | --- |
| `stack = []` | an empty stack is just an empty list |
| `stack.append(x)` | pushes on top, which is the end of the list |
| `stack.pop()` | takes the top off and returns it |
| `stack[-1]` | reads the top without removing it |
| `len(stack)` | number of items on the stack |
| `if not stack:` | is the stack empty |
| `x in stack` | is x somewhere in the stack |
| LIFO | last in, first out, index 0 is the bottom |

---

## Common Mistakes

- Popping an empty stack. You get `IndexError: pop from empty list` and the program stops. Guard every pop with `if stack:`, or loop with `while stack:`.
- Forgetting the `if stack:` guard before a peek. `stack[-1]` on an empty list raises `IndexError: list index out of range` too.
- Assuming a `for` loop visits a stack top first. It goes from index `0` upwards, so it reads bottom to top. Use `stack[::-1]`, a drain into a temporary list, or count down with `range(len(stack) - 1, -1, -1)`.
- Typing `stack.pop(0)` by mistake. That takes the **front** item, which is the bottom, and it is O(n) because every remaining item has to shift down. Bare `pop()` is the top and is O(1). Popping the front turns your stack into a queue.
- Mutating a stack while looping over it. Popping inside `for item in stack` skips items, because the loop is reading indexes that have already moved. Drain into a temporary list first, or loop `while stack:`.
- Expecting `append` to return the item. `append` returns `None`, so `stack = stack.append("Apple")` sets your stack to `None`. Same trap with `stack = stack.sort()`.
- Thinking the end of the list is the bottom. It is the top. A stack drawn with the top at the top of the page runs the opposite way to the list.

---

## Practice

Each question runs on its own with no `input()`. Run one with `python3 question_01.py`.

- [Question 01](./question_01.py)
- [Question 02](./question_02.py)
- [Question 03](./question_03.py)
- [Question 04](./question_04.py)
- [Question 05](./question_05.py)

Question 01 pushes and pops characters to reverse a string, question 02 checks balanced parentheses and bails out when a `)` arrives on an empty stack, question 03 drains into a temporary list to print top first and pushes it all back, question 04 does the same while tracking the largest value, and question 05 uses `len(history) > 1` as the guard so the first page survives.