"""
Move Zeros:

Move all zeros in a list to the end of the list, while preserving the relative order of the list

e.g. [0,1,2,0,5] -> [1,2,5,0,0]

This problem is an architype for move a certain signal to one side of the list

"""

def moveZeros(nums):
    """
    Modify original list such that all zeros are at the end while non-zero elements maintain same order
    IN:
        nums (list): a list of integers

    My Approach:
    - like quicksort, keep track of the left-most zero and the left-most nonzero element using two pointers
    - must go through each element once O(n)
    - space complexity can be O(1)
    """
    write = 0
    for read in range(len(nums)):
        # Check if element is nonzero, if so, swap
        if nums[read] != 0:
            nums[read], nums[write] = nums[write], nums[read]
            # Only increment counter when we visit nonzero element (so for zero, the pointer would halt until we reach the first nonzero)
            write += 1
    return nums


if __name__ == '__main__':
    # Test case 1
    a = [0,1,0,3,12]
    moveZeros(a)
    print(a)
    assert a == [1,3,12,0,0]
