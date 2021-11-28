"""
Given a list, move all even numbers before odd. Best if maintain relative order and use O(1) space
"""

def sortArrayByParity(nums):
    """
    >>> sortArrayByParity([3,1,2,4])
    [2, 4, 3, 1]

    >>> sortArrayByParity([0,-1,2,3])
    [0, 2, -1, 3]
    """
    write = 0
    # Go through each number
    for read in range(len(nums)):
        # Keep track of left-most odd and left-most even number
        if nums[read] % 2 == 0:
            # Swap
            nums[read], nums[write] = nums[write], nums[read]
            write += 1  # Pointer stays with the first odd number unless a swap happened
    return nums

import doctest
doctest.testmod()