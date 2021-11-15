# Problem: Two sum
# Date: 11/5/2021
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

# My solution
def twoSum(nums, target):
    """
    Return a tuple of the indices of the pair of numbers that add up to target
    IN:
        nums (list) - a list of integers
        target (int) - two numbers add up to this
    OUT:
        pairIndex (tuple) - pair of elements that add up to target
    
    DOC-TEST
    >>> twoSum([3,2,4], 6)
    [1, 2]

    >>> twoSum([3,3], 6)
    [0, 1]

    >>> twoSum([1,2,3], 100)

    My Approach:
    - Use hashmap
        - Go thru the list once, record the difference between target and element (e.g. 9-2 = 7)
        - Call this complement: Map difference to complement {7:0, 2:1}
    - Loop
        - Go thru the list once more, check if current number's complement is in dictionary
            - e.g. [2,7,11], is current index 0 (num of 2) in {7:0, 2:1} -> yes, return [1,0]
    My take-aways:
        - Use hashmap to store {signal: thing you want to find} such that when you have the correct signal you can pinpoint your goal
    
    """
    # Store difference between target and current number
    num2index = {}
    
    # Create the hashmap by going through each number
    for i in range(len(nums)):
        # Get complement of the number
        complement = target-nums[i]
        # Check if complement is in our hashmap
        if (complement in num2index) and (num2index[complement] != i):
            # If complement not in num2index, then the second statement won't be evaluated
            return [num2index[complement], i]
        # Always add this element to our growing hash map
        num2index[nums[i]] = i
    # Just in case, write out explicitly
    return None

# My tests
if __name__ == '__main__':
    import doctest
    doctest.testmod()