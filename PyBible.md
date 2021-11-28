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

A.append(x)
A.remove(x)
A.insert(index, x)
del A[i:j] - remove slice
