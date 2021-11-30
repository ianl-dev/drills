Python Bible

MAKE LIST BY RANGE: list(range(100))

- [1] + [0]\*10
- C = list(A)

* C and A are same content, but different objects
* different than C = A (affect both)

Last element in list is -1, then -2 counting backward in index

REVERSE: A[::-1]

- Rotate by Slicing: A[k:] + A[:k] rotates k steps to the left
  Remember: A[:shift-diff], A[shift-diff:] swap, symmetry

  - diff = len(first sliced part) - len(second sliced part)
  - shift = -1\*k since we are moving right (not left)
  - shift = -1\* (k%len(A)) since when move steps > len => mod

- In place
  A.sort()
  A.reverse()
- Make copy
  sorted(A) => list copy
  reversed(A) => iterator

- Permutation
c = [(x,y) for x in a for y in b]

- String
Immutable -> cannot set index value
s.strip() -> remove any space
s.startswith(prefix) -> True/False start with prefix?
s.endswith(suffix) -> True/False end with suffix?
','.join(iterable) -> return a string
s.lower() -> create a new string which stores the lower version
s.upper()

Setting is creating new array:
s = s[1:]
s += '123' 
Meaning: To concatenate n letters, it takes n^2 time
Extra space 
Alternative to string: list in python
As always, try to write values from the back

A.append(x)
A.remove(x)
A.insert(index, x)
del A[i:j] - remove slice
