"""
Problem: Move Zeroes
Date: 11/5/21
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 
Follow up: Could you minimize the total number of operations done?
"""

def moveZeros(nums):
    """
    Modify original list such that all zeros are at the end while non-zero elements maintain same order
    IN:
        nums (list): a list of integers

    My Approach:
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            print(i, j)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Test case 1
    a = [0,1,0,3,12]
    b = [0]
    moveZeros(c)
    print(c)
    c = [4,2,4,0,0,3,0,5,1,0]
