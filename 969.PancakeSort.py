import doctest
# For doc testing

def pancake_sort(arr):
  """
  Return a sorted array using flip() function
  Arguments:
    arr (list): unsorted array
  Output:
    arr (list): modified array

  >>> pancake_sort([1, 5, 4, 3, 2])
  [1, 2, 3, 4, 5]

  >>> pancake_sort([2, 3, 1, 5, 4])
  [1, 2, 3, 4, 5]
  """
  j = 0
  while j != len(arr):
    start = 0
    for i in range(1,len(arr)):
      if arr[start] > arr[i]:
        arr[start:i+1] = flip(arr[start:i+1], 2)
      start+=1
    j += 1
  return arr
  
def flip(arr, k):
  # O(n) way of reversal
  start = 0
  # Till the midpoint
  for i in range(k//2):
    buffer = arr[i]
    arr[i] = arr[k-i-1]
    arr[k-i-1] = buffer
  return arr

# Test results
doctest.testmod()