"""
Problem: Median of an array
Date: 11/9/21
Given two sorted arrays, find the median of all elements in the combined arrays

Example 1:

Input: nums1 = [1,2,3], nums2 =[4,5,6]
Output: 3.5

Input: Input: nums1 = [1,2,3,4,5,6], nums2 =[0,0,0,10,10,10]
sorted(nums1+nums2) = [0,0,0,1,2,3,4,5,6,10,10,10]
Output: 3.5

My Approach:
    - divide and conquer
    - check median of each sub array at each step

What I learned:
    - 
"""

def findMedian(nums1, nums2):
    """
    Return median of the two arrays
    IN:
        nums1 (list): a sorted list
        nums2 (list): a different sorted list
    OUT:
        totalMedian (float): median of the whole array

    Doc test
    >>> findMedian([2, 3], [4, 5])
    3.5
    >>> findMedian([1,2,3], [4,5,6])
    3.5

    """
    # Find median of current arrays in constant time
    isFirstOddLength = len(nums1)%2 == 1
    isSecondOddLength = len(nums2)%2 == 1

    midpt1, midpt2 = len(nums1)//2, len(nums2)//2

    # Base case
    if len(nums1) == 2 and len(nums2) == 2:
        totalSum = (max(nums1[0], nums2[0]) + min(nums1[1], nums2[1]))
        return float(totalSum)/2

    median1 = nums1[midpt1] if isFirstOddLength else (sum(nums1[midpt1-1: midpt1+1])/2)  # Even length takes the middle two numbers
    median2 = nums2[midpt2] if isSecondOddLength else (sum(nums2[midpt2-1: midpt2+1])/2)

    # Compare the medians
    if median1 == median2:
        # Same median means the total median is also the same (invariant)
        return median1
    elif median1 > median2:
        # First array has more larger spacing, drop the large elements, like how we cross out the right end numbers when calculating median
        return findMedian(nums1[:midpt1+1], nums2[midpt2:])  # Include midpoint
    else:
        return findMedian(nums1[midpt1:], nums2[:midpt2+1])  # Include midpoint

if __name__ == '__main__':
    import doctest
    doctest.testmod()
