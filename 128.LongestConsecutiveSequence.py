import doctest

def longestConsecutive(nums):
    """
    Return the longest consecutive sequence in an unsorted list
    Arguments:
        nums: an unsorted array

    * Same number will be included in the longest subsequence

    >>> longestConsecutive([1,1,2])
    3

    >>> longestConsecutive([2,3,1])
    3
    """

    opt_len, freq = 0, {}
    
    # Go thru each number and add to frequency map
    for n in nums:
        if n not in freq:
            # New key
            freq[n] = 1
            
    # Go thru each number and check for longest sub-sequence
    for i in range(len(nums)):
        current = nums[i]
        if current-1 not in freq:
            so_far = 0
            while current in freq:
                so_far += freq[current]
                current += 1
            opt_len = max(opt_len, so_far)
    return opt_len

# Testing
# Case 1 (1,2,3,4)
assert longestConsecutive([100,4,200,1,3,2]) == 4
